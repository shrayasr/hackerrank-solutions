def get_testcases():

  T = int(raw_input())

  N = []
  for i in xrange(0,T):
    N.append(int(raw_input()))

  return N

def print_heights(N):

  for n in N:

    height = 1
    for i in xrange(1,n+1):
      if i==0:
        continue
      elif i%2 == 0:
        height += 1
      else:
        height *= 2

    print height

def main():

  N = get_testcases()
  print_heights(N)

if __name__ == "__main__":
  main()
