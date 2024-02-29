import streamlit as st
import pickle
import sklearn

pickle_in = open('model_iris.pkl','rb')
classifier = pickle.load(pickle_in)

def predict_iris_variety(sepal_length, sepal_width, petal_length, petal_width):
   prediction = classifier.predict([[sepal_length, sepal_width, petal_length, petal_width]])
   print(prediction)
   return prediction

def Input_Output():
   st.title("Iris Variety Prediction")
   st.image("https://preview.redd.it/my-cat-garbanzo-has-hard-scarred-ears-i-adopted-him-like-v0-s1poolvncelc1.jpg?width=4284&format=pjpg&auto=webp&s=c8aa4ab03ad0d81b2e9ed6578b22d0cd04312a0d", width=600)

   st.markdown("You are using streamlit", unsafe_allow_html=True)
   sepal_length = st.text_input("Enter Sepal Length")
   sepal_width = st.text_input("Enter Sepal Width")
   petal_length = st.text_input("Enter Petal Length")
   petal_width = st.text_input("Enter Petal Width")

   result = ""
   if st.button("Predict"):
      result = predict_iris_variety(sepal_length, sepal_width, petal_length, petal_width)
      st.balloons()
   st.success('The output is {}'.format(result))

if __name__ == '__main__':
   Input_Output()