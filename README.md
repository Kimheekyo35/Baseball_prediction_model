# ⚾ KBO 야구선수 연봉 예측 및 데이터 분석 프로젝트
## 📖 프로젝트 소개
- 본 프로젝트는 KBO(한국 프로야구) 선수들의 데이터를 기반으로 투수와 타자의 연봉을 예측하고, 선수들의 출신 고교 등 다양한 요소를 시각적으로 분석하는 Streamlit 웹 애플리케이션입니다.

- 머신러닝 모델을 통해 선수의 성적(Performance) 데이터를 기반으로 다음 시즌의 연봉 구간을 예측하고, EDA(탐색적 데이터 분석) 페이지에서는 출신 고교별 선수들의 평균 연봉을 지도에 시각화하여 흥미로운 인사이트를 제공합니다.

## ✨ 주요 기능
### 🧤 투수 연봉 예측: 평균자책점, 승리, 이닝, WAR 등 투수의 주요 스탯을 입력받아 4개의 연봉 구간(하위 25%, 25-50%, 50-75%, 상위 75% 이상)을 예측합니다.

### 🏏 타자 연봉 예측: 안타, 홈런, 타점, WAR 등 타자의 주요 스탯을 입력받아 4개의 연봉 구간을 예측합니다.

### 📈 출신 고교별 연봉 분석: 야구 명문고와 비명문고 출신 선수들의 평균 연봉 데이터를 계산하고, Folium 라이브러리를 활용하여 대한민국 지도 위에 시각적으로 표현합니다.

### 📊 예측 결과 시각화: 연봉 예측 결과와 함께 전체 선수들의 연봉 구간 분포를 시각화하여 보여줍니다.

## 🛠️ 기술 스택
- 언어: Python

- 머신러닝/데이터 분석: Scikit-learn, XGBoost, Pandas, NumPy

- 웹 프레임워크/시각화: Streamlit, Matplotlib, Seaborn, Folium

- 모델 저장: Pickle

📂 프로젝트 구조
```
.
├── data
│   ├── pitcher_data.csv
│   ├── hitter_final2.csv
│   ├── Salary_WAR_data.csv
│   └── total_career_data.csv
├── modeling
│   ├── pitcher_model.pkl
│   └── hitter_model.pkl
├── pages
│   ├── 📈_EDA.py
│   ├── 🏏_hitter_modeling.py
│   └── 🧤_pitcher_modeling.py
├── pitcher_modeling_python.py
└── MAIN.py (Streamlit 실행을 위한 메인 페이지, 예시)

```
