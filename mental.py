import streamlit as st
import re
import pickle 


#  clean input data
def clean_text(text):
    text=re.sub(r"[^a-zA-Z\s]","",text)
    return text.lower()
#  load Model 
with open("model.pkl","rb") as f:
    model = pickle.load(f)

# vectorizer
with open("vectorizer.pkl", "rb") as f:
    vectorizer = pickle.load(f)

st.set_page_config(page_title="Mental Health Checker", layout="centered")

st.title("🧠 Mental Health Message Analyzer")
st.write("Enter a WhatsApp message and check for signs of anxiety, depression, suicidal thoughts, or normal behavior.")

user_input = st.text_area("💬 Enter a message:", height=100)

    # Analyze button
if st.button("Analyze"):
    if user_input.strip() == "":
        st.warning("Please enter a message to analyze.")
    
    else:
        with st.spinner("Analyzing..."):
            cleaned=clean_text(user_input)
            input_vector= vectorizer.transform([cleaned])
            prediction = model.predict(input_vector)[0]

        # st.markdown("......")
        st.subheader("Prediction Result:")

        if prediction.lower() == "suicidal":
                st.error("🚨 Urgent: Signs of **Suicidal Thoughts** detected.")
        elif prediction.lower() == "depression":
            st.warning("⚠️ Signs of **Depression** detected.")
        elif prediction.lower() == "anxiety":
            st.info("😟 This message may indicate **Anxiety**.")
        elif prediction.lower() == "stress":
            st.info("💢 The message suggests **Stress**.")
        elif prediction.lower() == "bipolar":
            st.warning("🌀 **Bipolar Disorder**-like expression detected.")
        elif prediction.lower() == "personality disorder":
            st.warning("🧩 Possible **Personality Disorder** indicators found.")
        else:
            st.success("✅ The message appears to be **Normal**.")
