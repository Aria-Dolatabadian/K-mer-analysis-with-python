def count_kmers(sequence, k_size):
    data = {}
    size = len(sequence)
    for i in range(size - k_size + 1):
        kmer = sequence[i: i + k_size]
        try:
            data[kmer] += 1
        except KeyError:
            data[kmer] = 1
    return data

output = count_kmers("CTGACTGACTGACTGTA", 3)
#Generate the frequency of the coverage values
print (output)
def calculate_coverage_frequence(kmer_dataset):
    _coverage_freq = {}
    for coverage in kmer_dataset.values():
        try:
            _coverage_freq[coverage] += 1
        except KeyError:
            _coverage_freq[coverage] = 1
    return _coverage_freq

results = calculate_coverage_frequence(output)
#returns how many times k-mers with coverage X appears in our sample
print(results)
