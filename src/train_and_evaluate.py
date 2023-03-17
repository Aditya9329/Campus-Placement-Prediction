import os 
import pandas as pd 
import argparse
import joblib
from logger import logging 
from get_data import read_params
from sklearn.tree import DecisionTreeClassifier
from data_transformation import encoder_function
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import r2_score


def model_training_and_evaluation(config_path):
    try:
        config  = read_params(config_path)
        train_data_path = config["split_data"]["train_path"]
        test_data_path  = config["split_data"]["test_path"]
        model_dir       = config["model_dir"]
        max_depth       = config["estimators"]["DecisionTreeClassifier"]["params"]["max_depth"]
        max_leaf_nodes  = config["estimators"]["DecisionTreeClassifier"]["params"]["max_leaf_nodes"]
        target = [config["base"]["target_col"]]

        train = pd.read_csv(train_data_path,sep=",")
        logging
        print("train:",train.shape)
        test = pd.read_csv(test_data_path,sep=",")
        print("test:",test.shape)
        # print(train)
        # print(test)
    

        x_train = train.drop(target,axis=1)
        x_test  = test.drop(target,axis=1)
        y_train = train[target] 
        y_test  = test[target]

        for_training,for_testing= encoder_function(x_train,x_test)
        print("for_training:",for_training.shape)
        print("for_testing: ",for_testing.shape)
        print(for_training)


    #     rf = RandomForestClassifier(
    #     max_depth    = max_depth,
    #     max_leaf_nodes = max_leaf_nodes
    # )
    #     rf.fit(for_training,y_train)
        
        dtree = DecisionTreeClassifier(
        max_depth    = max_depth,
        max_leaf_nodes = max_leaf_nodes
        )
        dtree.fit(for_training,y_train)
        os.makedirs(model_dir, exist_ok=True)
        
        model_path = os.path.join(model_dir, "model.joblib")
        joblib.dump(dtree, model_path)

    except Exception as e:
        logging.ERROR(e)




if __name__ == "__main__":
    args = argparse.ArgumentParser()
    args.add_argument("--config",default='params.yaml')
    parsed_args = args.parse_args()
    model_training_and_evaluation(config_path=parsed_args.config)


