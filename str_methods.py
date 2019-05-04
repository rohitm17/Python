#capitalize()
a='hello'
c=a.capitalize()
print(a)
print(c)

#join()
b=('a','s','d','f','g')
p="".join(b)
print(b)
print(p)

#swapcase()
s=a.swapcase()
print(s)

#center(width,fillchar)
w=a.center(10,'$')
print(w)

#count(str,begin,end)
o=a.count('l',0,4)
print(o)

#endswith(suffix,begin,end)
u=a.endswith('o',o,6)
print(u)
#startswith(prefix,begin,end)
n=a.startswith('h',0,2)
print(n)

#find(str,begin,end)
f=a.find('e',0,5)
print(f)

#index(str,begin,end)
i=a.index('o',0,5)
print(i)

#rfind(str,begin,end)
r=a.rfind('l',0,5)
print(r)

#rindex(str,begin,end)
ri=a.rindex('l',0,5)
print(ri)

#isalnum()
s=a.isalnum()
print(s)

#isalpha()
sa=a.isalpha()
print(sa)

#isdigit()
sd=a.isdigit()
print(sd)

#islower()
sl=a.islower()
print(sl)

#isupper()
su=a.isupper()
print(su)

#isspace()
ss=a.isspace()
print(ss)

#len(str)
l=len(a)
print(l)

#lower()
lo=a.lower()
print(lo)

#upper()
up=a.upper()
print(up)                                                                                                                       

#lstrip()
ls=a.lstrip()
print(ls)

#rstrip()
rs=a.rstrip()
print(rs)

#strip()
st=a.strip()
print(st)

#ljust(width,fillchar)
lj=a.ljust(10,'s')
print(lj)

#rjust(width,fillchar)
rj=a.rjust(10,'a')
print(rj)


#zfill(n)
n="tiff alice andy"
#z=n.zfill(20)
#print(z)

#max(str):highest ASCII value
m=max(a)
print(m)

#min()
mi=min(a)
print(mi)

#replace(old,new)
r=a.replace('h','y')
print(r)

#title
t="hello my friend"
h=t.title()
print(h)

#enumerate()
e=enumerate(t)
print(e)
