

# 📧 Spam Detection Model using Naive Bayes

📌 Project Overview

This project involves designing a Machine Learning Model to classify emails into two categories: Spam or Ham (Not Spam). The model is built using Scikit-Learn's Naive Bayes algorithm (MultinomialNB class) and employs TfidfVectorizer for feature extraction and text transformation.

🔍 Key Features:

Classifies emails as Spam or Ham 📩.

Uses Naive Bayes (MultinomialNB) for accurate predictions 🧠.

TfidfVectorizer ensures optimal text transformation 🔠.

Designed a Streamlit WebApp for real-time message classification 🌐.

Utilizes Pickle module to save and load the trained model efficiently 📂.

🛠️ Technologies & Libraries Used

🔹 Machine Learning & NLP

Python 🐍

Scikit-Learn 🤖

Naive Bayes (MultinomialNB) 📊

TfidfVectorizer 🔡

Pickle 📦

🌐 Web Application

Streamlit 🚀

📊 Model Workflow

Preprocess Email Data 🧹.

Convert text data into numerical format using TfidfVectorizer 🔢.

Train the Naive Bayes classifier 🏋️.

Save the trained model using Pickle 📂.

Deploy a Streamlit WebApp for real-time email classification 🌍.

🌍 Streamlit WebApp

A user-friendly web application was built using Streamlit to allow users to input an email message and predict whether it is spam or ham.

📌 Below are glimpses of the WebApp's predictions:

![Screenshot (215)](https://github.com/user-attachments/assets/f4e3853f-6ea2-47d6-9a0a-48ef3a3cd00f)
![Screenshot (216)](https://github.com/user-attachments/assets/5a9694e1-f975-4b14-9fbc-168112d3f1eb)

🚀 How to Use the Model

Clone the repository:

git clone <YOUR_GIT_URL>
cd Spam-Detection-Model

Install dependencies:

pip install -r requirements.txt

Run the WebApp:

streamlit run app.py

Enter a message in the input field to check if it's spam or ham. 📩

🤝 Contribution

Contributions are welcome! Follow these steps:

Fork the repository 🍴

Create a feature branch (git checkout -b feature-name) 🌿

Commit your changes (git commit -m 'Added new feature') ✏️

Push to the branch (git push origin feature-name) 🚀

Submit a pull request 🔄

📢 "Detect spam emails effectively using Machine Learning!" 📧🚀




