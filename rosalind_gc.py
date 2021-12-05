def read_gc(fname):
    with open(fname) as f:
        gc = f.readlines()
        x = None
        temp = None
        ids = []
        for l in gc:
            if x is None:
                x = []
                temp = []
                ids.append(l)
            elif 'G' in l or 'A' in l or 'C' in l:
                temp.append(l)
            else:
                ids.append(l)
                x.append(temp)
                temp = []
        x.append(temp)
        fasta = {}
        for i in range(len(ids)):
            id = ids[i].replace('>', '').replace('\n', '')
            fasta[id] = ''.join(x[i]).replace('\n', '')
        return fasta


# %%

fasta_dna = read_gc('data/rosalind_gc.txt')

max_gc = 0
max_id = None

for id in fasta_dna:
    curr = fasta_dna[id]
    len = 0
    gc_count = 0
    for base in curr:
        len += 1
        if base == 'C' or base == 'G':
            gc_count += 1
    gc = (gc_count / len)*100
    if max_gc < gc:
        max_gc = gc
        max_id = id

with open('data/rosalind_gc_sub.txt', 'w') as f:
    f.write(f"{max_id}\n{max_gc}")