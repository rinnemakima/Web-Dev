#1
x = str(input())
print(x.swapcase())

#2

x = int(input())
sum = 0
n = 0
defas = len(str(abs(x)))
for i in range (defas):
    n = x%10
    sum+=n**2
    x = x//10
print(sum)

#3
#Done in bash