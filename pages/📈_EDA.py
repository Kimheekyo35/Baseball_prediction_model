import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import folium
import streamlit as st

data_csv='./data/Salary_WAR_data.csv'
career_csv= './data/total_career_data.csv'
st.set_page_config(layout='wide')
col1,col2=st.columns([1.0,1.0])
col1,col2=st.columns(2)
df_salary=pd.read_csv(data_csv)
df_salary=df_salary[df_salary['연도']==2023]
df_career=pd.read_csv(career_csv)
salary_career=pd.merge(df_salary,df_career,on='선수',how='inner')
salary_career=salary_career.dropna(axis=0).reset_index(drop=True)
salary_career['연봉(만원)']=salary_career['연봉(만원)'].str.replace(',','')
salary_career['연봉(만원)']=salary_career['연봉(만원)'].astype(int)

df_career=df_career.dropna(axis=0)
highsc_career=df_career[df_career['출신학교'].str.contains('고')].reset_index(drop=True)

high_gaesung=highsc_career[highsc_career['출신학교'].str.contains('개성고')]
high_kyungnam=highsc_career[highsc_career['출신학교'].str.contains('경남고')]
high_sanggo=highsc_career[highsc_career['출신학교'].str.contains('군산상고')]
highsc_kyungju=highsc_career[highsc_career['출신학교'].str.contains('경주고')]
highsc_kyungdong=highsc_career[highsc_career['출신학교'].str.contains('경동고')]
highsc_duksu=highsc_career[highsc_career['출신학교'].str.contains('덕수고')]
highsc_sangwon=highsc_career[highsc_career['출신학교'].str.contains('상원고')]
highsc_laon=highsc_career[highsc_career['출신학교'].str.contains('라온고')]
highsc_masan=highsc_career[highsc_career['출신학교'].str.contains('마산고')]
highsc_yongma=highsc_career[highsc_career['출신학교'].str.contains('용마고')]
highsc_baemyung=highsc_career[highsc_career['출신학교'].str.contains('배명고')]
highsc_busangong=highsc_career[highsc_career['출신학교'].str.contains('부산공고')]
highsc_busaninfo=highsc_career[highsc_career['출신학교'].str.contains('부산정보고')]
highsc_bucheon=highsc_career[highsc_career['출신학교'].str.contains('부천고')]
highsc_seolak=highsc_career[highsc_career['출신학교'].str.contains('설악고')]
highsc_sungnam=highsc_career[highsc_career['출신학교'].str.contains('성남고')]
highsc_sekwang=highsc_career[highsc_career['출신학교'].str.contains('세광고')]
highsc_sorae=highsc_career[highsc_career['출신학교'].str.contains('소래고')]
highsc_hyochun=highsc_career[highsc_career['출신학교'].str.contains('효천고')]
highsc_sinil=highsc_career[highsc_career['출신학교'].str.contains('신일고')]
highsc_yatop=highsc_career[highsc_career['출신학교'].str.contains('야탑고')]
highsc_youngsun=highsc_career[highsc_career['출신학교'].str.contains('영선고')]
highsc_inchang=highsc_career[highsc_career['출신학교'].str.contains('인창고')]
highsc_jeonju=highsc_career[highsc_career['출신학교'].str.contains('전주고')]
highsc_cheongwon=highsc_career[highsc_career['출신학교'].str.contains('청원고')]
highsc_cheongju=highsc_career[highsc_career['출신학교'].str.contains('청주고')]
highsc_chungam=highsc_career[highsc_career['출신학교'].str.contains('충암고')]
highsc_chunghun=highsc_career[highsc_career['출신학교'].str.contains('충훈고')]
highsc_hwasoon=highsc_career[highsc_career['출신학교'].str.contains('화순고')]

high_notfamous=pd.concat([highsc_chunghun,highsc_hwasoon,highsc_cheongju,highsc_cheongwon,highsc_jeonju,highsc_inchang,highsc_youngsun,highsc_yatop,highsc_sinil
                          ,highsc_hyochun,highsc_sorae,highsc_sekwang,highsc_sungnam,highsc_seolak,highsc_bucheon,highsc_busaninfo,highsc_busangong,highsc_baemyung,highsc_yongma,highsc_masan,highsc_laon
                          ,highsc_sangwon,highsc_kyungdong,highsc_kyungju,high_sanggo,high_kyungnam,high_gaesung],axis=0)


lists=['개성고', '경남고', '경동고', '경주고', '군산상고', '라온고', '마산고', '부산정보고', '상원고', '설악고',
       '성남고', '세광고', '소래고', '신일고', '야탑고', '영선고', '용마고', '인창고', '전주고',
       '청원고', '청주고', '충훈고', '화순고', '효천고']

result=pd.DataFrame(
      columns=high_notfamous.columns
  )
