# TextPrettifier

TextPrettifier is a Python library for cleaning text data by removing HTML tags, URLs, numbers, special characters, contractions, and stopwords.
## TextPrettifier Key Features

### 1. Removing Emojis
The `remove_emojis` method removes emojis from the text.

### 2. Removing Internet Words
The `remove_internet_words` method removes internet-specific words from the text.

### 3. Removing HTML Tags
The `remove_html_tags` method removes HTML tags from the text.

### 4. Removing URLs
The `remove_urls` method removes URLs from the text.

### 5. Removing Numbers
The `remove_numbers` method removes numbers from the text.

### 6. Removing Special Characters
The `remove_special_chars` method removes special characters from the text.

### 7. Expanding Contractions
The `remove_contractions` method expands contractions in the text.

### 8. Removing Stopwords
The `remove_stopwords` method removes stopwords from the text.

### Additional Functionality
- If `is_lower` and `is_token` are both `True`, the text is returned in lowercase and as a list of tokens.
- If only `is_lower` is `True`, the text is returned in lowercase.
- If only `is_token` is `True`, the text is returned as a list of tokens.
- If neither `is_lower` nor `is_token` is `True`, the text is returned as is.


## Installation

You can install TextPrettifier using pip:

```bash
pip install text-prettifier
```
```python
from text_prettifier import TextPrettifier
```
### Initialize TextPrettifier
text_prettifier = TextPrettifier()

#### Example: Remove Emojis
```python
html_text = "Hi,Pythonogist! I ❤️ Python."
cleaned_html = text_prettifier.remove_emojis(html_text)
print(cleaned_html)
```
**Output**
Hi,Pythonogist! I Python.
#### Example: Remove HTML tags
```python
html_text = "<p>Hello, <b>world</b>!</p>"
cleaned_html = text_prettifier.remove_html_tags(html_text)
print(cleaned_html)
```
**Output**
Hello,world!
#### Example: Remove URLs
```python
url_text = "Visit our website at https://example.com"
cleaned_urls = text_prettifier.remove_urls(url_text)
print(cleaned_urls)
```
**Output**
Visit our webiste at
#### Example: Remove numbers
```python
number_text = "There are 123 apples"
cleaned_numbers = text_prettifier.remove_numbers(number_text)
print(cleaned_numbers)
```
**Output**
There are apples
#### Example: Remove special characters
```python
special_text = "Hello, @world!"
cleaned_special = text_prettifier.remove_special_chars(special_text)
print(cleaned_special)
```
**Output**
Hello world
#### Example: Remove contractions
```python
contraction_text = "I can't do it"
cleaned_contractions = text_prettifier.remove_contractions(contraction_text)
print(cleaned_contractions)
```
**Output**
I cannot do it
#### Example: Remove stopwords
```python
stopwords_text = "This is a test"
cleaned_stopwords = text_prettifier.remove_stopwords(stopwords_text)
print(cleaned_stopwords)
```
**Output**
This test
#### Example: Apply all cleaning methods
```python
all_text = "<p>Hello, @world!</p> There are 123 apples. I can't do it. This is a test."
all_cleaned = text_prettifier.sigma_cleaner(all_text)
print(all_cleaned)

```
**Output**
Hello world 123 apples cannot test


```If you are interested to tokenized and lower the cleaned text write the code```
```python
all_text = "<p>Hello, @world!</p> There are 123 apples. I can't do it. This is a test."
all_cleaned = text_prettifier.sigma_cleaner(all_text,is_token=True,is_lower=True)
print(all_cleaned)

```
**Output**
['Hello','world', '123','apples', 'cannot','test']

**Note:** I didn't include ```remove_numbers``` in ```sigma_cleaner``` because sometimes numbers carry useful information in term of NLP. If you want to remove number you can apply this method seperately on output of ```sigma_cleaner```.


### Contact Information

Feel free to reach out to me on social media:

[![GitHub](https://img.shields.io/badge/GitHub-mrqadeer)](https://github.com/mrqadeer)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Qadeer)](https://www.linkedin.com/in/qadeer-ahmad-3499a4205/)
[![Twitter](https://img.shields.io/badge/Twitter-Twitter)](https://twitter.com/mr_sin_of_me)
[![Facebook](https://img.shields.io/badge/Facebook-Facebook)](https://web.facebook.com/mrqadeerofficial/)




## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
