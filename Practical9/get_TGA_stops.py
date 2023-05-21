import re
f = open('Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa', 'r')
cdna = f.read().replace('\n', '')
cdna2=re.sub('>','\n>',cdna)
# delete other information
cdna3=re.sub('cdna.+]','',cdna2)
lines=cdna3.splitlines()
#modify the format
cdna4 = [gene for gene in lines if gene.endswith("TGA")]
cdna4=''.join(cdna4)
cdna5=re.sub('A>','A\n>',cdna4)
cdna6=re.sub(' ','\n',cdna5)
with open("TGA_genes.fa", "w") as f:
    f.write(cdna6)
if f:
    f.close()
