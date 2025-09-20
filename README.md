Disease Prognosis System Using Naive Bayes
A machine learning-based diagnostic tool that predicts diseases from symptom inputs using a Naive Bayes classifier. Built as part of my Bachelor's final year project and GitHub debut, this modular Python application demonstrates structured ML design, healthcare relevance, and interactive prediction.

 Features
Symptom-based disease prediction
Multinomial Naive Bayes model
Accuracy and classification report
Interactive terminal-based input
Modular code structure for scalability
Clean separation of logic across files

Folder Structure
disease-prognosis-naive-bayes/
│
├── data/
│   └── training_data.csv
├── models/
│   └── naive_bayes_model.pkl
├── src/
│   ├── preprocess.py
│   ├── evaluate.py
│   └── predict.py
├── main.py
├── requirements.txt
└── README.md

## 🚀 How to Run

1. **Clone the repository**  
   Open your terminal and run:
git clone https://github.com/your-username/disease-prognosis-naive-bayes.git cd disease-prognosis-naive-bayes

2. **Install dependencies**  
Make sure you have Python installed, then run:
pip install -r requirements.txt

3. **Run the main script**  
Execute the project:
python main.py

4. **Interact with the system**  
Enter symptoms one by one (1 = present, 0 = absent) when prompted.  
The model will predict the most likely disease based on your input.

Sample Output
🔍 Evaluation Report:
              precision    recall  f1-score   support

       Flu       1.00      1.00      1.00         1
  Sinusitis       1.00      1.00      1.00         1

✅ Accuracy: 1.00

🧪 Enter symptoms (1 = yes, 0 = no):
fever: 1
cough: 1
headache: 1
...

🩺 Predicted Disease: Flu






