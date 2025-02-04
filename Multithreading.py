# Imports
import threading
import time


# Variables and Functions
def characterSplit(word):
    return [char for char in word]

data = "ATGGAAACACCCTTCTACGGCGATGAGGCGCTGAGCGGCCTGGGCGGCGGCGTCAGTAGCAGTGGCGGCGGTGGTAGCTTCGCGTCCCCGGGTCGCCTGTTTCCCGGGGCGCCCCCGACGGCGGCGACTGGCAGCATGATGAAGAAAGACGCGCTGACGCTGAGCCTGAGCGAGCAGGTGGCGGCGGCGCTCAAGCCCGCGGCCGCGCCGCCCCCGGCCCCCCTGCGCACCGACGGCGCCCCAGGCACGGCGCCCCCCGACGGCCTACTCTCCTCGCCCGACCTGGGGCTGCTCAAGCTCGCCTCGCCCGAGCTCGAGCGCCTAATCATCCAGTCCAACGGGCTGGTCACCACCACGCCGACGAGCACTCAGTTCCTCTACCCCAAGGTGGCGGCCAGCGAGGAGCAGGAGTTTGCCGAGGGCTTCGTCAAGGCCCTGGAAGACTTGCACAAGCAGAACCAGCTGGGCACGGGCGCGGCCTCGGCAGCCGCGGCCGCCGGAGGACCCTCGGGCACGGCTGCGGGCGCCGCGCCTCCTGGCGAACTGGCCCCAGCGGCAGCCACGCCCGAGGCGCCCGTCTACGCGAACCTGAGCAGCTACGCGGGCGGCACCGGGGGTTCGGGGGGTGCTGCGACGGTCGCCTTCGCCGCGGAGCCTGTGCCCTTCCCTCCGCCACCGCCCCCAGGCGCGCTGGGGCCGCCCCGCCTGACCGCGCTCAAGGATGAGCCGCAGACGGTGCCCGACGTGCCAAGCTTCGGCGAGAGCCCGCCGTTGTCGCCCATCGACATGGACACGCAGGAGCGCATTAAGGCGGAGCGCAAGCGGCTGCGCAACCGCATCGCTGCCTCTAAGTGCCGCAAGCGCAAGCTGGAGCGCATCTCGCGCCTCGAGGAGAAAGTGAAGACGCTCAAGAGCCAGAACACGGAGCTGGCGTCCACAGCGAGCCTGCTGCGCGAGCAGGTGGCGCAGCTCAAGCAGAAGGTCCTCAGCCACGTCAACAGCGGCTGCCAGCTGCTGCCCCAGCACCAGGTGTCCGCGTACTGA"
nucleotideSingles = characterSplit(data)
nucleotidePairs = [data[i:i + 2] for i in range(0, len(data), 2)]
numNucleotides = {}
nucleotidePairings = []
mostFrequentNucleotidePairing = {}

def countNucleotides(data):
    A = 0
    T = 0
    G = 0
    C = 0
    for value in data:
        if value == "A":
            A += 1
        elif value == "T":
            T += 1
        elif value == "G":
            G += 1
        elif value == "C":
            C += 1
    numNucleotides.update({"A": A, "T": T, "G": G, "C": C})

def similarPairings(data): # in our scenario we decided order does matter, so TA != AT
    for value in data:
        if value not in nucleotidePairings:
            nucleotidePairings.append(value)
            
def process3(data):
    frequencyDict = {}
    for value in data:
        if value not in frequencyDict:
            frequencyDict.update({value : 1})
        else:
            frequencyDict[value] = frequencyDict[value] + 1
    mostFrequentPair = max(frequencyDict, key = frequencyDict.get)
    mostFrequentNucleotidePairing.update({mostFrequentPair : frequencyDict[mostFrequentPair]})


# Program
if __name__ == "__main__":
    task1 = threading.Thread(target = countNucleotides, args = (nucleotideSingles,))
    task2 = threading.Thread(target = similarPairings, args = (nucleotidePairs,))
    task3 = threading.Thread(target = process3, args = (nucleotidePairs,))
    # Multithreading
    start = time.time()
    end = time.time()
    print(end - start, ": Multithreading")
    # Normal
    start = time.time()
    countNucleotides(nucleotideSingles)
    similarPairings(nucleotidePairs)
    process3(nucleotidePairs)
    end = time.time()
    print(end - start, ": Normal")

print(numNucleotides)
print(nucleotidePairings)
print(mostFrequentNucleotidePairing)
