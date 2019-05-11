import re
n=input("enter the string with name and ages(first letter capital of name)")
ages=re.findall(r'\d{1,3}',n)
names=re.findall(r'[A-Z][a-z]*',n)
print("ages=",ages)
print('names=',names)

         #vowel
pattern=r"[aeiou]"
if re.search(pattern,"clue"):
    print("match clue")
if re.search(pattern,"bcdfg"):
    print("match bcdfg")

    #extract email
patrn=r"[\w.-]+@[\w.-]+"
string="please send info at info@oxford.com"
match=re.search(patrn,string)
if match:
    print("email:",match.group())
else:
    print("no match")

#extract each character
result=re.findall(r'.','Google for search')
print(result)

#Extract each word
res=re.findall(r'\w+','Good Going')
print(res)

#character in pair
rs=re.findall(r'\w\w','Good Going')
print(rs)

#first two char of evevry word
s=re.findall(r'\b\w\w','Good Going')
print(s)

#extract date
d=re.findall(r'\d{2}-\d{2}-\d{4}',"wish me on 17-08-1999")
print(d)

#extract year
y=re.findall(r'\d{4}',"wish me on 17-08-1999")
print(y)

#extract word start with vowel
v=re.findall(r'\b[aeiouAEIOU]\w*',"wish me on 17-08-1999")
print(v)

#Mobile no extract that start with 7,8,9
list=['1234566789','9876654321','8796543621','7654632190']
for i in list :
    op=re.findall(r'[7-9]{1}[0-9]{9}',i)
    if op:
        print(op,end='')

#SUB
sub=re.sub('[,;-]',' ','Hi, I am using - Whatsapp;')
print(sub)





        



