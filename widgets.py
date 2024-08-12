import streamlit as st
import pandas as pd

st.title('streamlit text input')

name= st.text_input('Enter your input:')

if name:
    st.write(f'Hello, {name} ')


## slider
age=st.slider('Select your age:',0,100,25)

st.write(f'Your age is: {age}')


## select box
option=['Java', 'C', 'Python', 'C#']
choice = st.selectbox('Choose your favorite lanuguage :', option)
st.write(f'You selected {choice} as your language')

## show data in dataframe and save to csv
df = pd.DataFrame(
    {'name': ['Jon','von','don', 'con'],
    'age':['24','26','28','30'],
'country' : ['India','New Zealand', 'South Africa', 'Uruguay']}
)

df.to_csv('sampleData.csv')
st.write(df)

uploaded_file= st.file_uploader('Choose a csv file', type='csv')

if uploaded_file is not None:
    df=pd.read_csv(uploaded_file)
    st.write(df)