def check(l):

    v=True
    k=True
    n = int(l)
    for i in range(2,n):
        if(n%i==0):
            v=False
    n = str(l)
    rev = str(n)[::-1]
    if str(n) == rev:
        k = True
    else:
        k = False
    if (v):
        print("Given input is prime")
    else:
        print("Given input is not prime")
    if (k):
        print("Given input is a palindrome")
    else:
        print("Given input is not a palindrome")
x=1
while(x!=0):
    l = input('enter your desired value: ')

    m=l.isdigit()
    if(m):
        check(l)
        break
    else:
        l=input("enter your desired value: ")




