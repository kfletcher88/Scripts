import argparse
import re

# Define the command line arguments
parser = argparse.ArgumentParser(description='Parse input file and output tab-separated values.')
parser.add_argument('input_file', type=str, help='Path to the input file')
parser.add_argument('output_file', type=str, help='Path to the output file')
args = parser.parse_args()

# Open the input and output files
with open(args.input_file, "r") as input_file, open(args.output_file, "w") as output_file:
    output_file.write("Species1\tSpecies2\tdN/dS\tdN\tdS\n")
    # Initialize variables to store data from current block
    group1 = ""
    group2 = ""
    dnds = ""
    dn = ""
    ds = ""

    # Iterate through each line of the input file
    for line in input_file:

        # Use regular expressions to extract the relevant information from the line
        match = re.match(r'^\s*\d+\s\((.+)\)\s+\.\.\.\s+\d+\s+\((.+)\)\s*', line)
        if match:
            group1, group2, = match.groups()
        match = re.search(r'dN/dS\s*=\s*([\d\.]+)\s*dN\s*=\s*([\d\.]+)\s*dS\s*=\s*([\d\.]+)', line)
        if match:
            dnds, dn, ds = match.groups()
            output_file.write(f"{group1}\t{group2}\t{dnds}\t{dn}\t{ds}\n")

            # Reset the variables for the next block
            species1 = ""
            group1 = ""
            species2 = ""
            group2 = ""
            dnds = ""
            dn = ""
            ds = ""
