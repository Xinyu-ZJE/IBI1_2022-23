def Protein_coding_capability_calculator(sequence):
    import re
#extract the code between 'atg' and 'tga', ignoring the case
#Noting that I have assumed that there's only one 'ATG' and only one'TGA'!
    ls_coding_sequence=re.findall('ATG(.*?)TGA',sequence,re.IGNORECASE)
#convert the list into string 
    coding_sequence=''.join(ls_coding_sequence)
    percentage=100*len(coding_sequence)/len(sequence)
#ensure that there is no illegal character
    if len(set(sequence)-set('ATCGatcg'))==0:
      if percentage>50:
       return percentage,'%'," It's a protein-coding sequence."
      elif percentage<10:
        return percentage,'%'," It's a non-coding sequence."
      else:
        return percentage,'%'," It's unclear"
    else:
        return 'illegal character'
    return
# Example1 protein-coding sequence
x=Protein_coding_capability_calculator('ATGGGGgGGGGgGGGGGGGGGGGGGGGGGGGGGGGGGGGGGTGA')
#Using *to remove ()
print(*x)
#'86.36363636363636 %  It's a protein-coding sequence.'
y=Protein_coding_capability_calculator('ATgaActGA')
print(*y)
#'33.333333333333336 %  It's unclear'
z=Protein_coding_capability_calculator('AAAAAAAAAAAAAAAAAAAAAAAAAAAAAATGAAcTGA')
print(*z)
#'7.894736842105263 %  It's a non-coding sequence.'
p=Protein_coding_capability_calculator('ZAAAAAAAAAAAAAAAAAAAAAAAAAAAAAATGAAATGA')
print(p)
#'illegal character
