import os
import sys
import pandas as pd
import numpy as np
import pickle

from src.exception import CustomException
from src.logger import logging

def save_object(filepath,obj):
    try:
        dir_path = os.path.dirname(filepath)

        os.makedirs(dir_path,exist_ok=True)
        
        with open(filepath,"wb") as file_obj:
            pickle.dump(obj,file_obj)
            
    except Exception as e:
        raise CustomException(e,sys)
    
def txt_to_pkl():
    # Open the text file for reading
    with open('artifacts/preprocessor.txt', 'r') as file:
        data = file.read()

    # Open the pickle file for writing
    with open('artifacts/preprocessor.pickle', 'wb') as file:
        # Serialize the data and write it to the pickle file
        pickle.dump(data, file)
        
if __name__=="__main__":
    txt_to_pkl()