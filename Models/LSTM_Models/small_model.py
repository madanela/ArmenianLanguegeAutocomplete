#!/usr/bin/env python
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.layers import Embedding, LSTM, Dense, Bidirectional
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.models import Sequential
from tensorflow.keras.optimizers import Adam

#rom Models.Scraping_Preprocessing.load_model import *
from .. import *
from Models.Scraping_Preprocessing import ArmScraping

# Path of Pretrained model
data_path = 'Models/Trained/small_LSTM/'

# This model contains tokenizer, max_sequence_len and model seperately trained and we load it to use pretrained one on Sample data
tokenizer,max_sequence_len ,model = Load_all(data_path)



seed_text = "Բարև ձեզ"
next_words = 10 #number of words to predict

#Prediction
for _ in range(next_words):
    token_list = tokenizer.texts_to_sequences([seed_text])[0]
    token_list = pad_sequences([token_list], maxlen= max_sequence_len -1, padding='pre')
    predicted = model.predict(token_list, verbose=0)
    output_word = ""
    for word, index in tokenizer.word_index.items():
        if index == predicted.argmax():
            output_word = word
            break
    output_word
    seed_text += " " + output_word
    print(seed_text)
