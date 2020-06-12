#YASHODEEP PAWAR USERID:2470
def sum_series(n):
  if n < 1:
    return 0
  else:
    return n + sum_series(n - 2)

n=int(input())
print(sum_series(n))



