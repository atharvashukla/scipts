#!/bin/bash

# Check if the script received an input file
if [ "$#" -ne 1 ]; then
    echo "Usage: $0 input_file.txt"
    exit 1
fi

input_file="$1"

# Check if the input file exists
if [ ! -f "$input_file" ]; then
    echo "Input file not found: $input_file"
    exit 1
fi

# Initialize the output file
output_file="output.txt"
echo -n "" > "$output_file"

# Read input file line by line and convert MM:SS to seconds
while IFS= read -r line; do
    minutes=$(echo "$line" | cut -d ':' -f 1)
    seconds=$(echo "$line" | cut -d ':' -f 2)
    total_seconds=$((minutes * 60 + seconds))
    echo "$total_seconds" >> "$output_file"
done < "$input_file"

echo "Conversion completed! Check the output in $output_file"
