from google.cloud import language_v1
import os
current_directory = os.getcwd()
# Ensure your credentials file path is correctly set
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = f"{current_directory}/gcloud-credentials.json"

def analyze_sentiment(comments):
    client = language_v1.LanguageServiceClient()
    results = []
    for comment_data in comments:
        comment = comment_data['comment']
        # Create a Document object with language detection enabled
        document = language_v1.Document(content=comment, type_=language_v1.Document.Type.PLAIN_TEXT)
        
        # Analyze sentiment and detect the language
        response = client.analyze_sentiment(request={'document': document, 'encoding_type': language_v1.EncodingType.UTF8})
        sentiment = response.document_sentiment
        language = response.language  # Language code, e.g., 'en', 'es', 'kn'
        
        sentiment_category = categorize_sentiment(sentiment.score)

        results.append({
            'comment': comment,
            'author': comment_data['author'],
            'like_count': comment_data['like_count'],
            'published_at': comment_data['published_at'],
            'score': round(sentiment.score, 2),
            'language': language,
            'language_full': get_language_name(language),
            'sentiment_category': sentiment_category
        })
    return results

def categorize_sentiment(score):
    if score > 0.3:
        return 'Positive'
    elif score < -0.3:
        return 'Negative'
    else:
        return 'Neutral'

def get_language_name(code):
    languages = {
        'en': 'English',
        'es': 'Spanish',
        'ja': 'Japanese',
        'zh': 'Chinese (Simplified)',
        'zh-TW': 'Chinese (Traditional)',
        'fr': 'French',
        'de': 'German',
        'it': 'Italian',
        'ko': 'Korean',
        'pt': 'Portuguese',
        'ru': 'Russian',
        'kn': 'Kannada'
    }
    return languages.get(code, 'Unknown')