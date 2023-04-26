import pandas as pd
import re

#input a BLOSUM62 matrix
df = pd.read_excel("BLOSUM.xlsx")
#convert the excel into matrix
array1 = df.values

#open the txt file
human_ACE2 =open('ACE2_human.fa')
mouse_ACE2= open('ACE2_mouse.fa')
cat_ACE2= open('ACE2_cat.fa')

#convert the format into string
human_ACE2=human_ACE2.read()
mouse_ACE2=mouse_ACE2.read()
cat_ACE2=cat_ACE2.read()

#delete the first line
seq_human=re.sub('>.*?\n','',human_ACE2)
seq_mouse=re.sub('>.*?\n','',mouse_ACE2)
seq_cat=re.sub('>.*?\n','',cat_ACE2)

#define a function to perform calculate the score
def global_align(seq1,seq2):
    loc='ARNDCQEGHILKMFPSTWYVBZX'
    val=identity=0
#as for the -1: because every seq ends with a string \n (I don't know why)
    for n in range(len(seq1)-1):
        i = seq1[n]
        j = seq2[n]
#find the location of the score.note that the first row is not score
        a=loc.find(i)
        b=loc.find(j)+1
#sum up all the score
        val = val + array1[a][b]
        if i==j:
            identity +=1
    return '(1) score is',val,'(2) number of identical amino acids is',identity,'(3) percentage of identical amino acid is',identity/len(seq1)*100,'%'
print(*global_align(seq_mouse,seq_cat))
print(*global_align(seq_mouse,seq_human))
print(*global_align(seq_cat,seq_human))

