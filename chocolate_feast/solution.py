def get_more(chocos, M):

    if (M > chocos):
        return 0

    remaining = chocos - M
    more = 1

    return more + get_more(remaining+more, M)

# Enter your code here. Read input from STDIN. Print output to STDOUT
T = int(raw_input())
for i in range (0,T):
    N,C,M = map(int,raw_input().split())

    answer = 0

    initial_chocos = N/C

    answer = initial_chocos + get_more(initial_chocos, M) 

    print answer