for list in lists:
  i=high_notfamous[high_notfamous['출신학교'].str.contains(list)]
  i.loc[:,'출신학교']=[list]*len(i)
  i.drop_duplicates()
  result=pd.concat([result,i],axis=0)

result=result.reset_index(drop=True)
high_notfamous=result
high_notfamous=pd.merge(salary_career,high_notfamous,on='선수',how='inner')
high_notfamous=high_notfamous.drop_duplicates()
high_notfamous=high_notfamous.drop(['출신학교_x'],axis=1)
high_notfamous=high_notfamous.rename(columns={'출신학교_y':'출신학교'}).reset_index(drop=True)
high_notfamous_mean_salary=high_notfamous.groupby('출신학교')['연봉(만원)'].mean()
high_notfamous_mean_salary=pd.DataFrame(high_notfamous_mean_salary)
high_notfamous_mean_salary=high_notfamous_mean_salary.astype(int)


data={
    '위도':[35.1697, 35.1206, 37.5862, 35.8438,35.9746, 37.0694, 35.2005, 35.1775, 35.8225, 38.1856, 37.5051, 36.6031, 37.4373,  37.6285 , 37.4037, 37.5160, 35.2122,37.5654,35.8254,37.6666,36.6360, 37.4107, 35.0543, 34.9037],
    '경도':[129.0302, 129.0203, 127.0146, 129.2261, 126.6991, 127.0673, 128.5616,129.0645 , 128.5383, 128.5735,126.9261,127.4531,126.794,127.0277, 127.1534, 126.7444,128.582, 126.9636, 127.1518, 127.0631, 127.4553, 126.8926, 126.9841, 127.4854]
}
not_famous_location=pd.DataFrame(data)
not_famous_location.index=high_notfamous_mean_salary.index
high_notfamous_mean_salary=pd.merge(high_notfamous_mean_salary,not_famous_location,on='출신학교',how='inner')

with col1:
  st.write('비명문고 연봉과 고등학교의 위도, 경도')
  high_notfamous_mean_salary
high_kb=salary_career[salary_career['출신학교'].str.contains('경북고')]
high_kb.loc[:,'출신학교']=['경북고']*len(high_kb)
high_kb.drop_duplicates()

high_busan=salary_career[salary_career['출신학교'].str.contains('부산고')]
high_busan.loc[:,'출신학교']=['부산고']*len(high_busan)
high_busan.drop_duplicates()

high_gj=salary_career[salary_career['출신학교'].str.contains('광주제일고')]
high_gj.loc[:,'출신학교']=['광주제일고']*len(high_gj)
high_gj.drop_duplicates()

high_seoul=salary_career[salary_career['출신학교'].str.contains('서울고')]
high_seoul.loc[:,'출신학교']=['서울고']*len(high_seoul)
high_seoul.drop_duplicates()

high_buk=salary_career[salary_career['출신학교'].str.contains('북일고')]
high_buk.loc[:,'출신학교']=['북일고']*len(high_buk)
high_buk.drop_duplicates()

high_daegu=salary_career[salary_career['출신학교'].str.contains('대구고')]
high_daegu.loc[:,'출신학교']=['대구고']*len(high_daegu)
high_daegu.drop_duplicates()

high_internet=salary_career[salary_career['출신학교'].str.contains('선린')]
high_internet.loc[:,'출신학교']=['선린고']*len(high_internet)
high_internet.drop_duplicates()

high_sangwon=salary_career[salary_career['출신학교'].str.contains('상원고')]
high_sangwon.loc[:,'출신학교']=['상원고']*len(high_sangwon)
high_sangwon.drop_duplicates()

high_bukyung=salary_career[salary_career['출신학교'].str.contains('부경고')]
high_bukyung.loc[:,'출신학교']=['부경고']*len(high_bukyung)
high_bukyung.drop_duplicates()

high_dongsung=salary_career[salary_career['출신학교'].str.contains('동성고')]
high_dongsung.loc[:,'출신학교']=['동성고']*len(high_dongsung)
high_dongsung.drop_duplicates()

high_duksu=salary_career[salary_career['출신학교'].str.contains('덕수고')]
high_duksu.loc[:,'출신학교']=['덕수고']*len(high_duksu)
high_duksu.drop_duplicates()

high_hwi=salary_career[salary_career['출신학교'].str.contains('휘문고')]
high_hwi.loc[:,'출신학교']=['휘문고']*len(high_hwi)
high_hwi.drop_duplicates()

high_jinheung=salary_career[salary_career['출신학교'].str.contains('진흥고')]
high_jinheung.loc[:,'출신학교']=['진흥고']*len(high_jinheung)
high_jinheung.drop_duplicates()

high_gongju=salary_career[salary_career['출신학교'].str.contains('공주고')]
high_gongju.loc[:,'출신학교']=['공주고']*len(high_gongju)
high_gongju.drop_duplicates()

