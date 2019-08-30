a = int(input('enter no. of bottles'))
h = list(map(int,input().split(' ')))
print(max([h.count(i) for i in h]))
