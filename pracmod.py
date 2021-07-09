#!/usr/bin/env python
gene_name=[]
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
#writing out to a output file
def gene_writer(gene_name,output_file):
    with open(output_file,'w') as myfile:
        myfile.write("Gene names\n")
        for name in gene_name:
            myfile.write(name+"\n")
            
if __name__=="__main__":
    import sys
    
    
    #define inputs
    humchrx=sys.argv[1]
    gene_list=sys.argv[2]

    #workflow
    print("Extracting gene names from humchrx file")
    gene_name=genename_extractor(humchrx)
    print("writing the gene names to an output file")
    gene_writer(gene_name,gene_list)

    