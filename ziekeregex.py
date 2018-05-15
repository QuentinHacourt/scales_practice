import re



with open('Phrygian.txt', 'r') as modeText:
    text = modeText.read()



lijst1 = re.findall(r'\d+', text)
lijst = []
for i in range(0,len(lijst1)-1):
    lijst.append(int(lijst1[i]))


print(lijst)
minimum = min(lijst)
maximum = max(lijst)

for i in range(minimum, maximum+1):
    patroon1 = str(i)
    print(patroon1)
    patroon2 = str(i-minimum)

    numberRegex = re.compile(patroon1)
    text = numberRegex.sub(patroon2,text)
    
fgdh

print(text)

with open('Phrygian.txt', 'w') as modeText:
    modeText.write(text)

