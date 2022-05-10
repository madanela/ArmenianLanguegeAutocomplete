"""
load trained model
"""

import configparser
import numpy as np
import pickle
import tensorflow as tf

def tok_load(data_path):
    with open(data_path + 'tokenizer_onwiki2.pickle', 'rb') as handle:
        tokenizer = pickle.load(handle)
    return tokenizer
def config_load(data_path):
    def read_config():
        configuration = {}
        with open(data_path + 'config.ini', 'r') as config_file:
            for line in config_file:
                print(line)
                fields = line.split('=')
                if len(fields) == 2:
                    configuration[fields[0].strip()] = int(fields[1])
        return configuration
    configOutput =read_config()

    return configOutput['max_sequence_len']    
def model_load(data_path):
    return tf.keras.models.load_model(data_path + 'model_onwiki2')
        
def Load_all(data_path):
    return tok_load(data_path),config_load(data_path),model_load(data_path)
