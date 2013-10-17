"""Fibbonacci Generator"""
first=0
second=1
fib=[1,1]
n=1
m=int(raw_input("how many fibbonacci numbers do you want to go up to?"))
while n<m:
    length = len(fib)
    fibBuf=fib[first]+fib[second]

    first=first+1


    second=second+1

    fib.append(fibBuf)
    print fib[length]
    n+=1

