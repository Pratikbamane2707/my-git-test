file = input('Enter file name or path:')

dictt ={}
with open(file,'r') as file:
    content = file.read()
    content=content.lower()
    punch = "!?.,;:'\"-()[]{}<>@#$%^&*_+=~`|\\"
    cln_txt=''
    for i in content:
        if i not in punch:
            cln_txt+=i
    content=cln_txt
    for i in content.split(' '):
        if i.lower() not in dictt:
            dictt[i]=1
        else:
            dictt[i]+=1

def find_MaxKey(dictt):
    max_val=max(dictt.values())
    for i in dictt.items():
        if i[1]==max_val:
            return i
max_key=find_MaxKey(dictt)
print(f'Most frequent word: {max_key[0]} (Count: {max_key[1]})')