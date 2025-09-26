import xgboost as xgb
from xgboost import XGBClassifier
import os
import joblib

class xgb_c_model():
    def __init__(self, input, target):
        self.input = input
        self.target = target

    def data_transform(self):
        from sklearn.model_selection import train_test_split
        import xgboost as xgb
        input = self.input
        target = self.target
        train_input, test_input, train_target, test_target = train_test_split(input, target, test_size = 0.2, random_state = 42)
        dtrain = xgb.DMatrix(data = train_input, label = train_target)
        dtest = xgb.DMatrix(data = test_input, label = test_target)
        return dtrain, dtest
    
    def get_test(self):
        from sklearn.model_selection import train_test_split
        import xgboost as xgb
        input = self.input
        target = self.target
        train_input, test_input, train_target, test_target = train_test_split(input, target, test_size = 0.2, random_state = 42)
        dtrain = xgb.DMatrix(train_input, train_target)
        dtest = xgb.DMatrix(test_input, test_target)
        return dtest
    
    def get_target(self):
        from sklearn.model_selection import train_test_split
        input = self.input
        target = self.target
        train_input, test_input, train_target, test_target = train_test_split(input, target, test_size = 0.2, random_state = 42)
        return test_target

    
    def train(self, parameter, num, early):
        import xgboost as xgb
        dtrain, dtest = self.data_transform()
        model = xgb.train(params = parameter, dtrain = dtrain, num_boost_round = num, early_stopping_rounds = early, evals = [(dtrain, 'train'), (dtest, 'eval')])
        return model
    
    def model_test(self, model, test_dmatrix):
        import xgboost as xgb
        preds = model.predict(test_dmatrix)
        return preds
    
    def get_eval(self, test, preds):
        from sklearn.metrics import confusion_matrix, accuracy_score, precision_score, recall_score, f1_score, roc_auc_score
        confusion = confusion_matrix(test, preds)
        accuracy = accuracy_score(test, preds)
        precision = precision_score(test, preds, average = 'weighted')
        recall = recall_score(test, preds, average = 'weighted')
        F1 = f1_score(test, preds, average = 'weighted')
        print('오차행렬 : \n', confusion)
        print('accuracy : ', accuracy)
        print('정밀도 : ', precision)
        print('재현율 : ', recall)
        print('F1 : ', F1)


import pandas as pd
import pickle as pkl

data = pd.read_csv('./data/pitcher_data.csv')
df_input = data[['ERA', 'QS_G', 'SO', 'WAR_x', 'W', 'IP', 'K_BB', 'exp_QS','SO_G', 'QS', 'NP', 'RA_9', '연차', 'TBF', '현재연봉', 'WHIP', 'K-BB', 'NP/IP']]
df_target = data['salary_cluster']

parameter = {'max_depth' : 3, 'eta' : 0.006, 'objective' : 'multi:softmax', 'eval_metrics' : 'merror', 'num_class' : 4}

from pitcher_modeling_python import xgb_c_model
x_model = xgb_c_model(df_input, df_target)
x_model_fin = x_model.train(parameter, 400, 100)

dtest = x_model.get_test()
preds = x_model.model_test(x_model_fin, dtest)

target = x_model.get_target()
target = target.values.tolist()


x_model.get_eval(target, preds)

name = 'pitcher_salary_predict.model'
model_file=open("modeling/pitcher_model.pkl","wb")
joblib.dump(x_model_fin, model_file)
model_file.close()