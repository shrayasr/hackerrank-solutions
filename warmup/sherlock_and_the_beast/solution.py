def generate(digits):

    nthrees=0

    while digits >= 0:

        if digits % 3 == 0:
            return ('5' * digits + '3' * nthrees)

        digits -= 5
        nthrees += 5

    return -1


T = int(raw_input())

for i in xrange(0,T):

    digits = int(raw_input())

    print generate(digits)
