import streamlit as st
import pandas as pd
import pickle
from pathlib import Path

teams = ['Mumbai Indians',
 'Rajasthan Royals',
 'Kolkata Knight Riders',
 'Chennai Super Kings',
 'Sunrisers Hyderabad',
 'Delhi Capitals',
 'Punjab Kings',
 'Lucknow Super Giants',
 'Gujarat Titans',
 'Royal Challengers Bengaluru']

cities = [       'Mumbai',    'Chandigarh',       'Kolkata',     'Hyderabad',
       'Chennai',        'Jaipur',     'Bengaluru',          'Pune',
         'Delhi',        'Indore', 'Visakhapatnam',     'Abu Dhabi',
     'Ahmedabad',         'Dubai',       'Sharjah',   'Navi Mumbai',
       'Lucknow',      'Guwahati',    'Dharamsala',        'Mohali']

model_path = Path(__file__).resolve().parent / 'model.pkl'
pipe = pickle.load(open(model_path, 'rb'))

st.title("IPL Win Probability Predictor")

col1,col2 = st.columns(2)

with col1:
  batting_team = st.selectbox('Select the batting team', sorted(teams))
  
with col2:
  bowling_team = st.selectbox('Select the bowling team', sorted(teams))
  
selected_city = st.selectbox('Select host city', sorted(cities))

target = st.number_input('Target', min_value=0, step=1)

col3,col4,col5 = st.columns(3)

with col3:
  score = st.number_input('Score', min_value=0, step=1)
with col4:
  overs = st.number_input('Overs completed', min_value=0.0, max_value=20.0, step=0.1)
with col5:
  wickets = st.number_input('Wickets out', min_value=0, max_value=10, step=1)
  
if st.button('Predict Probability'):
  if batting_team == bowling_team:
    st.error('Batting team and bowling team cannot be same.')
    st.stop()

  runs_left = max(target - score, 0)
  balls_left = max(120 - int(overs * 6), 0)
  wickets = max(10 - int(wickets), 0)
  crr = (score / overs) if overs > 0 else 0.0
  rrr = ((runs_left * 6) / balls_left) if balls_left > 0 else (0.0 if runs_left == 0 else 36.0)
  input_df = pd.DataFrame({
    'batting_team':[batting_team],
    'bowling_team':[bowling_team],
    'city':[selected_city],
    'runs_left':[runs_left],
    'balls_left':[balls_left],
    'wicket_left':[wickets],
    'total_runs_x':[target],
    'crr':[crr],
    'rrr':[rrr]
  })
  
  # st.table(input_df)
  result = pipe.predict_proba(input_df)
  loss = result[0][0]*100
  win = result[0][1]*100
  st.header(batting_team + "-" + str(round(win,2)) + "%")
  st.header(bowling_team + "-" + str(round(loss,2)) + "%")
  
