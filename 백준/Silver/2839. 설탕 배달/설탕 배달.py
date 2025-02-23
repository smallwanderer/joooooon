n = int(input())

def sugar_delivery(n):
  result = 0

  while True:
    if n < 0:
      return -1
    if n % 5 == 0:
      result += n // 5
      return result
    n -= 3
    result += 1

print(sugar_delivery(n))