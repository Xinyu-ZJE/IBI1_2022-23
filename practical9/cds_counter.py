import re
seq='ATGCAATCGACTACGATCTGAGAGGGCCTAA'
# avoid overlapping of start codon and stop codon
seq_1=re.findall('ATG(.+)',seq)
seq_2=''.join(seq_1)
number1=seq_2.count('TAA')
number2=seq_2.count('TGA')
number3=seq_2.count('TAG')
Total_number=number1+number2+number3
print(Total_number)