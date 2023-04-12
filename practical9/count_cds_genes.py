import re
#read the file
f = open('Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa', 'r')
stop_codon=input('Please chose a stop codon from TAA, TAG and TGA:')
#remove \n and add \n before >
cdna = f.read().replace('\n', '')
cdna2=re.sub('>','\n>',cdna)
#remove the information
cdna3=re.sub('cdna.+]','',cdna2)
lines=cdna3.splitlines()

if stop_codon=='TGA':
 cdna4_TGA = [gene for gene in lines if gene.endswith("TGA")]
 cdna4_new_TGA=[]
#count the number of 'TGA'
 for gene_TGA in cdna4_TGA:
#avoid the situation like 'ATGA...', so extract the string without the start codon.
    gene_TGA1=re.findall('ATG(.+)',gene_TGA)
    gene_TGA1=''.join(gene_TGA1)
    co=gene_TGA1.count('TGA')
    gene_TGA=re.sub(' ',' '+str(co)+' ',gene_TGA)
    cdna4_new_TGA.append(gene_TGA)
#conver the list into string, and reset the format
 cdna4_new_TGA=''.join(cdna4_new_TGA)
 cdna5_TGA=re.sub('A>','A\n>',cdna4_new_TGA)
 cdna6_TGA= re.sub(r'(\d)\s', r'\1\n', cdna5_TGA)
#output a file named 'TGA_stop_genes.fa'
 with open("TGA_stop_genes.fa", "w") as f:
    f.write(cdna6_TGA)
#the mechanism is similar
elif stop_codon=='TAA':
 cdna4_TAA = [gene for gene in lines if gene.endswith("TAA")]
 cdna4_new_TAA=[]
 for gene in cdna4_TAA:
    gene_TAA1=re.findall('ATG(.+)',gene)
    gene_TAA1=''.join(gene_TAA1)
    co=gene_TAA1.count('TAA')
    gene_TAA=re.sub(' ',' '+str(co)+' ',gene)
    cdna4_new_TAA.append(gene_TAA)
 cdna4_new_TAA=''.join(cdna4_new_TAA)
 cdna5_TAA=re.sub('A>','A\n>',cdna4_new_TAA)
 cdna6_TAA=re.sub(r'(\d)\s', r'\1\n', cdna5_TAA)
 with open("TAA_stop_genes.fa", "w") as f:
    f.write(cdna6_TAA)
elif stop_codon=='TAG':
 cdna4_TAG = [gene for gene in lines if gene.endswith("TAG")]
 cdna4_new_TAG=[]
 for gene in cdna4_TAG:
    gene_TAG1=re.findall('ATG(.+)',gene)
    gene_TAG1=''.join(gene_TAG1)
    co=gene_TAG1.count('TAG')
    gene_TAG=re.sub(' ',' '+str(co)+' ',gene)
    cdna4_new_TAG.append(gene_TAG)
 cdna4_new_TAG=''.join(cdna4_new_TAG)
 cdna5_TAG=re.sub('G>','G\n>',cdna4_new_TAG)
 cdna6_TAG=re.sub(r'(\d)\s', r'\1\n', cdna5_TAG)
 with open("TAG_stop_genes.fa", "w") as f:
    f.write(cdna6_TAG)
else:
    print('notfound')
