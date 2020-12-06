mylist=[]
for _ in range(int(input())):
    name = input()
    score = float(input())
    mylist.append([name,score])
first_low=min(b for a,b in mylist)
for a,b in mylist:
    mylist.sort()
    for a,b in mylist:
        if (b==first_low):
            mylist.remove([a,b])
second_low=min(b for a,b in mylist)
for a,b in mylist:
    if (b==second_low):
        print(a)