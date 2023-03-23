import pickle
from logger import logging
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
from sklearn.preprocessing import LabelEncoder



def encoder_function(x_train,x_test):
    transformer = ColumnTransformer(transformers=[
    ('tnf1',OneHotEncoder(sparse=False,drop='first'),['ssc_b','hsc_b','hsc_s','degree_t','workex','specialisation'])
    ],remainder='passthrough')

    logging.info("data transformation object has created")




    
    x_train_transformed = transformer.fit_transform(x_train)
    logging.info("fit and transform the x_train data and stored into the variable called x_train_transformed")

    # pickle.dump(x_train_transformed,open('ColumnTransformer.sav','wb'))
    x_test_transformed  = transformer.transform(x_test)
    logging.info("transformed the x_test data and stored into the x_test_transformed variable")
    # print(x_train_transformed)
    # print(x_test_transformed)
    return x_train_transformed, x_test_transformed





def encode_target(y_train,y_test):
    le = LabelEncoder()
    le.fit(y_train)
    y_train_transformed = le.transform(y_train)
    y_test_transformed  = le.transform(y_test)
    return y_train_transformed,y_test_transformed