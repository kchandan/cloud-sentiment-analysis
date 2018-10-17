dataset = ["Food is good and not too expensive. Serving is just right for adult. Ambient is nice too.",
           "Used to be good. Chicken soup was below average, bbq used to be good.",
           "Food was good, standouts were the spicy beef soup and seafood pancake! ",
           "Good office lunch or after work place to go to with a big group as they have a lot of private areas with large tables",
           "As a Korean person, it was very disappointing food quality and very pricey for what you get. I won't go back there again. ",
           "Not great quality food for the price. Average food at premium prices really.",
           "Fast service. Prices are reasonable and food is decent.",
           "Extremely long waiting time. Food is decent but definitely not worth the wait.",
           "Clean premises, tasty food. My family favourites are the clear Tom yum soup, stuffed chicken wings, chargrilled squid.",
           "really good and authentic Thai food! in particular, we loved their tom yup clear soup with sliced fish. it's so well balanced that we can have it just on its own. "
           ]

def gc_sentiment(text):  
    from google.cloud import language
    
    client = language.LanguageServiceClient()
    document = language.types.Document(
            content=text,
            type=language.enums.Document.Type.PLAIN_TEXT)
    annotations = client.analyze_sentiment(document=document)
    score = annotations.document_sentiment.score
    magnitude = annotations.document_sentiment.magnitude
    return score, magnitude

from tqdm import tqdm # This is an awesome package for tracking for loops
import pandas as pd
gc_results = [gc_sentiment(row) for row in tqdm(dataset, ncols = 100)]
gc_score, gc_magnitude = zip(*gc_results) # Unpacking the result into 2 lists
gc = list(zip(dataset, gc_score, gc_magnitude))
columns = ['text', 'score', 'magnitude']
gc_df = pd.DataFrame(gc, columns = columns)
print (gc_df)