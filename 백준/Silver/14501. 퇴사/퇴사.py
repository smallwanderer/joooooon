import copy
N = int(input())

def binary_tree():
  result = {0: 0}

  for i in range(N):
    T, P = map(int, input().split())
    T += i

    if T > N:
      continue

    temp = copy.deepcopy(result)
    for key, val in temp.items():
      if key <= i:
        if T in result.keys():
          result[T] = max(result[T], val+P)
        else:
          result[T] = val+P

  print(result[max(result, key=result.get)])
  
binary_tree()