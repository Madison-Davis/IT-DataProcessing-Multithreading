# Data Processing

# Part 1: Multithreading
See code for implementation. More details shown below: </br>
Canine Class DNA was utilized to showcase the power of multithreading scientific data.  Multithreading refers to having a single processor/CPU handle multiple tasks "threads" simultaneously.

Dataset:
A single class sample of the dog canine DNA was utilized for this project.  The full dataset can be found here: https://www.kaggle.com/code/singhakash/dna-sequencing-with-machine-learning/data

 Threads Tested:
1: Single Nucleotide Count

2: Unique Nucleotide Pairings Where Order Matters

3: Most Frequent Identifiable Nucleotide Pairing

Thread Results:
Single Nucleotide Count, {'A': 172, 'T': 126, 'G': 359, 'C': 387}

Unique Nucleotide Pairings Where Order Matters, ['AT', 'GG', 'AA', 'AC', 'CC', 'TT', 'CT', 'CG', 'GA', 'GC', 'TG', 'TC', 'AG', 'TA', 'GT', 'CA']

Most Frequent Identifiable Nucleotide Pairing, {'GC': 85}

 Thread vs Normal Time Comparison:
Time Elapsed, 0.0 : Multithreading
Time Elapsed, 0.0006768703460693359 : Normal


# Part 2: Multiprocessing
See code for implementation. More details shown below: </br>
Demonstrating how multiprocessing can provide benefits in parallel data processing.

Results: multiprocessing (where an individual adds more than one CPU to allow multiple processors to run code all at once) was 5x faster than normal computation.

0.011406898498535156 : Multiprocessing

0.055684804916381836 : Normal

Data:
A random exponential function was utilized to mimic bacteria growth over a span of 30,0000 arbitrary units of time.
