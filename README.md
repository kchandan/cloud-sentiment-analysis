# AI API As Service

## Cloud based Sentiment Analysis

This provides easy to use API wrappers around popular public cloud services.

### Before you start

1. You will need Twitter dev account setup.( for Streaming analytics )
2. AWS account setup ( To use AWS Comprehend )
3. Azure account setup ( To use Azure Text Analytics )
4. GCP account setup ( To use GCP ML )

### Directory/file Layout

1. ~/.aws/credentials - For AWS keys
2. ~/.azure/credentials - For Azure keys
3. Use env variables for GCP
4. ~/twitter/credentials - For Twitter Dev keys

### Credential file setup

1. Twitter
```
[default]
consumer_key = 
consumer_secret = 
access_token = 
access_token_secret = 
```
2. Azure

```
[default]
key1 = 
key2 = 
region = eastus2
```
3. AWS
```
[default]
aws_access_key_id = 
aws_secret_access_key = 
region = us-east-1
```
### Installation Step


Install all dependencies.
```
pip3 -r requirements.txt
```

### Start 

Start Jupyter notebook

```
jupyter notebook
```

Do a quick offline test to check Installation
```
python offline-tweet-analyze.py
```

Once all account etc are set try full stream 
```
python tweet-stream-analyze.py
```

Copyright: Chandan Kumar, beCloudReady Inc
