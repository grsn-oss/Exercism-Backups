def proteins(strand):
    stack = ""
    Amino_acid = []
    M = ["AUG"]
    P = ["UUU","UUC"]
    L = ['UUA', "UUG"]
    S = ["UCU","UCC","UCA","UCG"]
    T = ["UAU","UAC"]
    C = ["UGU","UGC"]
    TP = ["UGG"]
    ST = ["UAA","UAG","UGA"]
    for char in strand:
        stack += char
        
        if len(stack) == 3:
            if stack in M:
                Amino_acid.append("Methionine")
                stack = ""
            if stack in P:
                Amino_acid.append("Phenylalanine")
                stack = ""
            if stack in L:
                Amino_acid.append("Leucine")
                stack = ""
            if stack in S:
                Amino_acid.append("Serine")
                stack = ""
            if stack in T:
                Amino_acid.append("Tyrosine")
                stack = ""
            if stack in C:
                Amino_acid.append("Cysteine")
                stack = ""
            if stack in TP:
                Amino_acid.append("Tryptophan")
                stack = ""
            if stack in ST:
                return Amino_acid

    return Amino_acid
        
