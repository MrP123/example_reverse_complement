"""
This script should provide the function "reverse_complement" that takes a DNA sequence as input and returns the reverse complement of the sequence.
"""


def reverse_complement(dna_sequence):
    """A Function that returns the reverse complement of a DNA sequence"""

    translation_dict = {"A" : "T",
                        "T" : "A",
                        "G" : "C",
                        "C" : "G"}
    
    complement = ""
    for base in dna_sequence:
       
        # Wenn es vorkommt
        if base in translation_dict.keys():
            new_base = translation_dict[base]
        
        # Sonst
        else:
            new_base = "_"
        complement += new_base


    return complement[::-1]

if __name__ == "__main__":
    dna_sequence = "ATGATCTCGTAAa"
    reverse_complement_sequence = reverse_complement(dna_sequence)
    print(dna_sequence)
    print(reverse_complement_sequence)