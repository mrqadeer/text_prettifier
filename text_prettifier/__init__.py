"""
TextPrettifier: A Python library for advanced text preprocessing.

This library provides tools for cleaning and preprocessing text data by removing
emojis, internet words, special characters, digits, HTML tags, URLs, and stopwords.
It supports both synchronous and asynchronous processing, as well as 
batch processing for large texts.
"""

from .text_prettifier import TextPrettifier
from .version import __version__, git_revision as __git_version__

__all__ = ['TextPrettifier', '__version__', '__git_version__']