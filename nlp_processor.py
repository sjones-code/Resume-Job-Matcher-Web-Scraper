# nlp_processor.py
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

def process_text(text):
    """Processes text to get a list of meaningful keywords."""
    if not text:
        return []

    # Lowercase everything
    text = text.lower()

    # Tokenize into words
    words = word_tokenize(text)

    # Remove stopwords and non-alphanumeric tokens
    stop_words = set(stopwords.words('english'))
    filtered_words = [word for word in words if word.isalnum() and word not in stop_words]

    return filtered_words
