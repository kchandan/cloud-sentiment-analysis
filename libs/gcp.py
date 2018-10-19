from google.cloud import language

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