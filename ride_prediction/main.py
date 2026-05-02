import streamlit as st 
import warnings
import pickle
warnings.filterwarnings("ignore")

st.header("Ride Prediction")
ppw=st.number_input("Enter price per week")
pn=st.number_input("Enter population")
mi=st.number_input("Enter monthly income")
appm=st.number_input("Averge Parking Per Month")
btn=st.button("Predict!")
if btn:
    model=pickle.load(open("taxi.pkl","rb"))
    res=model.predict([[ppw,pn,mi,appm]]).round(2)
    st.markdown(f"Expected Result={res}")