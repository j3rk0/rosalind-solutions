with open('data/rosalind_dna.txt') as f:
    dna = f.readline()

# %% COUNT NUMBER OF EACH BASE

A = dna.count('A')
C = dna.count('C')
G = dna.count('G')
T = dna.count('T')

# %% SAVE OCCURENCES OF THE BASES

with open('data/rosalind_dna_sub.txt', 'w') as f:
    f.write(f"{A} {C} {G} {T}")

