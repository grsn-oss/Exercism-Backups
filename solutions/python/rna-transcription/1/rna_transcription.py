def to_rna(dna_strand):
    rna_complement =""
    for index in range(0,len(dna_strand)):
        if dna_strand[index] == 'G':
            rna_complement += 'C'
        elif dna_strand[index] == 'C':
            rna_complement += 'G'
        elif dna_strand[index] == 'T':
            rna_complement += 'A'
        elif dna_strand[index] == 'A':
            rna_complement += 'U'
        else:
            continue 

    return rna_complement