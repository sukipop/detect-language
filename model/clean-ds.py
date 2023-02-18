import pandas as pd
import shutil
import subprocess

# make a back up of the dataset
shutil.copyfile('dataset.csv', '.dataset.back')

# remove first line of input file
subprocess.run(['sed', '-i', '1d', 'dataset.csv'])

# remove empty lines from input file
subprocess.run(['sed', '-i', '/^$/d', 'dataset.csv'])

# remove duplicate lines from input file
subprocess.run(['sort', '-u', '-o', 'dataset.csv', 'dataset.csv'])

# shuffle lines in input file
subprocess.run(['shuf', '-o', 'dataset.csv', 'dataset.csv'])

# add header line to input file
header = 'text,language\n'
with open('dataset.csv', 'r+') as f:
    content = f.read()
    f.seek(0, 0)
    f.write(header + content)

# Load the data from a CSV file (skipping the first line)
data = pd.read_csv("dataset.csv")

# Count the number of examples for each language
counts = data.groupby("language").size().sort_values(ascending=False)

# Print the language values and example counts in descending order of counts
for lang, count in counts.items():
    print(f"{lang}: {count}")
