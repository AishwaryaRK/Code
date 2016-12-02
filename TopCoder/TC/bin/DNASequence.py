class DNASequence:
    def longestDNASequence(self, sequence):
        count = 0
        longestDNASequence = 0
        dna = ('A', 'C', 'G', 'T')
        for c in sequence:
            if c in dna:
                count += 1;
            else:
                longestDNASequence = count if count > longestDNASequence else longestDNASequence
                count = 0
        longestDNASequence = count if count > longestDNASequence else longestDNASequence
        return longestDNASequence


print DNASequence().longestDNASequence("GATTACA")
