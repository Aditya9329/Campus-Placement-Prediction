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
from logger import logging
from sklearn.model_selection import train_test_split


def split_data(config_path):
    try:
        config = read_params(config_path)
        logging.info("read the configuration path")
        raw_data_path = config["load_data"]["raw_dataset_csv"]
        logging.info("read the raw_data_path successfully")
        training_data_path = config["split_data"]["train_path"]
        logging.info("read the training data path successfully")
        testing_data_path  = config["split_data"]["test_path"]
        logging.info("read the testing data path successfully")
        test_size     = config["split_data"]["test_size"]


        df = pd.read_csv(raw_data_path,sep=",")
        logging.info("data reading done from raw folder")
        df.drop(columns=['Unnamed: 0','sl_no','salary'],inplace=True)
        logging.info("dropping unecessary columns")

        train,test = train_test_split(df,
                                      test_size = test_size)

        # print(train)
        # print(test)
        logging.info("train data and test data get separated")

        train.to_csv(training_data_path,sep=",",index=False)
        logging.info("training data get stored into the processed folder")
        test.to_csv(testing_data_path,sep=",",index=False)
        logging.info("testing data get stored into the processed folder")
    except Exception as e:
        print("Error:",e)



if __name__ == "__main__":
    args = argparse.ArgumentParser()
    args.add_argument("--config",default='params.yaml')
    parsed_args = args.parse_args()
    split_data(config_path=parsed_args.config)

