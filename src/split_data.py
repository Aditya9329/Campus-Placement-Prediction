"""
"Aditya Narayan Maurya" 
            READ THE RAW DATA FROM data/raw
                    PROCESS IT
                    SPLIT IT 
                     INTO
            TRAINING AND TESTING AND STORE IT
                    INTO THE
            PROCESSED DATA DIRECTORY i.e. data/processed

"""

import os 
import argparse
import pandas as pd 
from get_data import read_params
from sklearn.model_selection import train_test_split


def split_data(config_path):
    try:
        config = read_params(config_path)
        raw_data_path = config["load_data"]["raw_dataset_csv"]
        training_data_path = config["split_data"]["train_path"]
        testing_data_path  = config["split_data"]["test_path"]
        test_size     = config["split_data"]["test_size"]

        df = pd.read_csv(raw_data_path,sep=",")
        df.drop(columns=['sl_no','salary'],inplace=True)

        train,test = train_test_split(df,
                                      test_size = test_size)

        print(train)
        print(test)
        train.to_csv(training_data_path,sep=",",index=False)
        test.to_csv(testing_data_path,sep=",",index=False)
    except Exception as e:
        print("Error:",e)



if __name__ == "__main__":
    args = argparse.ArgumentParser()
    args.add_argument("--config",default='params.yaml')
    parsed_args = args.parse_args()
    split_data(config_path=parsed_args.config)

