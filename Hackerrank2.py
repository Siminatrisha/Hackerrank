n=input()
n=int(n)
if 1<=n<=100 and n%2!=0:
    print('Weird')
elif 2<n<=5 and n%2==0:
    print('Not Weird') 
elif 5<n<=20 and n%2==0:
    print('Weird')    
else:
    print('Not Weird')    