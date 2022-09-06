"[A] - Letter in correct place, (B) - Letter exists but it is in a wrong place, {C} - Letter does not exist."
from random import*
z,g,p=choice([*open('i')]),1,print
while g<6and(y:=input()[:5])!=z[:5]:p(*map(lambda a,b:(h:="{([})]"[(a==b)+(a in z):])[0]+a+h[3],y,z));g+=1
p(f"{g-1}/5")