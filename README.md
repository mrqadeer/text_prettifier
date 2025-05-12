# TextPrettifier

TextPrettifier is a Python library for cleaning text data by removing HTML tags, URLs, numbers, special characters, contractions, and stopwords. It now features asynchronous processing and multithreading capabilities for efficient processing of large texts.

## Key Features

### Text Cleaning Features

#### 1. Removing Emojis
The `remove_emojis` method removes emojis from the text.

#### 2. Removing Internet Words
The `remove_internet_words` method removes internet-specific words from the text.

#### 3. Removing HTML Tags
The `remove_html_tags` method removes HTML tags from the text.

#### 4. Removing URLs
The `remove_urls` method removes URLs from the text.

#### 5. Removing Numbers
The `remove_numbers` method removes numbers from the text.

#### 6. Removing Special Characters
The `remove_special_chars` method removes special characters from the text.

#### 7. Expanding Contractions
The `remove_contractions` method expands contractions in the text.

#### 8. Removing Stopwords
The `remove_stopwords` method removes stopwords from the text.

### Advanced Processing Features

#### 9. Asynchronous Processing
All methods have async counterparts prefixed with 'a' (e.g., `aremove_emojis`) for non-blocking operations.

#### 10. Batch Processing
Process multiple texts in parallel with `process_batch` and `aprocess_batch`.

#### 11. Chunked Processing for Large Texts
Efficiently process large texts with `chunk_and_process` and `achunk_and_process`.

#### 12. Lemmatization and Stemming
Apply lemmatization or stemming to text with dedicated methods.

## Installation

You can install TextPrettifier using pip:

```bash
pip install text-prettifier
```

## Quick Start

### Basic Usage

```python
from text_prettifier import TextPrettifier

# Initialize TextPrettifier
text_prettifier = TextPrettifier()

# Example: Remove Emojis
html_text = "Hi,Pythonogist! I ❤️ Python."
cleaned_html = text_prettifier.remove_emojis(html_text)
print(cleaned_html)  # Output: Hi,Pythonogist! I Python.

# Example: Apply all cleaning methods
all_text = "<p>Hello, @world!</p> There are 123 apples. I can't do it. This is a test."
all_cleaned = text_prettifier.sigma_cleaner(all_text, is_lower=True)
print(all_cleaned)  # Output: hello world 123 apples cannot test

# Get tokens with cleaning
tokens = text_prettifier.sigma_cleaner(all_text, is_token=True, is_lower=True)
print(tokens)  # Output: ['hello', 'world', '123', 'apples', 'cannot', 'test']
```

### Asynchronous Processing

```python
import asyncio
from text_prettifier import TextPrettifier

async def process_text():
    text_prettifier = TextPrettifier()
    
    text = "Hello, @world! 123 I can't believe it. 😊"
    result = await text_prettifier.asigma_cleaner(text, is_lower=True)
    print(result)  # Output: hello world 123 cannot believe

# Run the async function
asyncio.run(process_text())
```

### Batch Processing

```python
from text_prettifier import TextPrettifier

# Initialize with specific number of worker threads
text_prettifier = TextPrettifier(max_workers=4)

# Process multiple texts in parallel
texts = [
    "Hello, how are you? 😊",
    "<p>This is HTML</p> content",
    "Visit https://example.com for more info",
    "I can't believe it's not butter!"
]

# Synchronous batch processing
results = text_prettifier.process_batch(texts, is_lower=True)
for text, result in zip(texts, results):
    print(f"Original: {text}")
    print(f"Cleaned: {result}")
    print()

# Asynchronous batch processing
async def process_async():
    results = await text_prettifier.aprocess_batch(texts, is_lower=True)
    for text, result in zip(texts, results):
        print(f"Original: {text}")
        print(f"Cleaned: {result}")
        print()

# Run in an async environment
# asyncio.run(process_async())
```

### Processing Large Texts

```python
from text_prettifier import TextPrettifier

text_prettifier = TextPrettifier()

# Create a large text for demonstration
large_text = "Hello, this is a sample text with some HTML <p>tags</p> and URLs https://example.com and emojis 😊" * 1000

# Process the large text efficiently by chunking
result = text_prettifier.chunk_and_process(
    large_text,
    chunk_size=5000,  # Process in chunks of 5000 characters
    is_lower=True,
    keep_numbers=True
)

print(f"Original length: {len(large_text)}")
print(f"Processed length: {len(result)}")

# Asynchronous processing of large text
async def process_large_async():
    result = await text_prettifier.achunk_and_process(
        large_text,
        chunk_size=5000,
        is_lower=True,
        keep_numbers=True
    )
    print(f"Original length: {len(large_text)}")
    print(f"Processed length: {len(result)}")

# Run in an async environment
# asyncio.run(process_large_async())
```

### Lemmatization and Stemming

```python
from text_prettifier import TextPrettifier

text_prettifier = TextPrettifier()

text = "I am running in the park with friends"

# Apply lemmatization
lemmatized = text_prettifier.sigma_cleaner(text, is_lemmatize=True)
print(lemmatized)  # Output: I run park friend

# Apply stemming
stemmed = text_prettifier.sigma_cleaner(text, is_stemming=True)
print(stemmed)  # Output: I run park friend
```

## Advanced Configuration

TextPrettifier supports various configuration options:

```python
text_prettifier = TextPrettifier(max_workers=8)  # Set maximum worker threads

# Configure sigma_cleaner options
result = text_prettifier.sigma_cleaner(
    text,
    is_token=True,       # Return tokens instead of a string
    is_lower=True,       # Convert to lowercase
    is_lemmatize=True,   # Apply lemmatization
    is_stemming=False,   # Don't apply stemming (would override lemmatization)
    keep_numbers=True    # Keep numbers in the text
)
```

## Contact Information

Feel free to reach out to me on social media:

[![GitHub](https://img.shields.io/badge/GitHub-mrqadeer)](https://github.com/mrqadeer)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Qadeer)](https://www.linkedin.com/in/qadeer-ahmad-3499a4205/)
[![Twitter](https://img.shields.io/badge/Twitter-Twitter)](https://twitter.com/mr_sin_of_me)
[![Facebook](https://img.shields.io/badge/Facebook-Facebook)](https://web.facebook.com/mrqadeerofficial/)

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
