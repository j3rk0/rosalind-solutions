with open('data/rosalind_revc.txt') as f:
    dna = f.readline()

# %%
rev_comp = ""
for base in reversed(dna):
    if base == 'G':
        rev_comp += 'C'
    elif base == 'T':
        rev_comp += 'A'
    elif base == 'C':
        rev_comp += 'G'
    elif base == 'A':
        rev_comp += 'T'

# %%

with open('data/rosalind_revc_sub.txt', 'w') as f:
    dna = f.write(rev_comp)
