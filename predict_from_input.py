import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
import joblib

from src.preprocess import preprocess_data
from src.evaluate import evaluate_model
from src.predict import predict_from_input

# Load data
df = pd.read_csv("data/training_data.csv")

# Preprocess
X, y = preprocess_data(df)

# Split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train
model = MultinomialNB()
model.fit(X_train, y_train)

# Save model
joblib.dump(model, "models/naive_bayes_model.pkl")

# Evaluate
evaluate_model(model, X_test, y_test)

# Predict
predict_from_input(model, X.columns)
