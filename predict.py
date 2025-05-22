import streamlit as st
import pickle
import sklearn
st.header('Titanic Survival Prediction')
st.subheader('Predicting Survival on the titanic')

model=pickle.load(open('model.pkl','rb'))
l1=pickle.load(open('l1.pkl','rb'))
l2=pickle.load(open('l2.pkl','rb'))

st.image('https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTv3fY81SDUWAajL4lo-2SqOSxjXV8jKyR2XQ&s')
#st.text('The Titanic, a British luxury passenger liner, was one of the largest and most opulent ships ever built. On its maiden voyage from Southampton, England, to New York City, the Titanic struck an iceberg in the North Atlantic on April 14, 1912. The ship sank on April 15, 1912, resulting in the deaths of over 1,500 passengers and crew, making it one of the deadliest peacetime maritime disasters in history.')

#pclass = st.number_input("Passenger Class")
pclass = st.radio("Passenger Class",(1,2,3))#select cheyyunna rubathil kittan
sex = st.text_input("enter sex: [male,female]")
age = st.number_input("Age")
sibsp = st.number_input("Number of Siblings/Spouses Aboard")
parch = st.number_input("Number of Parents/Children Aboard")
fare = st.number_input("Fare")
embarked = st.text_input("Embarked: [S,C,Q]")
if st.button("Predict"):
    sex_l = l1.transform([sex])[0]
    embarked_l = l2.transform([embarked])[0]
    Predict = model.predict([[pclass, sex_l, age, sibsp, parch, fare, embarked_l]])[0]
    if Predict==1:
        st.success("Survived")
    else:
         st.warnig("Did not Survived")