from keras.models import load_model
from keras.preprocessing.text import Tokenizer
from keras.preprocessing.sequence import pad_sequences
import pandas as pd 
import re
import numpy as np

data = pd.read_csv('dataset_tw.csv',names=['text', 'sentiment'], sep='::')
# Keeping only the neccessary columns
data = data[['text','sentiment']]

data = data[data.sentiment != "neutral"]
data['text'] = data['text'].apply(lambda x: x.lower())
data['text'] = data['text'].apply((lambda x: re.sub('[^a-zA-z0-9\\s]','',x)))

for idx,row in data.iterrows():
    row[0] = row[0].replace('rt',' ')
    
max_fatures = 2000
tokenizer = Tokenizer(num_words=max_fatures, split=' ')
tokenizer.fit_on_texts(data['text'].values)

twt = ['HELLO TO EVERYBODY YOU ARE A WONDERFUL DICK SUCKER, IDIOT AND STUPID NIGGA.']
#vectorizing the tweet by the pre-fitted tokenizer instance
twt = tokenizer.texts_to_sequences(twt)
#padding the tweet to have exactly the same shape as `embedding_2` input
twt = pad_sequences(twt, maxlen=27, dtype='int32', value=0)
print(twt)
model = load_model('red')
sentiment = model.predict(twt,batch_size=1,verbose = 2)[0]
if(np.argmax(sentiment) == 0):
    print("negative")
elif (np.argmax(sentiment) == 1):
    print("positive")