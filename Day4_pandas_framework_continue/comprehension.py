n=int(input("Enter the number : "))
l=[]
print("enter words for list comprehension:")
for i in range(n):
    s=input().strip()
    l.append(s)
c=input("enter character : ")
# print(c,l)
g= ([i for i in l if c in i])
print(*g)
