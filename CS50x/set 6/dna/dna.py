import csv
import sys


def main():
    # Check if the user has provided the correct number of arguments
    if len(sys.argv) != 3:
        sys.exit("Usage: python dna.py data.csv sequence.txt")

    sequences = []
    dnafile = {}
    # Open the CSV file and read the contents into a dictionary
    with open(sys.argv[1]) as dictfile:
        for index, row in enumerate(dictfile):
            if index == 0:
                # Extract the DNA sequences from the first row of the CSV file
                sequences = [sequence for sequence in row.strip().split(",")][1:]
            else:
                # Extract the name and DNA sequence from each subsequent row of the CSV file
                name = row.strip().split(",")
                dnafile[name[0]] = name[1:]

    # Open the text file containing the DNA sequence to be analyzed
    with open(sys.argv[2], "r") as txtfile:
        sqcfile = txtfile.read().replace("\n", "")

    # Find the longest run of each DNA sequence in the input file
    result = [longest_match(sqcfile, subsequence) for subsequence in sequences]

    # Compare the results to the DNA sequences in the CSV file
    for s in dnafile:
        count = 0
        for j in range(len(dnafile[s])):
            if result[j] == int(dnafile[s][j]):
                count += 1
        if count == len(sequences):
            # If there is a match, print the name of the person
            return print(s)

    # If there is no match, print "No match"
    return print("No match")


def longest_match(sequence, subsequence):
    """Returns length of longest run of subsequence in sequence."""
    longest_run = 0
    subsequence_length = len(subsequence)
    sequence_length = len(sequence)

    for i in range(sequence_length):
        count = 0

        while True:
            start = i + count * subsequence_length
            end = start + subsequence_length

            if sequence[start:end] == subsequence:
                count += 1
            else:
                break

        longest_run = max(longest_run, count)

    return longest_run


main()