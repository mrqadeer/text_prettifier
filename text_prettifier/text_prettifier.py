import re 
import contractions
import asyncio
import concurrent.futures
from typing import List, Union, Optional, Callable, Dict, Any, Tuple
from functools import partial
from .utils.patterns import Patterns
from internet_words_remover import words_remover
from nltk.stem import PorterStemmer, WordNetLemmatizer
from multiprocessing import cpu_count

lemmatizer = WordNetLemmatizer()

class TextPrettifier:
    __EMOJI_PATTERN = Patterns().emoji_pattern()
    __HTML_PATTERN = Patterns().html_pattern()
    __URL_PATTERN = Patterns().url_pattern()
    __NUMBER_PATTERN = Patterns().number_pattern()
    __SPECIAL_CHAR_PUNCTUATION_PATTERN = Patterns().special_char_punctuation_pattern()
    __STOP_WORDS = Patterns().stopword_pattern()

    def __init__(self, max_workers: Optional[int] = None) -> None:
        """
        Initialize the TextPrettifier object.
        
        Parameters:
        ----------
        max_workers : Optional[int]
            Maximum number of worker threads. If None, defaults to the number of CPUs.
        """
        self.max_workers = max_workers or cpu_count()

    def remove_emojis(self, text: str) -> str:
        """
        Remove emojis from the input text.

        Parameters:
        ----------
        text : str
            The input text containing emojis.

        Returns:
        -------
        str
            The text with emojis removed.

        Example:
        --------
        >>> cleaner = TextPrettifier()
        >>> cleaner.remove_emojis('Hello 😊 world! 🌍')
        'Hello  world! '
        """
        return self.__EMOJI_PATTERN.sub(r'', text)

    async def aremove_emojis(self, text: str) -> str:
        """
        Asynchronously remove emojis from the input text.

        Parameters:
        ----------
        text : str
            The input text containing emojis.

        Returns:
        -------
        str
            The text with emojis removed.
        """
        loop = asyncio.get_event_loop()
        return await loop.run_in_executor(None, self.remove_emojis, text)

    def remove_html_tags(self, text: str) -> str:
        """
        Remove HTML tags from the input text.

        Parameters:
        ----------
        text : str
            The input text containing HTML tags.

        Returns:
        -------
        str
            The text with HTML tags removed.

        Example:
        --------
        >>> cleaner = TextPrettifier()
        >>> cleaner.remove_html_tags('<p>Hello</p> <b>world</b>')
        'Hello world'
        """
        text = re.sub(self.__HTML_PATTERN, '', text).strip()
        text = re.sub(r'\s+', ' ', text).strip()
        return text

    async def aremove_html_tags(self, text: str) -> str:
        """
        Asynchronously remove HTML tags from the input text.

        Parameters:
        ----------
        text : str
            The input text containing HTML tags.

        Returns:
        -------
        str
            The text with HTML tags removed.
        """
        loop = asyncio.get_event_loop()
        return await loop.run_in_executor(None, self.remove_html_tags, text)

    def remove_urls(self, text: str) -> str:
        """
        Remove URLs from the input text.

        Parameters:
        ----------
        text : str
            The input text containing URLs.

        Returns:
        -------
        str
            The text with URLs removed.

        Example:
        --------
        >>> cleaner = TextPrettifier()
        >>> cleaner.remove_urls('Check this out: https://example.com')
        'Check this out:'
        """
        text = re.sub(self.__URL_PATTERN, '', text).strip()
        text = re.sub(r'\s+', ' ', text).strip()
        return text

    async def aremove_urls(self, text: str) -> str:
        """
        Asynchronously remove URLs from the input text.

        Parameters:
        ----------
        text : str
            The input text containing URLs.

        Returns:
        -------
        str
            The text with URLs removed.
        """
        loop = asyncio.get_event_loop()
        return await loop.run_in_executor(None, self.remove_urls, text)

    def remove_numbers(self, text: str) -> str:
        """
        Remove numbers from the input text.

        Parameters:
        ----------
        text : str
            The input text containing numbers.

        Returns:
        -------
        str
            The text with numbers removed.

        Example:
        --------
        >>> cleaner = TextPrettifier()
        >>> cleaner.remove_numbers('There are 123 apples and 456 oranges.')
        'There are apples and oranges.'
        """
        text = re.sub(self.__NUMBER_PATTERN, '', text).strip()
        text = re.sub(r'\s+', ' ', text).strip()
        return text

    async def aremove_numbers(self, text: str) -> str:
        """
        Asynchronously remove numbers from the input text.

        Parameters:
        ----------
        text : str
            The input text containing numbers.

        Returns:
        -------
        str
            The text with numbers removed.
        """
        loop = asyncio.get_event_loop()
        return await loop.run_in_executor(None, self.remove_numbers, text)

    def remove_special_chars(self, text: str) -> str:
        """
        Remove special characters and punctuations from the input text.

        Parameters:
        ----------
        text : str
            The input text containing special characters and punctuations.

        Returns:
        -------
        str
            The text with special characters and punctuations removed.

        Example:
        --------
        >>> cleaner = TextPrettifier()
        >>> cleaner.remove_special_chars('Hello, world!')
        'Hello world'
        """
        text = re.sub(self.__SPECIAL_CHAR_PUNCTUATION_PATTERN, '', text).strip()
        text = re.sub(r'\s+', ' ', text).strip()
        return text

    async def aremove_special_chars(self, text: str) -> str:
        """
        Asynchronously remove special characters and punctuations from the input text.

        Parameters:
        ----------
        text : str
            The input text containing special characters and punctuations.

        Returns:
        -------
        str
            The text with special characters and punctuations removed.
        """
        loop = asyncio.get_event_loop()
        return await loop.run_in_executor(None, self.remove_special_chars, text)

    def remove_contractions(self, text: str) -> str:
        """
        Expand contractions in the input text.

        Parameters:
        ----------
        text : str
            The input text containing contractions.

        Returns:
        -------
        str
            The text with contractions expanded.

        Example:
        --------
        >>> cleaner = TextPrettifier()
        >>> cleaner.remove_contractions("I can't do it.")
        'I cannot do it.'
        """
        text = contractions.fix(text).strip()
        text = re.sub(r'\s+', ' ', text).strip()
        return text

    async def aremove_contractions(self, text: str) -> str:
        """
        Asynchronously expand contractions in the input text.

        Parameters:
        ----------
        text : str
            The input text containing contractions.

        Returns:
        -------
        str
            The text with contractions expanded.
        """
        loop = asyncio.get_event_loop()
        return await loop.run_in_executor(None, self.remove_contractions, text)

    def remove_stopwords(self, text: str) -> str:
        """
        Remove stopwords from the input text.

        Parameters:
        ----------
        text : str
            The input text containing stopwords.

        Returns:
        -------
        str
            The text with stopwords removed.

        Example:
        --------
        >>> cleaner = TextPrettifier()
        >>> cleaner.remove_stopwords('This is a test sentence.')
        'This test sentence.'
        """
        text = re.sub(self.__STOP_WORDS, '', text, flags=re.IGNORECASE).strip()
        text = re.sub(r'\s+', ' ', text).strip()
        return text

    async def aremove_stopwords(self, text: str) -> str:
        """
        Asynchronously remove stopwords from the input text.

        Parameters:
        ----------
        text : str
            The input text containing stopwords.

        Returns:
        -------
        str
            The text with stopwords removed.
        """
        loop = asyncio.get_event_loop()
        return await loop.run_in_executor(None, self.remove_stopwords, text)

    def remove_internet_words(self, text: str) -> str:
        """
        Remove internet slang words from the input text.

        Parameters:
        ----------
        text : str
            The input text containing internet slang words.

        Returns:
        -------
        str
            The text with internet slang words replaced.

        Example:
        --------
        >>> cleaner = TextPrettifier()
        >>> cleaner.remove_internet_words('This is an osm moment.')
        'This is an awesome moment.'
        """
        text = words_remover(text).strip()
        text = re.sub(r'\s+', ' ', text).strip()
        return text

    async def aremove_internet_words(self, text: str) -> str:
        """
        Asynchronously remove internet slang words from the input text.

        Parameters:
        ----------
        text : str
            The input text containing internet slang words.

        Returns:
        -------
        str
            The text with internet slang words replaced.
        """
        loop = asyncio.get_event_loop()
        return await loop.run_in_executor(None, self.remove_internet_words, text)

    def lemmatize_text(self, text: str, pos: str = "v") -> str:
        """
        Lemmatize the words in the input text.

        Parameters:
        ----------
        text : str
            The input text to lemmatize.
        pos : str, optional
            Part of speech for lemmatization. Default is "v" (verb).

        Returns:
        -------
        str
            The text with lemmatized words.
        """
        words = text.lower().split()
        return " ".join([lemmatizer.lemmatize(word, pos=pos) for word in words])

    async def alemmatize_text(self, text: str, pos: str = "v") -> str:
        """
        Asynchronously lemmatize the words in the input text.

        Parameters:
        ----------
        text : str
            The input text to lemmatize.
        pos : str, optional
            Part of speech for lemmatization. Default is "v" (verb).

        Returns:
        -------
        str
            The text with lemmatized words.
        """
        loop = asyncio.get_event_loop()
        return await loop.run_in_executor(None, partial(self.lemmatize_text, pos=pos), text)

    def stem_text(self, text: str) -> str:
        """
        Apply stemming to the words in the input text.

        Parameters:
        ----------
        text : str
            The input text to stem.

        Returns:
        -------
        str
            The text with stemmed words.
        """
        ps = PorterStemmer()
        words = text.lower().split()
        return " ".join([ps.stem(word) for word in words])

    async def astem_text(self, text: str) -> str:
        """
        Asynchronously apply stemming to the words in the input text.

        Parameters:
        ----------
        text : str
            The input text to stem.

        Returns:
        -------
        str
            The text with stemmed words.
        """
        loop = asyncio.get_event_loop()
        return await loop.run_in_executor(None, self.stem_text, text)

    def sigma_cleaner(self, text: str, 
                     is_token: bool = False, 
                     is_lower: bool = False,
                     is_lemmatize: bool = False, 
                     is_stemming: bool = False,
                     keep_numbers: bool = True) -> Union[str, List[str]]:
        """
        Apply all cleaning methods to the input text.

        Parameters:
        ----------
        text : str
            The input text to be cleaned.
        is_token : bool, optional
            If True, returns the text as a list of tokens. Default is False.
        is_lower : bool, optional
            If True, converts the text to lowercase. Default is False.
        is_lemmatize : bool, optional
            If True, lemmatizes the text. Default is False.
        is_stemming : bool, optional
            If True, applies stemming to the text. Default is False.
        keep_numbers : bool, optional
            If True, keeps numbers in the text. Default is True.

        Returns:
        -------
        Union[str, List[str]]
            Cleaned text as a string or list of tokens based on `is_token`.
        
        Example:
        --------
        >>> cleaner = TextPrettifier()
        >>> cleaner.sigma_cleaner('Hello <b>world</b>! 123 :)', is_token=True, is_lower=True)
        ['hello', 'world', '123']
        """
        text = self.remove_emojis(text)
        text = self.remove_internet_words(text)
        text = self.remove_html_tags(text)
        text = self.remove_urls(text)
        if not keep_numbers:
            text = self.remove_numbers(text)
        text = self.remove_special_chars(text)
        text = self.remove_contractions(text)
        text = self.remove_stopwords(text)
        
        if is_lower:
            text = text.lower()
            
        if is_lemmatize:
            text = self.lemmatize_text(text)
        elif is_stemming:
            text = self.stem_text(text)
            
        if is_token:
            return text.split()
        
        return text

    async def asigma_cleaner(self, text: str, 
                                 is_token: bool = False, 
                                 is_lower: bool = False,
                                 is_lemmatize: bool = False, 
                                 is_stemming: bool = False,
                                 keep_numbers: bool = True) -> Union[str, List[str]]:
        """
        Asynchronously apply all cleaning methods to the input text.

        Parameters:
        ----------
        text : str
            The input text to be cleaned.
        is_token : bool, optional
            If True, returns the text as a list of tokens. Default is False.
        is_lower : bool, optional
            If True, converts the text to lowercase. Default is False.
        is_lemmatize : bool, optional
            If True, lemmatizes the text. Default is False.
        is_stemming : bool, optional
            If True, applies stemming to the text. Default is False.
        keep_numbers : bool, optional
            If True, keeps numbers in the text. Default is True.

        Returns:
        -------
        Union[str, List[str]]
            Cleaned text as a string or list of tokens based on `is_token`.
        """
        text = await self.aremove_emojis(text)
        text = await self.aremove_internet_words(text)
        text = await self.aremove_html_tags(text)
        text = await self.aremove_urls(text)
        if not keep_numbers:
            text = await self.aremove_numbers(text)
        text = await self.aremove_special_chars(text)
        text = await self.aremove_contractions(text)
        text = await self.aremove_stopwords(text)
        
        if is_lower:
            text = text.lower()
            
        if is_lemmatize:
            text = await self.alemmatize_text(text)
        elif is_stemming:
            text = await self.astem_text(text)
            
        if is_token:
            return text.split()
        
        return text

    def process_batch(self, texts: List[str], 
                     is_token: bool = False, 
                     is_lower: bool = False,
                     is_lemmatize: bool = False, 
                     is_stemming: bool = False,
                     keep_numbers: bool = True) -> List[Union[str, List[str]]]:
        """
        Process a batch of texts in parallel using multithreading.

        Parameters:
        ----------
        texts : List[str]
            List of input texts to be cleaned.
        is_token : bool, optional
            If True, returns each text as a list of tokens. Default is False.
        is_lower : bool, optional
            If True, converts each text to lowercase. Default is False.
        is_lemmatize : bool, optional
            If True, lemmatizes each text. Default is False.
        is_stemming : bool, optional
            If True, applies stemming to each text. Default is False.
        keep_numbers : bool, optional
            If True, keeps numbers in each text. Default is True.

        Returns:
        -------
        List[Union[str, List[str]]]
            List of cleaned texts.
        """
        with concurrent.futures.ThreadPoolExecutor(max_workers=self.max_workers) as executor:
            func = partial(
                self.sigma_cleaner,
                is_token=is_token,
                is_lower=is_lower,
                is_lemmatize=is_lemmatize,
                is_stemming=is_stemming,
                keep_numbers=keep_numbers
            )
            results = list(executor.map(func, texts))
        return results

    async def aprocess_batch(self, texts: List[str], 
                                 is_token: bool = False, 
                                 is_lower: bool = False,
                                 is_lemmatize: bool = False, 
                                 is_stemming: bool = False,
                                 keep_numbers: bool = True) -> List[Union[str, List[str]]]:
        """
        Asynchronously process a batch of texts in parallel.

        Parameters:
        ----------
        texts : List[str]
            List of input texts to be cleaned.
        is_token : bool, optional
            If True, returns each text as a list of tokens. Default is False.
        is_lower : bool, optional
            If True, converts each text to lowercase. Default is False.
        is_lemmatize : bool, optional
            If True, lemmatizes each text. Default is False.
        is_stemming : bool, optional
            If True, applies stemming to each text. Default is False.
        keep_numbers : bool, optional
            If True, keeps numbers in each text. Default is True.

        Returns:
        -------
        List[Union[str, List[str]]]
            List of cleaned texts.
        """
        tasks = [
            self.asigma_cleaner(
                text,
                is_token=is_token,
                is_lower=is_lower,
                is_lemmatize=is_lemmatize,
                is_stemming=is_stemming,
                keep_numbers=keep_numbers
            )
            for text in texts
        ]
        return await asyncio.gather(*tasks)

    def chunk_and_process(self, text: str, chunk_size: int = 10000, 
                         is_token: bool = False, 
                         is_lower: bool = False,
                         is_lemmatize: bool = False, 
                         is_stemming: bool = False,
                         keep_numbers: bool = True) -> str:
        """
        Process a large text by splitting it into chunks and processing in parallel.

        Parameters:
        ----------
        text : str
            The large input text to be processed.
        chunk_size : int, optional
            The size of each chunk in characters. Default is 10000.
        is_token : bool, optional
            If True, returns the text as a list of tokens. Default is False.
        is_lower : bool, optional
            If True, converts the text to lowercase. Default is False.
        is_lemmatize : bool, optional
            If True, lemmatizes the text. Default is False.
        is_stemming : bool, optional
            If True, applies stemming to the text. Default is False.
        keep_numbers : bool, optional
            If True, keeps numbers in the text. Default is True.

        Returns:
        -------
        Union[str, List[str]]
            Processed text, either as a string or list of tokens.
        """
        # Chunk the text
        chunks = [text[i:i + chunk_size] for i in range(0, len(text), chunk_size)]
        
        # Process chunks in parallel
        processed_chunks = self.process_batch(
            chunks,
            is_token=False,  # We'll tokenize at the end if needed
            is_lower=is_lower,
            is_lemmatize=is_lemmatize,
            is_stemming=is_stemming,
            keep_numbers=keep_numbers
        )
        
        # Combine results
        result = " ".join(processed_chunks)
        
        # Tokenize if requested
        if is_token:
            return result.split()
        
        return result

    async def achunk_and_process(self, text: str, chunk_size: int = 10000, 
                                     is_token: bool = False, 
                                     is_lower: bool = False,
                                     is_lemmatize: bool = False, 
                                     is_stemming: bool = False,
                                     keep_numbers: bool = True) -> str:
        """
        Asynchronously process a large text by splitting it into chunks and processing in parallel.

        Parameters:
        ----------
        text : str
            The large input text to be processed.
        chunk_size : int, optional
            The size of each chunk in characters. Default is 10000.
        is_token : bool, optional
            If True, returns the text as a list of tokens. Default is False.
        is_lower : bool, optional
            If True, converts the text to lowercase. Default is False.
        is_lemmatize : bool, optional
            If True, lemmatizes the text. Default is False.
        is_stemming : bool, optional
            If True, applies stemming to the text. Default is False.
        keep_numbers : bool, optional
            If True, keeps numbers in the text. Default is True.

        Returns:
        -------
        Union[str, List[str]]
            Processed text, either as a string or list of tokens.
        """
        # Chunk the text
        chunks = [text[i:i + chunk_size] for i in range(0, len(text), chunk_size)]
        
        # Process chunks in parallel
        processed_chunks = await self.aprocess_batch(
            chunks,
            is_token=False,  # We'll tokenize at the end if needed
            is_lower=is_lower,
            is_lemmatize=is_lemmatize,
            is_stemming=is_stemming,
            keep_numbers=keep_numbers
        )
        
        # Combine results
        result = " ".join(processed_chunks)
        
        # Tokenize if requested
        if is_token:
            return result.split()
        
        return result

    def __str__(self) -> str:
        """
        Return a string representation of the TextPrettifier object.

        Returns:
        -------
        str
            A string indicating that the object is for text purification.

        Example:
        --------
        >>> cleaner = TextPrettifier()
        >>> print(cleaner)
        Purify the Text!!
        """
        return "Purify the Text!!"

if __name__ == "__main__":
    tp = TextPrettifier()
    text = "Hello, how are you?"
    print(tp.sigma_cleaner(text, is_token=True, is_lower=True))
    
    # Example of batch processing
    texts = ["Hello, how are you?", "I'm doing well!", "<p>HTML content</p>"]
    results = tp.process_batch(texts, is_lower=True)
    print(results)
    
    # Example of processing a large text
    large_text = "Hello, how are you?" * 1000
    result = tp.chunk_and_process(large_text, chunk_size=1000, is_lower=True)
    print(f"Processed {len(large_text)} characters, result length: {len(result)}")
    
    # Example of using async (requires running in an async context)
    async def async_example():
        result = await tp.asigma_cleaner("Hello, how are you?", is_lower=True)
        print(result)
        
        batch_results = await tp.aprocess_batch(texts, is_lower=True)
        print(batch_results)
        
        large_result = await tp.achunk_and_process(large_text, chunk_size=1000, is_lower=True)
        print(f"Async processed {len(large_text)} characters, result length: {len(large_result)}")
    
    # You would run this in an async environment:
    # asyncio.run(async_example())
