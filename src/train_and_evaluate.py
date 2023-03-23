import os 
import pandas as pd 
import argparse
import joblib
from logger import logging 
from get_data import read_params
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
from data_transformation import encoder_function
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from data_transformation import encode_target
from sklearn.metrics import r2_score
import json


def metrics_eval(actual,predicted):
    score = accuracy_score(actual,predicted)
    return score

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
        
        # print("train:",train.shape)
        test = pd.read_csv(test_data_path,sep=",")
        # print("test:",test.shape)
        # print(train)
        # print(test)
    

        x_train = train.drop(target,axis=1)
        x_test  = test.drop(target,axis=1)
        y_train = train[target] 
        # print(y_train)
        y_test  = test[target]
        # print("Y_TRAIN:",y_train)
        # print("Y_TEST:",y_test)

        y_train_new,y_test_new = encode_target(y_train,y_test)

        print("y_train_new",y_train_new)
        print("y_test_new",y_test_new)


        for_training,for_testing= encoder_function(x_train,x_test)
        logging.info("Training and Testing data is transformed")
        # print("for_training:",for_training.shape)
        # print("for_testing: ",for_testing.shape)
        # print(for_training)


    #     rf = RandomForestClassifier(
    #     max_depth    = max_depth,
    #     max_leaf_nodes = max_leaf_nodes
    # )
    #     rf.fit(for_training,y_train)
        
        dtree = DecisionTreeClassifier(
        max_depth    = max_depth,
        max_leaf_nodes = max_leaf_nodes
        )
        dtree.fit(for_training,y_train_new)
        logging.info("Model training completed")
        y_pred = dtree.predict(for_testing)
        print("Prediction:",y_pred)
        print("prediction done")
        
        acc = metrics_eval(y_test_new,y_pred)
        print("Acc:",acc)


        scores_file = config["reports"]["scores"]
        params_file = config["reports"]["params"]

        with open(scores_file,"w") as f:
            scores={
                "accuracy_score":acc
            }
            json.dump(scores,f,indent=4)


        with open(params_file,"w") as f:
            params={
                "max_depth":max_depth,
                "max_leaf_nodes":max_leaf_nodes
            }
            json.dump(params,f,indent=4)
        os.makedirs(model_dir, exist_ok=True)
        
        model_path = os.path.join(model_dir, "model.joblib")
        joblib.dump(dtree, model_path)
        logging.info("Model has dumped")

    except Exception as e:
        logging.ERROR(e)




if __name__ == "__main__":
    args = argparse.ArgumentParser()
    args.add_argument("--config",default='params.yaml')
    parsed_args = args.parse_args()
    model_training_and_evaluation(config_path=parsed_args.config)


