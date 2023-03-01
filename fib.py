f0=0
f1=1
print(f0,end=" ")
print(f1,end=" ")

for fn in range(2,15):
    fn=f0+f1
    print(fn,end=" ")
    f0=f1
    f1=fn
