import streamlit as st
import pandas as pd

st.write("""
## Division of 2 numbers
**Enter 2 numbers**
""")

def user_input():
  num = st.number_input('Numerator')
  deno = st.number_input('Denominator')
  result = None
  
  if deno == 0:
    result = 'undefined'
  else:
    result = num / deno
  
  return pd.DataFrame({
    'NUMERATOR': num,
    'DENOMINATOR': deno,
    'DIVISION': result
  }, index=[0])


df = user_input()
st.write("""
### Result
""")
st.write(df)
