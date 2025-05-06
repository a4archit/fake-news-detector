import pickle
import os 

from tensorflow import keras
from keras.preprocessing.sequence import pad_sequences
from typing import Tuple
from pandas import Series 



class FakeNewsDetector():
    """ This class manage all the working regards model. """

    # setting paths
    MODEL_PATH = os.path.join(os.getcwd(), "model_9226.h5")
    TOKENIZER_PATH = os.path.join(os.getcwd(), "tokenizer.pkl")



    def __init__(self):
        # fetching neccessary files
        self.model = keras.models.load_model(self.MODEL_PATH)
        self.tokenizer = pickle.load(open(self.TOKENIZER_PATH, 'rb'))


    
    def predict(self, text: str) -> Tuple[int, str]:
        """ This function will perform actual prediction on given text """

        if text == "":
            raise ValueError("Enter a proper news headline !!!")
        
        # tokenizing
        tokens = self.tokenizer.texts_to_sequences(Series(text))

        # padding 
        padded_tokens = pad_sequences(tokens, maxlen=30, padding='post', truncating='post' )

        # prediction
        prediction = self.model.predict(padded_tokens, verbose=False)

        confidense = prediction[0][0]

        label = 'fake' if confidense < 0.5 else 'real' if confidense > 0.65 else 'not sure'

        return (label, confidense)
    



if __name__ == "__main__":

    model = FakeNewsDetector()
    q = "An ant drive a car with seat belt"

    print(model.predict(q))
        


