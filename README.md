# ArmenianLanguegeAutocomplete

Here are represented Three types of ALA (Armenian Language Autocomplete) models. Those are Word2Vec,2 Bidirectional LSTM, Bert (with translate) and GPT-2(trained on Armenian).

Accuracy of 1st lstm basic model is above 90% because of overfitting then we tried the same model in much bigger dataset
and the model does not learn on it because of lemitization basics and accuracy riches at most 4% in predicting next word.
Currently, our best model is GPT-2 trained 10 epochs on wiki_data_3.txt which is included in Data/Scraped folder.

GPT-2 Distill pretrained model and Large LSTM are not included in this repository, because of size limit. 

So both of them are availible in Drive. All three files inside final folder whould be located in Models/Transformers.
large_LSTM should be located in Trained Folder.

All packages used are inside `requirements.txt`. In order to install, run `pip install to-requirements.txt` command.

Both small and large LSTM models are located in Models/LSTM_Models/ folder and there are 2 models, train and model for each of them.
If you want to train on your own dataset you need to change the input folder inside train and then run python file, for example `python large_train.py`.
If you want to use pretrained model, you have to firsly, add the trained model, if it is not there from drive, and then, by changing the seed_text and next_words inside `large_model.py` for example, you are going to get continuation of `seed_text` with the amount `next_words`  number of words.

Another model, is Bert Translation model which is using Bert LM and translate to for ALA. Translate_notebook is located in Models/Translate_Models which runs with input string. Also there is streamlit version of it which we used from open-source and by running `streamlit run next_word_armenian.py` it will work in iteractive envirionment.

And last part, is transformer models. In Models/Transformers there are 2 models gpt2-train.ipynb and gpt-2-model.ipynb. First one is model with training process, and second one is loading trained model and use only for prediction. In order to run the gpt-2-model.ipynb, you should download final folder from drive, and paste all 3 files of it inside Models/Transformer folder.

Also there is example of ArmBerta included in Models/transformers, for testing.

Besides all of it, there is Scraping_Preprocessing folder inside Models, which includes preprocessing and cleaning tools developed by us, in order to make our dataset more usable. All preprocessing has been done with data inside Data/Scraped, so you are not going to need any of those tools.

Project authors: Nune Meliksetyan, Ani Guloyan, Alen Adamyan. 
Instructor: Michael Poghosyan.

# Video



https://user-images.githubusercontent.com/57109551/168443210-ffe6bf5b-2520-42cd-9559-fd0b88881287.mp4


