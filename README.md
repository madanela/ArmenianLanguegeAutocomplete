# ArmenianLanguegeAutocomplete

Here are represented Three types of Armenian Language Autocomplete models. Those are Word2Vec,2 Bidirectional LSTM, Bert (with translate) and GPT-2(trained on Armenian).

Accuracy of 1st lstm basic model is above 90% because of overfitting then we tried the same model in much bigger dataset
and the model does not learn on it because of lemitization basics and accuracy riches at most 4% in predicting next word.
Currently, our best model is GPT-2 trained 10 epochs on wiki_data_3.txt which is included in Data/Scraped folder.

GPT-2 Distill pretrained model and Large LSTM are not included in this repository, because of size limit. 
So both of them are availible in Drive. All three files inside final folder whould be located in Models/Transformers.
large_LSTM should be located in Trained Folder.

All packages used are inside `requirements.txt`. In order to install, write `pip install to-requirements.txt`.

Both small and large LSTM models are located in Models/LSTM_Models/ folder and there are 2 models, train and model for each of them.
If you want to train on your own dataset you need to change the input folder inside train and then run python file, for example `python large_train.py`.
If you want to use pretrained model, you have to firsly, add the trained model, if it is not there from drive, and then, by changing the seed_text and next_words inside `large_model.py` for example, you are going to get continuation of `seed_text` with the amount `next_words`  number of words.

There is also, tokenizer example included in the LSTM_Models folder, which we tested on subword lstm models.






