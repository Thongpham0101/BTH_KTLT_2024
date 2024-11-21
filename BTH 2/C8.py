print("PHẠM MẠNH THỐNG")
print("MSV:235752021610071")
a,b=1,2
c=0
while b<=40:
    a,b=b,a+b
    print(a,end=" ")
    if a%2==0:
        c=c+a
print("Tổng của các số chẵn trong dãy fibonanci là: ",c)
