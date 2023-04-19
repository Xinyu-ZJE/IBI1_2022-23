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
        print(percentage,'%'," It's a protein-coding sequence.")
      elif percentage<10:
        print(percentage,'%'," It's a non-coding sequence.")
      else:
        print(percentage,'%'," It's unclear")
    else:
        print('illegal character')
    return
# Example1 protein-coding sequence
Protein_coding_capability_calculator('ATGGGGgGGGGgGGGGGGGGGGGGGGGGGGGGGGGGGGGGGTGA')
#'86.36363636363636 %  It's a protein-coding sequence.'
Protein_coding_capability_calculator('ATgaActGA')
#'33.333333333333336 %  It's unclear'
Protein_coding_capability_calculator('AAAAAAAAAAAAAAAAAAAAAAAAAAAAAATGAAcTGA')
#'7.894736842105263 %  It's a non-coding sequence.'
Protein_coding_capability_calculator('ZAAAAAAAAAAAAAAAAAAAAAAAAAAAAAATGAAATGA')
#'illegal character
