myseq = 'CAATAGAGACTAAGCATTAT'
k = 3
step = 1

# Generate k-mers from the sequence
kmers = [myseq[i:i+k] for i in range(0, len(myseq)-k+1, step)]

# Print each k-mer
for subseq in kmers:
    print(subseq)
