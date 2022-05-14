import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle
import gensim 
from tensorflow.keras.preprocessing.sequence import pad_sequences
from transformers import TFGPT2LMHeadModel,GPT2Tokenizer
import tensorflow as tf
import string



from Models.Scraping_Preprocessing.load_model import *
data_path = 'Models/Trained/large_LSTM/'
tokenizer_lstm,max_sequence_len_lstm ,model_lstm  = None,None,None
def lstm_predict(text):
    global tokenizer_lstm,max_sequence_len_lstm ,model_lstm 
    if tokenizer_lstm is None:
        tokenizer_lstm,max_sequence_len_lstm ,model_lstm  = Load_all(data_path)
    next_words = 1
    for _ in range(next_words):
        token_list = tokenizer_lstm.texts_to_sequences([text])[0]
        token_list = pad_sequences([token_list], maxlen= max_sequence_len_lstm -1, padding='pre')
        predicted = model_lstm.predict(token_list, verbose=0)
        output_word = ""
        for word, index in tokenizer_lstm.word_index.items():
            if index == predicted.argmax():
                output_word = word
                break
        return output_word
tokenizer_gpt = None
model_gpt = None   
def gpt_predict(text):
    global tokenizer_gpt,model_gpt
    if tokenizer_gpt is None:
        tokenizer_gpt = GPT2Tokenizer.from_pretrained("distilgpt2")
        model_gpt = TFGPT2LMHeadModel.from_pretrained("distilgpt2")    
        model_gpt.load_weights("Models/Transformers/finalmodel")    
    input_ids = tokenizer_gpt.encode(text,return_tensors = 'tf')
    greedy_output = model_gpt.generate(input_ids,
                               max_length = len(text) + 50,
                               num_beams = 5,
                               early_stopping = True,
                               no_repeat_ngram_size = 5,
                               )
    out_text = tokenizer_gpt.decode(greedy_output[0],skip_special_tokens = True).split(' ')
    inp_text = text.split(' ')
    
    out_text = out_text[len(inp_text):][0]

    return out_text

# Create flask app
flask_app = Flask(__name__, template_folder='static')
model = pickle.load(open("Models/word2vec/model.pkl", "rb"))

@flask_app.route("/")
def Home():
    return render_template("index.html")



@flask_app.route("/predict", methods = ["POST"])
def predict():

    #text = b'request.form.values().decode()
    text = [str(x) for x in request.form.values()][0]
    
    prediction = model.wv.most_similar(positive=gensim.utils.simple_preprocess(text), topn=1)[0][0]
    prediction2 = lstm_predict(text)
    prediction3 = gpt_predict(text)
    return render_template("index.html", 
                           prediction_text = "Word2vec prediction is: {}".format(prediction), 
                           prediction_text2 = "LSTM prediction is: {}".format(prediction2),
                           prediction_text3 = "GPT2 prediction is: {}".format(prediction3))
    #return render_template("index.html", prediction_text = text)


if __name__ == "__main__":
    flask_app.run(debug=True)