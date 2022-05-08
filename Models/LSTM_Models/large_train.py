import tensorflow as tf
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.layers import Embedding, LSTM, Dense, Bidirectional
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.models import Sequential
from tensorflow.keras.optimizers import Adam
import numpy as np


tokenizer = Tokenizer()

data = open('Data/Scraped/wiki_data_3.txt').read()

import tensorflow as tf
print("Num GPUs Available: ", len(tf.config.list_physical_devices('GPU')))
print(tf. __version__)
corpus = data.lower().split("\n")
tokenizer.fit_on_texts(corpus)
total_words = len(tokenizer.word_index) + 1

input_sequences = []
for line in corpus:
    token_list = tokenizer.texts_to_sequences([line])[0]
    for i in range(1, len(token_list)):
        n_gram_sequence = token_list[:i+1]
        input_sequences.append(n_gram_sequence)
        
        
# pad sequences
max_sequence_len = 512
print("hello")
input_sequences = np.array(pad_sequences(input_sequences, maxlen=max_sequence_len, padding='pre'))

print("hello")
# create predictors and label
xs, labels = input_sequences[:,:-1],input_sequences[:,-1]
ys = labels


#Model build
model = Sequential()
model.add(Embedding(total_words, 200, input_length=max_sequence_len-1))
model.add(Bidirectional(LSTM(250)))
model.add(Dense(total_words, activation='softmax'))
adam = Adam(lr=0.01)
model.compile(loss=tf.keras.losses.SparseCategoricalCrossentropy(), optimizer=adam, metrics=['accuracy'])


#earlystop = EarlyStopping(monitor='val_loss', min_delta=0, patience=5, verbose=0, mode='auto')
history = model.fit(xs, ys, epochs=5, verbose=1,workers = 4)
 

seed_text = "Բարև բոլորին, ես այսօր առավօտյան գնալու եմ  "
next_words = 10

#Prediction

for _ in range(next_words):
    token_list = tokenizer.texts_to_sequences([seed_text])[0]
    token_list = pad_sequences([token_list], maxlen=max_sequence_len-1, padding='pre') # making all input length the same
    predicted = model.predict(token_list, verbose=0)
    output_word = ""
    for word, index in tokenizer.word_index.items():
        if index == predicted.argmax():
            output_word = word
            break
    output_word
    seed_text += " " + output_word
    print(seed_text)
    
    
    
# this part is saving model 3 pieces, Tokenizer, max_sequence_len, Model which is used in this model.
import pickle
data_path = 'Models/Trained/large_LSTM/'

model.save(data_path + 'model_onwiki2')
with open(data_path + 'tokenizer_onwiki2.pickle', 'wb') as handle:
    pickle.dump(tokenizer, handle, protocol=pickle.HIGHEST_PROTOCOL)
import configparser
config = configparser.ConfigParser()
config['modelparams']={'max_sequence_len':max_sequence_len}

with open(data_path + 'config.ini', 'w') as configfile:
   config.write(configfile)