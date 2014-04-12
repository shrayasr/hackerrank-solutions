T = int(raw_input())

K = []
for i in xrange(0, T):
    K.append(float(raw_input()))

for k in K:

    maxk=0

    for i in xrange(int((k/2)+1),1,-1):

        j = k - i

        if j*i > maxk:
            maxk = j*i

    print int(maxk)

