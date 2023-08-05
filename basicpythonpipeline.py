
# This pipeline takes DNA sequences in FASTA format as input and does the following tasks: calculate sequence lengths, count the occurrence of each nucleotide (A, C, G, T), and identify potential coding regions (open reading frames).

# Required Python Libraries
from Bio import SeqIO

# Function to Calculate Sequence Lengths
def calculate_sequence_lengths(input_file):
    sequences = SeqIO.parse(input_file, "fasta")
    for record in sequences:
        print(f"Sequence ID: {record.id}, Length: {len(record.seq)} bases")

# Function to Count Nucleotides
def count_nucleotides(input_file):
    sequences = SeqIO.parse(input_file, "fasta")
    for record in sequences:
        nucleotide_counts = {
            "A": record.seq.count("A"),
            "C": record.seq.count("C"),
            "G": record.seq.count("G"),
            "T": record.seq.count("T")
        }
        print(f"Sequence ID: {record.id}, Nucleotide Counts: {nucleotide_counts}")

# Function to Identify Open Reading Frames (ORFs)
def find_orfs(input_file, min_length):
    sequences = SeqIO.parse(input_file, "fasta")
    for record in sequences:
        orfs = []
        for i in range(len(record.seq) - min_length + 1):
            frame = record.seq[i:i+min_length]
            if 'N' not in frame:  # Exclude regions with ambiguous bases
                orfs.append(frame)
        print(f"Sequence ID: {record.id}, ORFs with Minimum Length {min_length}: {orfs}")

# Main Pipeline
if __name__ == "__main__":
    input_file = "input_sequences.fasta"
    min_orf_length = 50
    
    print("Calculating Sequence Lengths:")
    calculate_sequence_lengths(input_file)
    
    print("\nCounting Nucleotides:")
    count_nucleotides(input_file)
    
    print("\nFinding Open Reading Frames (ORFs):")
    find_orfs(input_file, min_orf_length)
