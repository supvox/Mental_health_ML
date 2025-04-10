#🧠 Mental Health ML Project

This project uses Machine Learning to detect mental health conditions (like anxiety, depression, suicidal thoughts, etc.) from WhatsApp chat inputs.

✅ Project Structure:
mental.py — Main script that launches the Streamlit UI for your ML model.

Pre-trained model loaded from a .pkl file (ensure it's in the same folder).

⚙️ Prerequisites:
Make sure you have Python and Streamlit installed in your environment.

If Streamlit is not installed, open CMD/Terminal and run:

bash
Copy
Edit
pip install streamlit
🚀 How to Run the App:
Open CMD or Terminal.

Navigate to your project directory where mental.py is located.

Run the following command:

bash
Copy
Edit
streamlit run mental.py
🧪 Features of the App:
Enter a WhatsApp message or line of text.

The model will analyze it and predict one of the following:

Normal

Anxiety

Depression

Suicidal

Stress

Bipolar

Personality Disorder
