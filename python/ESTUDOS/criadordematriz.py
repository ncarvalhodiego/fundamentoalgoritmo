import os, platform, random, math
os.system("cls")

n = int(input(">> "))

for i in range(1,n+1):
    for j in range(1,n+1):
        x = str("%d,%d" %(i,j))
        print("%5s" % x, end=" ")
    print()