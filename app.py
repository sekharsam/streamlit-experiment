import streamlit as st
import pandas as pd
import numpy as np

st.title('Hello Streamlit')

##Display a simple text
st.write('Its a simple text')

##create a simple dataframe
df= pd.DataFrame({
    'first_column': [1,2,3,4],
    'second column': [10,20,30,40]
})

## Display the dataframe
st.write("Here is the datafrme")
st.write(df)

## create line chart
chart_data=pd.DataFrame(
    np.random.randn(20,3),columns=['a','b','c']
)
st.line_chart(chart_data)