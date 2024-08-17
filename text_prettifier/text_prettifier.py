import re 
import contractions
from .utils.patterns import Patterns
from internet_words_remover import words_remover
class TextPrettifier:
    __EMOJI_PATTERN = Patterns().emoji_pattern()
    __HTML_PATTERN = Patterns().html_pattern()
    __URL_PATTERN = Patterns().url_pattern()
    __NUMBER_PATTERN = Patterns().number_pattern()
    __SPECIAL_CHAR_PUNCTUATION_PATTERN = Patterns().special_char_punctuation_pattern()
    __STOP_WORDS = Patterns().stopword_pattern()

    def __init__(self) -> None:
        """
        Initialize the TextPrettifier object.
        
        The constructor is empty because all necessary initialization is done
        at the class level with class attributes.
        """
        pass

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

    def sigma_cleaner(self, text: str, is_token: bool = False, is_lower: bool = False):
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

        Returns:
        -------
        str or list
            Cleaned text as a string or list of tokens based on `is_token`.
        
        Example:
        --------
        >>> cleaner = TextPrettifier()
        >>> cleaner.sigma_cleaner('Hello <b>world</b>! 123 :)', is_token=True, is_lower=True)
        ['hello', 'world', '']
        """
        text = self.remove_emojis(text)
        text = self.remove_internet_words(text)
        text = self.remove_html_tags(text)
        text = self.remove_urls(text)
        text = self.remove_numbers(text)
        text = self.remove_special_chars(text)
        text = self.remove_contractions(text)
        text = self.remove_stopwords(text)
        if is_lower and is_token:
            return text.lower().split()
        elif is_lower:
            return text.lower()
        elif is_token:
            return text.split()
        else:
            return text

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
    tp=TextPrettifier()
    text="Hello, how are you?"
    print(tp.sigma_cleaner(text,is_token=True,is_lower=True))
    