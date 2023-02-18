import os
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.svm import LinearSVC
from sklearn.pipeline import Pipeline
import joblib

model_name = "model.joblib"
dataset_path = "dataset.csv"

# Load the data and remove any rows with NaN values
data = pd.read_csv(dataset_path).dropna()

# Split the data into training and testing sets
train_data = data.sample(frac=0.8, random_state=42)
test_data = data.drop(train_data.index)

# Check if the saved model file exists and delete it if it does
if os.path.isfile(model_name):
    os.remove(model_name)

# Train a new model
model = Pipeline([
    ('vectorizer', TfidfVectorizer()),
    ('classifier', LinearSVC(loss="squared_hinge", dual=False, verbose=1))
])
model.fit(train_data["text"], train_data["language"])

# Save the trained model
joblib.dump(model, model_name)
