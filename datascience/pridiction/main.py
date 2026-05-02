import streamlit as st 
import pandas as pd
import warnings
import pickle
warnings.filterwarnings("ignore")

st.header("Sales Data Pridiction")
tv=st.number_input("Enter TV Ads")
radio=st.number_input("Enter Radio Ads")
newspaper=st.number_input("Enter Newspapers ADs")

btn=st.button("Predict!")
if btn:
    
    model=pickle.load(open('sales_data.pkl','rb'))
    lasso=model.predict([[tv,radio,newspaper]]).round(2)
    st.markdown(f'Ecpected Results= {lasso}')

df=pd.read_csv('sales_data.csv')

X=df[['TV','Radio','Newspaper']]
y=df['Sales']
model=pickle.load(open('sales_data.pkl','rb'))
features=X.columns
coefficients=model.coef_
st.subheader('Features Importance')
coef_df=pd.DataFrame({'features':features,'coefficients':coefficients})
st.bar_chart(coef_df.set_index('features'))

st.balloons()