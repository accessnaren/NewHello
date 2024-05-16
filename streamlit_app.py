import streamlit as st
st.write('Hellow world')

st.header('st.button')
if st.button('say hello'):

    st.write('why Hello there')
else:
    st.write('GoodBye')