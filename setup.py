from setuptools import setup, find_packages
import codecs
import os

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()

VERSION = '1.1.3'  
DESCRIPTION = "A Python library for cleaning and preprocessing text data by removing,emojies,internet words, special characters, digits, HTML tags, URLs, and stopwords."


KEYWORDS = [
    'text cleaning', 'text preprocessing', 'text scrubber', 'NLP', 'natural language processing',
    'data cleaning', 'data preprocessing', 'string manipulation', 'text manipulation',
    'stopwords removal', 'contractions expansion', 'text normalization', 'text sanitization',
    'internet words removal','emojis removal','emojis killer'
]

# Setting up
setup(
    name="text-prettifier",
    version=VERSION,
    author="Qadeer Ahmad",
    author_email="mrqadeer1231122@gmail.com",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=long_description,
    packages=find_packages(),
    install_requires=['contractions', 'nltk','internet-words-remover'],  
    keywords=KEYWORDS,
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ],
)