high_chungam=salary_career[salary_career['출신학교'].str.contains('충암고')]
high_chungam.loc[:,'출신학교']=['충암고']*len(high_chungam)
high_chungam.drop_duplicates()

high_daejun=salary_career[salary_career['출신학교'].str.contains('대전고')]
high_daejun.loc[:,'출신학교']=['대전고']*len(high_daejun)
high_daejun.drop_duplicates()

high_baejae=salary_career[salary_career['출신학교'].str.contains('배재고')]
high_baejae.loc[:,'출신학교']=['배재고']*len(high_baejae)
high_baejae.drop_duplicates()

high_inchun=salary_career[salary_career['출신학교'].str.contains('인천고')]
high_inchun.loc[:,'출신학교']=['인천고']*len(high_inchun)
high_inchun.drop_duplicates()

high_jangchung=salary_career[salary_career['출신학교'].str.contains('장충고')]
high_jangchung.loc[:,'출신학교']=['장충고']*len(high_jangchung)
high_jangchung.drop_duplicates()


high_dongsan=salary_career[salary_career['출신학교'].str.contains('동산고')]
high_dongsan.loc[:,'출신학교']=['동산고']*len(high_dongsan)
high_dongsan.drop_duplicates()

high_gangreung=salary_career[salary_career['출신학교'].str.contains('강릉고')]
high_gangreung.loc[:,'출신학교']=['강릉고']*len(high_gangreung)
high_gangreung.drop_duplicates()

high_ansan=salary_career[salary_career['출신학교'].str.contains('안산공고')]
high_ansan.loc[:,'출신학교']=['안산공고']*len(high_ansan)
high_ansan.drop_duplicates()

result_career=pd.concat([high_kb,high_busan,high_gj,high_seoul,high_buk,high_daegu,high_internet,high_sangwon,high_bukyung,high_dongsung,high_duksu,high_hwi,high_jinheung,high_gongju,high_daejun,high_baejae,high_inchun,high_jangchung,high_dongsan,high_gangreung,high_ansan,high_chungam],axis=0)
salary_mean_career=result_career.groupby(['출신학교'])['연봉(만원)'].mean()


salary_mean_career=pd.DataFrame(
    data=salary_mean_career,
    index=salary_mean_career.index,
    columns=['연봉(만원)']
)
salary_mean_career['연봉(만원)']= salary_mean_career['연봉(만원)'].astype(int)

data={
    '위도':[37.7885,35.8445,36.4475,35.15369 ,35.8486,36.3222122 ,37.5553429 ,37.4736,37.5851,37.5558,35.1149,35.1214,36.8319, 35.8225,37.4840,37.5427,37.3361442,37.4542,37.5526, 35.1959575 ,37.5848086 ,37.5050],
    '경도':[128.91,128.64,127.12,126.906,128.588,127.424,127.042,126.64,127.00,127.15, 129.01,129.04,127.15,128.53, 127.00,126.96,126.860,126.690,127.00,126.842,126.921,127.06]
}
location=pd.DataFrame(data)
location.index=salary_mean_career.index
salary_mean_career=pd.concat([salary_mean_career,location],axis=1)
with col2:

  st.write('명문고의 연봉과 고등학교의 위도, 경도')
  salary_mean_career

map = folium.Map(location=[36.34, 127.77],zoom_start=7.8)
def salary_cal(i):
  return salary_mean_career.loc[salary_mean_career.index[i],['연봉(만원)']]

def salary_cal_notfamous(j):
  return high_notfamous_mean_salary.loc[high_notfamous_mean_salary.index[j],['연봉(만원)']]
for i in range(len(salary_mean_career)):
  folium.Circle(
      location=[salary_mean_career.loc[salary_mean_career.index[i], '위도'], salary_mean_career.loc[salary_mean_career.index[i], '경도']],
      color='cornflowerblue',
      stroke=False,
      fill=True,
      fill_color='cadetblue',
      fill_opacity=0.6,
      radius=salary_cal(i).iloc[0]/5,
      weight=3,
      tooltip=f'{salary_mean_career.index[i]}',
      popup=salary_cal(i).iloc[0]
).add_to(map)


for j in range(len(high_notfamous_mean_salary)):
  folium.Circle(
      location=[high_notfamous_mean_salary.loc[high_notfamous_mean_salary.index[j], '위도'], high_notfamous_mean_salary.loc[high_notfamous_mean_salary.index[j], '경도']],
      color='red',
      stroke=False,
      fill=True,
      fill_color='red',
      fill_opacity=0.6,
      radius=salary_cal_notfamous(j).iloc[0]/5,
      weight=3,
      tooltip=f'{high_notfamous_mean_salary.index[j]}',
      popup=salary_cal_notfamous(j).iloc[0]
  ).add_to(map)


st.header('명문고와 비명문고 연봉 비교')
st.components.v1.html(folium.Figure().add_child(map).render(), height=500)


