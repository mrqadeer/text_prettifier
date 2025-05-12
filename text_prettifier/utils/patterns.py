# patterns.py

import re
from typing import Pattern, Dict, Any, Set, Optional, Callable
from functools import lru_cache
from nltk.corpus import stopwords

class Patterns:
    """
    Class providing common regex patterns for text cleaning.
    
    This class provides static methods to generate regular expression patterns 
    for various text cleaning operations like removing HTML tags, URLs, 
    special characters, numbers, stopwords, and emojis.
    """
    
    _patterns_cache: Dict[str, Pattern] = {}
    
    @staticmethod
    @lru_cache(maxsize=1)
    def html_pattern() -> Pattern:
        """
        Returns a compiled regex pattern for matching HTML tags.
        
        Returns:
        -------
        Pattern
            Compiled regex pattern for HTML tags.
        """
        return re.compile('<.*?>')

    @staticmethod
    @lru_cache(maxsize=1)
    def url_pattern() -> Pattern:
        """
        Returns a compiled regex pattern for matching URLs.
        
        Returns:
        -------
        Pattern
            Compiled regex pattern for URLs.
        """
        return re.compile(r"https?://\S+|www\.\S+|git@\S+")

    @staticmethod
    @lru_cache(maxsize=1)
    def special_char_punctuation_pattern() -> Pattern:
        """
        Returns a compiled regex pattern for matching special characters and punctuation.
        
        Returns:
        -------
        Pattern
            Compiled regex pattern for special characters and punctuation.
        """
        return re.compile(r'[!"#$%&\'()*+,\-./:;<=>?@\[\\\]^_`{|}~]')

    @staticmethod
    @lru_cache(maxsize=1)
    def number_pattern() -> Pattern:
        """
        Returns a compiled regex pattern for matching numbers.
        
        Returns:
        -------
        Pattern
            Compiled regex pattern for numbers.
        """
        return re.compile(r"\d+")

    @staticmethod
    @lru_cache(maxsize=1)
    def stopword_pattern(language: str = 'english') -> str:
        """
        Returns a regex pattern string for matching stopwords in the specified language.
        
        Parameters:
        ----------
        language : str, optional
            The language for stopwords. Default is 'english'.
        
        Returns:
        -------
        str
            Regex pattern string for stopwords.
        """
        try:
            stopwords_list = set(stopwords.words(language))
            return r'\b(?:{})\b'.format('|'.join(stopwords_list))
        except Exception as e:
            # Fallback to a minimal English stopwords list if NLTK data is not available
            fallback_stopwords = {
                "i", "me", "my", "myself", "we", "our", "ours", "ourselves", "you", "your", 
                "yours", "yourself", "yourselves", "he", "him", "his", "himself", "she", "her", 
                "hers", "herself", "it", "its", "itself", "they", "them", "their", "theirs", 
                "themselves", "what", "which", "who", "whom", "this", "that", "these", "those", 
                "am", "is", "are", "was", "were", "be", "been", "being", "have", "has", "had", 
                "having", "do", "does", "did", "doing", "a", "an", "the", "and", "but", "if", 
                "or", "because", "as", "until", "while", "of", "at", "by", "for", "with", 
                "about", "against", "between", "into", "through", "during", "before", "after", 
                "above", "below", "to", "from", "up", "down", "in", "out", "on", "off", "over", 
                "under", "again", "further", "then", "once", "here", "there", "when", "where", 
                "why", "how", "all", "any", "both", "each", "few", "more", "most", "other", 
                "some", "such", "no", "nor", "not", "only", "own", "same", "so", "than", "too", 
                "very", "s", "t", "can", "will", "just", "don", "don't", "should", "now"
            }
            return r'\b(?:{})\b'.format('|'.join(fallback_stopwords))

    @staticmethod
    @lru_cache(maxsize=1)
    def emoji_pattern() -> Pattern:
        """
        Returns a compiled regex pattern for matching emojis.
        
        Returns:
        -------
        Pattern
            Compiled regex pattern for emojis.
        """
        return re.compile("["
                            u"\U0001F600-\U0001F64F"  # emoticons
                            u"\U0001F300-\U0001F5FF"  # symbols & pictographs
                            u"\U0001F680-\U0001F6FF"  # transport & map symbols
                            u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
                            u"\U00002500-\U00002BEF"  # chinese char
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

    @staticmethod
    @lru_cache(maxsize=1)
    def whitespace_pattern() -> Pattern:
        """
        Returns a compiled regex pattern for matching multiple whitespace characters.
        
        Returns:
        -------
        Pattern
            Compiled regex pattern for whitespace.
        """
        return re.compile(r'\s+')

    @staticmethod
    @lru_cache(maxsize=1)
    def email_pattern() -> Pattern:
        """
        Returns a compiled regex pattern for matching email addresses.
        
        Returns:
        -------
        Pattern
            Compiled regex pattern for email addresses.
        """
        return re.compile(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b')

    @staticmethod
    @lru_cache(maxsize=1)
    def hashtag_pattern() -> Pattern:
        """
        Returns a compiled regex pattern for matching hashtags.
        
        Returns:
        -------
        Pattern
            Compiled regex pattern for hashtags.
        """
        return re.compile(r'#\w+')

    @staticmethod
    @lru_cache(maxsize=1)
    def mention_pattern() -> Pattern:
        """
        Returns a compiled regex pattern for matching mentions (@username).
        
        Returns:
        -------
        Pattern
            Compiled regex pattern for mentions.
        """
        return re.compile(r'@\w+')
