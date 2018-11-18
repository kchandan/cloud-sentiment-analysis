import boto3
import json

class aws_comp:
    def __init__(self,region):
        self.comprehend = boto3.client(service_name='comprehend', region_name=region)

    def detect_lang(self,text):
        print('Calling DetectDominantLanguage')
        output = self.comprehend.detect_dominant_language(Text = text)
        for lang in output['Languages']:
            print (lang['LanguageCode'], lang['Score'])


if __name__ == "__main__":
    a = aws_comp('us-east-1')
    a.detect_lang("Use access keys to make secure REST or HTTP Query protocol requests to AWS service APIs")

