n = int(input("Enter a number: "))
i=1
while i<=n:
    if i==0:
        n=1
    else:
        n=n*i
        i=i+1
print(n)