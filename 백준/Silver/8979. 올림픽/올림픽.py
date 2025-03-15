import sys

n, k = map(int, sys.stdin.readline().strip().split())
country = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(n)]
country.sort(key=lambda x:(x[1], x[2], x[3]), reverse=True)

rank = 1
for c_idx in range(1,n):
  if country[c_idx][1:] != country[c_idx-1][1:]:
    rank += 1
  if country[c_idx][0] == k:
    sys.stdout.write(f"{rank}")
    break