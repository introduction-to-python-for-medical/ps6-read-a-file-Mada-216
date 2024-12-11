def create_codon_dict(path):
    codon_dict = {}
    with open(path, 'r') as file: 
         for row in file:
             cells = row.strip().split('ََ\t')
             codon = cells [0]
             amino_acid = cells[2]
             codon_dict[codon] = amino_acid
    return codon_dict


