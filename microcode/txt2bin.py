import numpy as np
def generate_combinations(string):
    global combinations

    # Zähle die Anzahl der 'x' im String
    num_x = string.count('x')
   
    # Erzeuge alle möglichen Kombinationen von '1' und '0' der Länge num_x
    for i in range(2 ** num_x):
        binary = bin(i)[2:].zfill(num_x)  # Binärdarstellung der Zahl mit führenden Nullen auffüllen
        combination = string.replace('x', '{}').format(*binary)  # Ersetze 'x' durch die Kombination
        addr=int(combination[:13],base=2)
        #print(combination[13:])
        d=int(combination[13:],base=2)
        #combinations.append(combination)
        #print(addr,data,combination)
        #print(addr,d)
        combinations.append([addr,d])
    
    #combinations=np.array(combinations)

def save_lines(elemente, dateiname):
    with open(dateiname, 'ab') as datei:
        for element in elemente:
            #datei.write(str(element) + '\n')
            print(element)
            datei.write(bytes(int(element,base=2)))


oldfile = 'EEPROM_4_kurz.txt' #input("Dateiname: ")
newfile = 'EEPROM_4.bin' #input("Neue Datei: ")
combinations=[]
with open(oldfile, 'r') as datei:
    for zeile in datei.read().split('\n'): # Verarbeite die Zeile hier
        zeile = zeile.strip()
        if (not(((zeile.startswith('0'))or(zeile.startswith('1')))or(zeile.startswith('x')))):
                continue
        else:
            #print('zeile',zeile)
            generate_combinations(zeile)
            #save_lines(combi_strings, newfile)
            #combinations.append(combi_strings)
combinations= np.array(combinations)
#print(combinations)
combinations_sorted= combinations[combinations[:, 0].argsort()]
print(combinations_sorted)

length=combinations_sorted[-1,0]
all_combinations=np.zeros([length])
for i in range(length):
    found=False
    for k,j in enumerate(combinations_sorted[:,0]):
        #print(j)
        if int(i)==int(j):
            found=True
            all_combinations[i] = combinations_sorted[k,1]
            break
    if not(found):
        all_combinations[i] = 0

with open(newfile,'wb') as datei2:
    for combination in all_combinations:

        datei2.write(int(combination).to_bytes(1, 'little'))
        print(combination)
    #save_lines(elemente, dateiname):
#print(length,combinations_sorted)
print(all_combinations[0])
#print("Done")