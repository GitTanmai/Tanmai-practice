import re
ln= int(input())
st= ''
for i in range(0,ln):
    st+=input()+"\n"
    
#print(st)
st= re.sub(" && ", " and ", st)
#print(st)    
st= re.sub(" \|\| ", " or ", st)
print(st)    