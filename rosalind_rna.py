with open('data/rosalind_rna.txt') as f:
    dna = f.readline()

# %%

rna = dna.replace('T', 'U')

# %%

with open('data/rosalind_rna_sub.txt', 'w') as f:
    dna = f.write(rna)
