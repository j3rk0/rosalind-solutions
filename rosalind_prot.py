import csv

with open('data/codon_table.csv') as in_file:
    reader = csv.reader(in_file)
    codons = {}
    for row in reader:
        codons[row[0]] = row[1]

with open('data/rosalind_prot.txt') as in_file:
    x = in_file.readline()

y = []
for i in range(0, len(x) - 2, 3):
    curr = x[i:i + 3]
    y.append(codons[curr])

res = ''.join(y).replace('Stop', '')

with open('data/rosalind_prot_sub.txt', 'w') as f:
    f.write(res)

