# patterns.py

import re
from nltk.corpus import stopwords

class Patterns:
    @staticmethod
    def html_pattern():
        return re.compile('<.*?>')

    @staticmethod
    def url_pattern():
        return re.compile(r"https?://\S+|www\.\S+|git@\S+")

    @staticmethod
    def special_char_punctuation_pattern():
        return re.compile(r'[!"#$%&\'()*+,\-./:;<=>?@\[\\\]^_`{|}~]')

    @staticmethod
    def number_pattern():
        return re.compile(r"\d+")

    @staticmethod
    def stopword_pattern():
        stopwords_list = set(stopwords.words('english'))
        return r'\b(?:{})\b'.format('|'.join(stopwords_list))

    @staticmethod
    def emoji_pattern():
        return re.compile("["
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
