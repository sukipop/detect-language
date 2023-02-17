#!/bin/bash
input_file="dataset.csv"
header="text,language"

# Remove first line of input file
sed -i '1d' "$input_file"

# Remove empty lines from input file
sed -i '/^$/d' "$input_file"

# Remove duplicate lines from input file
sort -u -o "$input_file" "$input_file"

# Shuffle lines in input file
shuf -o "$input_file" "$input_file"

# Add header line to input file
echo "$header" | cat - "$input_file" > temp && mv temp "$input_file"
