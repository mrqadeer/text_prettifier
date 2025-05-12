from setuptools import setup, find_packages
import codecs
import os

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()

VERSION = '2.0.1'  # Updated version
DESCRIPTION = "A Python library for cleaning and preprocessing text data with asynchronous and multithreading capabilities."


KEYWORDS = [
    'text cleaning', 'text preprocessing', 'text scrubber', 'NLP', 'natural language processing',
    'data cleaning', 'data preprocessing', 'string manipulation', 'text manipulation',
    'stopwords removal', 'contractions expansion', 'text normalization', 'text sanitization',
    'internet words removal', 'emojis removal', 'emojis killer', 'asynchronous', 'async',
    'multithreading', 'parallel processing', 'batch processing'
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
    install_requires=[
        'contractions', 
        'nltk',
        'internet-words-remover',
        'typing; python_version < "3.8"'
    ],
    python_requires='>=3.6',
    keywords=KEYWORDS,
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
        "Topic :: Text Processing",
        "Topic :: Text Processing :: Linguistic",
        "License :: OSI Approved :: MIT License",
    ],
)
