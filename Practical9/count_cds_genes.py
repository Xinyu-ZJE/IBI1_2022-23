import re
#read the file
f = open('Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa', 'r')
stop_codon=input('Please chose a stop codon from TAA, TAG and TGA:')
#remove \n and add \n before >
cdna = f.read().replace('\n', '')
cdna2=re.sub('>\D','\n>',cdna)
#remove the information
cdna3=re.sub('cdna.*]','',cdna2)
lines=cdna3.splitlines()

cdna4= [gene for gene in lines if gene.endswith(stop_codon)]
cdna4_new=[]
#count the number of input stop codon
if stop_codon=='TAA' or stop_codon=='TGA' or stop_codon=='TAG':
 for gene in cdna4:
#avoid the situation like 'ATGA...', so extract the string without the start codon.
    gene_1=re.findall('ATG(.+)',gene)
    gene_1=''.join(gene_1)
    co=gene_1.count(stop_codon)
    gene=re.sub(' ',' '+str(co)+' ',gene)
    cdna4_new.append(gene)
#conver the list into string, and reset the format
 cdna4_new=''.join(cdna4_new)
 cdna5=re.sub('(\S)>','\n>',cdna4_new)
 cdna6= re.sub(r'(\d)\s', r'\1\n', cdna5)
 filename=stop_codon+'_stop_genes.fa'
 with open(filename, "w") as f:
    f.write(cdna6)

else:
    print('not found')

if f:
    f.close()
