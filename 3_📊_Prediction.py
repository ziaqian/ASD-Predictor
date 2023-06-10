import streamlit as st
import pickle
import numpy as np
import sklearn

# Function to load the model
def load_model():
    loaded_model = pickle.load(open("ASD_model.sav", 'rb'))
    return loaded_model



st.set_page_config(page_title="ASD Predictor",page_icon="🧑‍⚕️")
st.title("AUTISM SPECTRUM DISORDER(ASD) PREDICTION")
st.sidebar.success("Select a page above")
st.write("---")
st.text("")

#input A1 Score
a1=st.number_input("I often notice small sounds when others do not. (1 for agree; 0 for disagree)")
st.write(a1 , " score")
st.text("")

#input A2 Score
a2=st.number_input("I usually concentrate more on the whole picture, rather than the small details.(1 for agree; 0 for disagree)")
st.write(a2 ," score")
st.text("")

#input  A3 Score
a3=st.number_input("I find it easy to do more than one thing at once.(1 for agree; 0 for disagree)")
st.write(a3 ," score")
st.text("")

#input A4 Score
a4=st.number_input("If there is an interruption, I can switch back to what i was doing very quickly.(1 for agree; 0 for disagree)")
st.write(a4 ," score")
st.text("")

#input A5 Score
a5=st.number_input("I find it easy to 'read between the lines' when someone is talking to me.(1 for agree; 0 for disagree)")
st.write(a5 ," score")
st.text("")

#input A6 Score
a6=st.number_input("I know how to tell if someone listening to me is getting bored.(1 for agree; 0 for disagree)")
st.write(a6 ," score")
st.text("")

# input A7 Score
a7=st.number_input("When I'm reading a story, I find it difficult to work out the character's intention.(1 for agree; 0 for disagree)")
st.write(a7 ," score")
st.text("")

#input  A8 Score
a8=st.number_input("I like to collect information about categories of things(e.g. types of car, types of bird, types of train, types of plant etc).(1 for agree; 0 for disagree)")
st.write(a8 ," score")
st.text("")

#input  A9 Score
a9=st.number_input("I find it easy to work out what someone is thinking or feeling just by looking at their face.(1 for agree; 0 for disagree)")
st.write(a9 ," score")
st.text("")

#input  A10 Score
a10=st.number_input("I find it difficult to work out people’s intentions.(1 for agree; 0 for disagree)")
st.write(a10 ," score")
st.text("")

feature_list=[a1,a2,a3,a4,a5,a6,a7,a8,a9,a10,]

user_input=np.array(feature_list).reshape(1,-1)


if st.button("PREDICT"):
    st.text("")
    st.subheader(("RESULT"))
    loaded_model=load_model()
    prediction=loaded_model.predict(user_input)
    st.write("Prediction")
    result=""
    if prediction==[[1]]:
        result="The patient HAS Autism."
    elif prediction == [[0]]:
        result="The patient DOES NOT HAVE Autism."

    st.code(result)
    st.text("")
