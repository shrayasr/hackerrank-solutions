N,M = map(int, raw_input().split())

sumJars = 0
for i in xrange(0,M):
    a,b,k = map(int, raw_input().split())

    sumJars += ((b-a)+1) * k

print sumJars/N
