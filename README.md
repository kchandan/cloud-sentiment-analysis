# AI API As Service

This is umbrella project to create API wrappers around most Public cloud services to make usage of these services Cloud Agnostic.

Please feel free to report bug or contribute.

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
>python offline-tweet-analyze.py
                                              tweets  Py_polarity aws_sentiment  azure_score
0  RT @RepMaxineWaters: Why does Trump have such ...         0.25       NEUTRAL     0.856162
1  BBC News - Migrant caravan: Mexico to deport g...         0.00       NEUTRAL     0.896271
2  RT @acupoker: So the Saudis push this rhetoric...         0.00       NEUTRAL     0.500000
3  RT @SethAbramson: Keep in mind that while the ...         0.00       NEUTRAL     0.500000
4  RT @LindseyGrahamSC: @realDonaldTrump I suppor...         0.00       NEUTRAL     0.250855
5  RT @LadyLibertyInEx: Can even TWO Trump rallie...         0.16       NEUTRAL     0.500000
6  RT @GeorgeTakei: Folks are acting as though we...         0.00       NEUTRAL     0.195102
7  RT @GeorgeTakei: Make no mistake: Trump is tes...         0.10       NEUTRAL     0.760210
8  RT @eugenegu: We have an outbreak of E. Coli O...        -0.80      NEGATIVE     0.049141
9  RT @Knowhatmatters: @caitoz “You don’t get to ...         0.00       NEUTRAL     0.500000
```

Once all account etc are set try full stream 
```
python tweet-stream-analyze.py
```

Copyright: Chandan Kumar, beCloudReady Inc

Reach me: chandank@becloudready.com
