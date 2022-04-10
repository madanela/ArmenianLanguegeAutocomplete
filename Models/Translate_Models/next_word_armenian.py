import os
import streamlit as st
import torch
import string
import pynput
from transformers import BertTokenizer, BertForMaskedLM
from pynput import keyboard
from googletrans import Translator



@st.cache()
def load_model(model_name):
  try:
    if model_name.lower() == "bert":
      bert_tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')
      bert_model = BertForMaskedLM.from_pretrained('bert-base-uncased').eval()
      return bert_tokenizer,bert_model
  except Exception as e:
    pass





#use joblib to fast your function


def decode(tokenizer, pred_idx, top_clean):
  ignore_tokens = string.punctuation + '[PAD]'
  tokens = []
  for w in pred_idx:
    token = ''.join(tokenizer.decode(w).split())
    if token not in ignore_tokens:
      tokens.append(token.replace('##', ''))
  return '\n'.join(tokens[:top_clean])




def encode(tokenizer, text_sentence, add_special_tokens=True):
  text_sentence = text_sentence.replace('<mask>', tokenizer.mask_token)
    # if <mask> is the last token, append a "." so that models dont predict punctuation.
  if tokenizer.mask_token == text_sentence.split()[-1]:
    text_sentence += ' .'

    input_ids = torch.tensor([tokenizer.encode(text_sentence, add_special_tokens=add_special_tokens)])
    mask_idx = torch.where(input_ids == tokenizer.mask_token_id)[1].tolist()[0]
  return input_ids, mask_idx







def get_all_predictions(text_sentence, top_clean=5):
    # ========================= BERT =================================
  input_ids, mask_idx = encode(bert_tokenizer, text_sentence)
  with torch.no_grad():
    predict = bert_model(input_ids)[0]
  bert = decode(bert_tokenizer, predict[0, mask_idx, :].topk(top_k).indices.tolist(), top_clean)
  return {'bert': bert}





def get_prediction_eos(input_text):
  try:
    translator = Translator()
    result = translator.translate(input_text, src='hy', dest='en').text
    result += ' <mask>'

    res = get_all_predictions(result, top_clean=int(top_k))
    
    fin_result = dict()
    
    model_name = list(res.keys())[0]

    for i in res[model_name].split("\n"):

        if model_name in fin_result:
           fin_result[model_name]+='\n'
        else:
           fin_result[model_name]=''

        fin_result[model_name]+=translator.translate(i, src='en', dest='hy').text

    return fin_result
  except Exception as error:
    pass



try:
     
     print("entered 1")
     st.title("Next Word Prediction with Pytroch")
     st.sidebar.text("Next Word Prediction")
     
     top_k = st.sidebar.slider("How many words do you need", 1 , 25, 1) #some times it is possible to have less words
     print(top_k)
     model_name = st.sidebar.selectbox(label='Select Model to Apply',  options=['BERT', 'XLNET'], index=0,  key = "model_name")

     print("entered 2")
     bert_tokenizer, bert_model  = load_model(model_name) 
     input_text = st.text_area("Enter your text here")
     #click outside box of input text to get result
     res = get_prediction_eos(input_text)
     print("entered 3 ",res,input_text)
     answer = []
     print(res['bert'].split("\n"))
     for i in res['bert'].split("\n"):
         answer.append(i)

     answer_as_string = "    ".join(answer)
     st.text_area("Predicted List is Here",answer_as_string,key="predicted_list")



except Exception as e:
  print("SOME PROBLEM OCCURED")