#my repo
with open('text1.txt', encoding='utf-8', errors='ignore') as file:
    text = file.read()

wordfrequency={}
m=text.split()
for i in m:
    if i.endswith(':'):
        if i in wordfrequency:
            wordfrequency[i]+=1
        else:
            wordfrequency[i]=1
    else:
        continue
print('writing the name in the format (name:)will give u no of messages sent by them')
name=input('name of the person: ')
if name not in wordfrequency.keys():
    KeyError("")
try:
    print(wordfrequency[name])
except KeyError :
    print('please use the proper format / no user found')

