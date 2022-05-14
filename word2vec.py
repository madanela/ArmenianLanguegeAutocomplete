# IMPORTS 
import gensim 
import pandas as pd
import pickle

# Preparing Data 

df1 = pd.read_csv('DATA/wiki_data.txt', sep=":", header=None)
df2 = pd.read_csv('DATA/wiki_data_2.txt', sep=":", header=None)
df3 = pd.read_csv('DATA/wiki_data_3.txt', sep=":", header=None)
df4 = pd.read_csv('DATA/wiki_data_4.txt', sep=":", header=None)

df1 = df1.append(df2,ignore_index = True)
df1 = df1.append(df3, ignore_index = True)
df1 = df1.append(df4, ignore_index = True)
df = df1

df = df.drop(labels=1, axis=1)
df.rename(columns = {0:'reviewText'}, inplace = True)

# Looping over the Data and separating it into sentences. 
review_text = df.reviewText.apply(gensim.utils.simple_preprocess)

# Creating the model
model = gensim.models.Word2Vec(
    window=10, # 10 words before and after
    min_count=2, # if u have a sentence that has 1 word do not use 
    workers=4, 
)

model.build_vocab(review_text, progress_per=1000)

# Training the model with initially prepared data
model.train(review_text, total_examples=model.corpus_count, epochs=model.epochs)

pickle.dump(model, open("Models/word2vec/model.pkl", "wb"))