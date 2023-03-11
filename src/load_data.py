#read the data from data source 
#and save it in the data/raw_data for next process
import os 
import argparse
import pandas as pd 
from get_data import read_params,get_data

def load_and_save(config_path):
    # try:
        config = read_params(config_path)
        df = get_data(config_path)
        print(df)
        raw_data_path = config["load_data"]["raw_dataset_csv"]
        print(raw_data_path)
        df.to_csv(raw_data_path,sep=",",index=False) 

    # except Exception as e:
    #     print("Error:",e)




if __name__ == "__main__":
    args = argparse.ArgumentParser()
    args.add_argument("--config",default="params.yaml")
    parsed_args = args.parse_args()
    load_and_save(config_path=parsed_args.config)

