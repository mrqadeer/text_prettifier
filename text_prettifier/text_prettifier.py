import re 
import contractions
from nltk.corpus import stopwords
from internet_words_remover import words_remover
class TextPrettifier:
    def __init__(self) -> None:
        """
        Initialize the TextPrettifier object.
        """
        self.__pattern_html_tags=re.compile('<.*?>')
        self.__pattern_urls=re.compile(r"https?://\S+|www\.\S+|git@\S+")
        self.__pattern_special_char_punctuations=re.compile(r'[!"#$%&\'()*+,\-./:;<=>?@\[\\\]^_`{|}~]')
        self.__pattern_numbers=re.compile(r"\d+")
        self.__all_stopwords=set(stopwords.words('english'))
        self.__pattern_stopwords = r'\b(?:{})\b'.format('|'.join(self.__all_stopwords))
        self.__emoji_pattern = re.compile("["
                                u"\U0001F600-\U0001F64F"  # emoticons
                                u"\U0001F300-\U0001F5FF"  # symbols & pictographs
                                u"\U0001F680-\U0001F6FF"  # transport & map symbols
                                u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
                                u"\U00002500-\U00002BEF"  # chinese char
                                u"\U00002702-\U000027B0"
                                u"\U00002702-\U000027B0"
                                u"\U000024C2-\U0001F251"
                                u"\U0001f926-\U0001f937"
                                u"\U00010000-\U0010ffff"
                                u"\u2640-\u2642"
                                u"\u2600-\u2B55"
                                u"\u200d"
                                u"\u23cf"
                                u"\u23e9"
                                u"\u231a"
                                u"\ufe0f"  # dingbats
                                u"\u3030"
                                "]+", flags=re.UNICODE)
    def remove_emojis(self,text):
        return self.__emoji_pattern.sub(r'', text) 
    def remove_html_tags(self,text:str)->str:
        """
        Remove HTML tags from text.

        Parameters:
        ------
        text (str): The input text containing HTML tags.

        Returns:
        ------
        str: Text with HTML tags removed.

        Example:
        ------
        >>> cleaner = TextPrettifier()
        >>> cleaner.remove_html_tags('<p>Hello</p>')
        
        Output:
        ------
        'Hello'
        """
        text=re.sub(self.__pattern_html_tags,'',text).strip()
        # for extra spaces
        text=re.sub(r'\s+', ' ', text).strip()
        return text
    
    def remove_urls(self,text:str)->str:
        """
        Remove URLs from text.

        Parameters:
        ------
        text (str): The input text containing URLs.

        Returns:
        str: Text with URLs removed.

        Example:
        ------
        >>> cleaner = TextPrettifier()
        >>> cleaner.remove_urls('Visit our website at https://example.com')
        
        Output:
        ------
        'Visit our website at'
        """
        text=re.sub(self.__pattern_urls,'',text).strip()
        # for extra spaces
        text=re.sub(r'\s+', ' ', text).strip()
        return text
    
    def remove_numbers(self,text:str)->str:
        """
        Remove numbers from text.

        Parameters:
        ------
        text (str): The input text containing numbers.

        Returns:
        ------
        str: Text with numbers removed.

        Example:
        ------
        >>> cleaner = TextPrettifier()
        >>> cleaner.remove_numbers('There are 123 apples')
        
        Output:
        ------
        'There are apples'
        """
        text=re.sub(self.__pattern_numbers,'',text).strip()
        # for extra spaces
        text=re.sub(r'\s+', ' ', text).strip()
        return text
    
    def remove_special_chars(self,text:str)->str:
        """
        Remove special characters and punctuations from text.

        Parameters:
        ------
        text (str): The input text containing special characters and punctuations.

        Returns:
        ------
        str: Text with special characters and punctuations removed.

        Example:
        ------
        >>> cleaner = TextPrettifier()
        >>> cleaner.remove_special_chars('Hello, world!')
        
        Output:
        ------
        'Hello world'
        """
        text=re.sub(self.__pattern_special_char_punctuations,'',text).strip()
        # for extra spaces
        text=re.sub(r'\s+', ' ', text).strip()
        return text
    
    def remove_contractions(self,text:str)->str:
        """
        Expand contractions in text.

        Parameters:
        ------
        text (str): The input text containing contractions.

        Returns:
        ------
        str: Text with contractions expanded.

        Example:
        ------
        >>> cleaner = TextPrettifier()
        >>> cleaner.remove_contractions("I can't do it")
        
        Output:
        ------
        'I cannot do it'
        """
        text=contractions.fix(text).strip()
        # for extra spaces
        text=re.sub(r'\s+', ' ', text).strip()
        return text
    
    def remove_stopwords(self,text:str)->str:
        """
        Remove stopwords from text.

        Parameters:
        ------
        text (str): The input text containing stopwords.

        Returns:
        ------
        str: Text with stopwords removed.

        Example:
        ------
        >>> cleaner = TextPrettifier()
        >>> cleaner.remove_stopwords('This is a test')
        
        Output:
        ------
        'This test'
        """
        text=re.sub(self.__pattern_stopwords,'',text,flags=re.IGNORECASE).strip()
        # for extra spaces
        text=re.sub(r'\s+', ' ', text).strip()
        
        
        return text
    
    def remove_internet_words(self,text:str):
        """
        Remove internet slang words from text.

        Parameters:
        ------
        text (str): The input text containing internet slang words.

        Returns:
        ------
        str: Text with internet slang words removed.

        Example:
        ------
        >>> cleaner = TextPrettifier()
        >>> cleaner.removing_internet_words('This is an osm moment of my life.')
        
        Output:
        ------
        'This is an awesome moment of my life.'
        """
        text=words_remover(text).strip()
        # for extra spaces
        text=re.sub(r'\s+', ' ', text).strip()
        
        return text

    def sigma_cleaner(self,text:str,is_token:bool=False,is_lower:bool=False):
        """
        Apply all cleaning methods to text.

        Parameters:
        ------
        text (str): The input text to be cleaned.

        Returns:
        ------
        str: Cleaned text after applying all cleaning methods.
        list: Cleaned list after applying all cleaning methods if is_token is True 

        Example:
        ------
        >>> cleaner = TextPrettifier()
        >>> cleaner.sigma_cleaner('This is a <p>test</p> with 123 numbers')
        
        Output:
        ------
        'This test numbers'
        """
        text=self.remove_emojis(text)
        text=self.remove_internet_words(text)
        text=self.remove_html_tags(text)
        text=self.remove_urls(text)
        text=self.remove_numbers(text)
        text=self.remove_special_chars(text)
        text=self.remove_contractions(text)
        text=self.remove_stopwords(text)
        if is_lower and is_token:
            return text.lower().split()
        elif is_lower:
            return text.lower()
        elif is_token:
            return text.split()
        else:
            return text
    
    def __str__(self) -> str:
        return "Purify the Text!!"
tp=TextPrettifier()