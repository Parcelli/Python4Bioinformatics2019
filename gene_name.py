#!/usr/bin/env python
#9/07/2021
_name=[]
def genename_extractor(file):
    """
    Takes in a file with species names in the first field and extracts the gene names into a list
    """
    with open(file,'r') as myfile:
        lines=myfile.readlines()
        for i,line in enumerate(lines):
            if i>35:
                sp_line=line.split()
                field=(sp_line [0])
                if field.startswith("-"):
                    break
                final_field=' '.join(field)
                gene_name.append(field)
    return(gene_name) 

 
    



