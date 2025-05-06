# HASH TABLE

n, m = map(int, input().split())
pocket_id = dict()
pocket_name = dict()
for i in range(1, n+1):
  name = input()
  # if name[-1].isupper():
  #   name = name[0].upper() + name[1:-1] + name[-1].lower()

  pocket_id[i] = name
  pocket_name[name] = i

for k in range(m):
  question = input()

  if question.isdigit():
    print(pocket_id[int(question)])
  else:
    print(pocket_name[question])