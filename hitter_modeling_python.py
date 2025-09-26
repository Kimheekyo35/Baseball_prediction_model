import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import warnings
import streamlit as st
import os
import joblib
import matplotlib.font_manager as fm

#font 오류 수정
# font_list = fm.findSystemFonts()
# font_name = None
# for font in font_list:
#     if 'AppleGothic' in font:
#         font_name = fm.FontProperties(fname=font).get_name()
# plt.rc('font', family=font_name)


warnings.filterwarnings('ignore')
hitter_data = './data/htter_salary_stats_debut.csv'
parkfactor = './data/pitcher_meanERA_parkfactor.csv'

df_hitter=pd.read_csv(hitter_data)




from sklearn.model_selection import train_test_split

data = df_hitter[['TB', 'R', 'H', '2B', 'HR',  'RBI', 'SF', 'BB', 'IBB', 'HBP', 'SLG', 'MH', 'WAR','연차','연봉(만원)']]
target = df_hitter['연봉구간']

X_train, X_test, y_train, y_test = train_test_split(
    data,
    target,
    test_size=0.3,
    random_state=0
)
from sklearn.ensemble import RandomForestClassifier

model = RandomForestClassifier(max_depth = 6, min_samples_leaf = 8, min_samples_split = 20, n_estimators= 100)

model.fit(X_train,y_train)

from sklearn.metrics import accuracy_score

# test 데이터 예측
y_pred = model.predict(X_test)

# 정확도 계산
accuracy = accuracy_score(y_test, y_pred)
print(f'Accuracy: {accuracy}'.format(accuracy))

model_file=open("modeling/hitter_model.pkl","wb")
joblib.dump(model, model_file)
model_file.close()