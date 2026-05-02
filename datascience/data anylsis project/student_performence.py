import streamlit as st
import pandas as pd

st.markdown("""
<style>
/* Background */
body {
    background-color: #0e1117;
}

/* Main container */
.block-container {
    padding: 2rem;
}

/* KPI Cards */
[data-testid="metric-container"] {
    background: linear-gradient(135deg, #1f77b4, #6a11cb);
    color: white;
    padding: 15px;
    border-radius: 15px;
    text-align: center;
    box-shadow: 0px 4px 15px rgba(0,0,0,0.4);
}

/* Headings */
h1, h2, h3 {
    color: #ffffff;
    text-align: center;
}

/* Selectbox styling */
div[data-baseweb="select"] {
    background-color: #1e1e2f;
    border-radius: 10px;
    color: white;
}

/* Tables */
.stDataFrame {
    border-radius: 10px;
    overflow: hidden;
}

/* Scrollbar */
::-webkit-scrollbar {
    width: 8px;
}
::-webkit-scrollbar-thumb {
    background: #888;
    border-radius: 10px;
}
</style>
""", unsafe_allow_html=True)



df=pd.read_csv('student_performance.csv')
st.title('Student Performance Anylsis')
st.subheader('Key Matrices')
col1, col2, col3, col4=st.columns(4)
col1.metric('Total Students',df['Student_ID'].nunique())
col2.metric('Average Attendence',df['Attendance'].mean())
col3.metric('Average Pass Student',((df['Final_Score']>30).sum())*100/df['Student_ID'].nunique())
col4.metric('Average top Performer Score(Abve 90%)',df[df['Final_Score']>=90]['Final_Score'].mean().round(2))


st.subheader('Parent Qualification')
parent_qualification=st.selectbox(' ',df['Parental_Education'].unique(),index=None,placeholder='Select the Parent Qualification')
filtered_df=df[df['Parental_Education']==parent_qualification]
st.write('Filtered Data',filtered_df)

st.subheader("Average Final Score of student According to their Parent Education ")

parent_qualification_avg=df.groupby('Parental_Education')['Final_Score'].mean()
st.bar_chart(parent_qualification_avg)



st.subheader('Internet Access')
internet_access=st.selectbox(' ',df['Internet_Access'].unique(),index=None,placeholder='Select the Yes/No')
filtered_df=df[df['Internet_Access']==internet_access]
st.write('Filtered Data',filtered_df)

st.subheader("Average Final Score of student According to their Internet conectivity ")

internet=df.groupby('Internet_Access')['Final_Score'].mean()
st.bar_chart(internet)


st.subheader('Subject-Wise Average Score')

subject_avg=df[['Math_Score','Science_Score','English_Score']].mean()
st.bar_chart(subject_avg)


st.subheader('Gender-Wice Data')
gender=st.selectbox(' ',df['Gender'].unique(),index=None,placeholder='Select the Male/Female')
filtered_df=df[df['Gender']==gender]
st.write('Filtered Data',filtered_df)

st.subheader('Gender-Wise Performence')

gender_avg=df.groupby('Gender')['Final_Score'].mean()
st.bar_chart(gender_avg)



st.subheader('Study Hours vs Final Score')
st.scatter_chart(data=df,x='Study_Hours',y='Final_Score')

st.subheader('Attandence vs Final Score')
st.scatter_chart(data=df,x='Attendance',y='Final_Score')


st.balloons()

st.markdown("""
<script>
const elements = window.parent.document.querySelectorAll('.stMetric');

elements.forEach((el, index) => {
    el.style.opacity = 0;
    setTimeout(() => {
        el.style.transition = "all 0.8s ease";
        el.style.opacity = 1;
        el.style.transform = "translateY(0px)";
    }, index * 200);
});
</script>
""", unsafe_allow_html=True)