T = int(raw_input())

K = []
for i in xrange(0, T):
    K.append(float(raw_input()))

for k in K:

    l = k/2
    r = k-l
    print int(l*r)
