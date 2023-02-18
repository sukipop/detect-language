import os
import sys
import joblib

model_name = "model/model.joblib"
input_file = "input.txt"
output_dir = "output"

def detect_language(text):
    model = joblib.load(model_name)
    predictions = model.predict([text])
    return predictions[0]

# Create the output directory if it doesn't exist
if not os.path.exists(output_dir):
    os.mkdir(output_dir)

# Open the input file
with open(input_file, "r") as fin:
    # Initialize a dictionary to store the output file objects
    output_files = {}

    # Iterate over the lines in the input file
    for line in fin:
        # Strip whitespace and detect the language of the line
        line = line.strip()
        lang = detect_language(line)
        print(f"{line} - {lang}")

        # Create a new output file for the language if it doesn't exist
        if lang not in output_files:
            output_files[lang] = open(os.path.join(output_dir, f"{lang}.txt"), "w")

        # Write the line to the appropriate output file
        output_files[lang].write(line + "\n")

    # Close all output files
    for f in output_files.values():
        f.close()
