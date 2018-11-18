from google.cloud import language
from google.cloud import translate

class gcp:
    def __init__(self):
        pass
    def gc_sentiment(self,text):  
        client = language.LanguageServiceClient()
        document = language.types.Document(
                content=text,
                type=language.enums.Document.Type.PLAIN_TEXT)
        annotations = client.analyze_sentiment(document=document)
        score = annotations.document_sentiment.score
        magnitude = annotations.document_sentiment.magnitude
        return score, magnitude
    def detect_language(self,text):
        # [START translate_detect_language]
        """Detects the text's language."""
        translate_client = translate.Client()

        # Text can also be a sequence of strings, in which case this method
        # will return a sequence of results for each text.
        result = translate_client.detect_language(text)

        print('Text: {}'.format(text))
        print('Confidence: {}'.format(result['confidence']))
        print('Language: {}'.format(result['language']))
        # [END translate_detect_language]

if __name__ == '__main__':
    g = gcp()
    g.detect_language("Hello world my name is chandan")