n,m=raw_input().split()
l=raw_input().split()
A=set(raw_input().split())
B=set(raw_input().split())
happiness = 0

for i in l:
    if i in A:
        happiness +=1
    if i in B:
        happiness -=1 
print (happiness)
