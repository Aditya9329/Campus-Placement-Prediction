#read the data from data source 
#and save it in the data/raw_data for next process
import os 
import argparse
import pandas as pd 
from logger import logging
from get_data import read_params,get_data

def load_and_save(config_path):
    try:
        config = read_params(config_path)
        logging.info("get the configuration path")
        df = get_data(config_path)
        # print(df)
        logging.info("pandas dataframe get created")
        raw_data_path = config["load_data"]["raw_dataset_csv"]
        logging.info("read the raw_data_path successfully")
        print(raw_data_path)
        df.to_csv(raw_data_path,sep=",",index=False)
        logging.info("data copied to the raw data folder for further processes") 

    except Exception as e:
        print("Error:",e)




if __name__ == "__main__":
    args = argparse.ArgumentParser()
    args.add_argument("--config",default="params.yaml")
    parsed_args = args.parse_args()
    load_and_save(config_path=parsed_args.config)

