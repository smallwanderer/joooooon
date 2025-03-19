
def sliding_window_12847(arr, key):
  p1, p2, current_sum = 0, key-1, sum(arr[:key])
  current_max = current_sum
  while p2 < len(arr)-1:
    p2 += 1
    current_sum += arr[p2]
    current_sum -= arr[p1]
    p1 += 1
    current_max = max(current_max, current_sum)
  return current_max

n, key = map(int, input().split())
arr = list(map(int, input().split()))
print(sliding_window_12847(arr, key))