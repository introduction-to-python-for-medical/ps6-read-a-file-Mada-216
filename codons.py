def create_codon_dict(path):
    codon_dict = {}
    with open(path, 'r') as file: 
        for row in file:
            # Split the row by tab characters
            cells = row.strip().split('\t')
            if len(cells) >= 3:  # Check that there are enough columns
                codon = cells[0]
                amino_acid = cells[2]
                codon_dict[codon] = amino_acid
            else:
                # Handle rows that do not have enough columns if needed
                print(f"Skipping malformed row: {row}")
    return codon_dic
