"""
This script should provide the function "reverse_complement" that takes a DNA sequence as input and returns the reverse complement of the sequence.
"""


def reverse_complement(dna_sequence):
    """A Function that returns the reverse complement of a DNA sequence"""

    complement = ""
    for base in dna_sequence:
       
        if base == "A":
            new_base = "T"
        elif base == "T":
            new_base = "A"
        elif base == "G":
            new_base = "C"
        elif base == "C":
            new_base = "G" 
        else:
            new_base = "_"
        
        complement += new_base


    return complement[::-1]

if __name__ == "__main__":
    dna_sequence = "ATGATCTCGTAAaaaaa"
    reverse_complement_sequence = reverse_complement(dna_sequence)
    print(dna_sequence)
    print(reverse_complement_sequence)