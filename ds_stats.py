import pandas as pd

# Load the data from a CSV file (skipping the first line)
data = pd.read_csv("dataset.csv")

# Count the number of examples for each language
counts = data.groupby("language").size().sort_values(ascending=False)

# Print the language values and example counts in descending order of counts
for lang, count in counts.items():
    print(f"{lang}: {count}")
