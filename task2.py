import collections
from collections import Counter

numShoes = int(raw_input())
shoes = Counter(map(int, raw_input().split()))
numCust = int(raw_input())

income = 0

for i in range(numCust):
    size, price = map(int, raw_input().split())
    if shoes[size]: 
        income += price
        shoes[size] -= 1

print income
