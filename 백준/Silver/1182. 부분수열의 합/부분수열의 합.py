N,S = list(map(int,input().split()))
seq = list(map(int,input().split()))

def sub_seq(index,current_sum,seq,S):
  if index == len(seq):
    return 1 if current_sum == S else 0

  return (sub_seq(index+1,current_sum, seq,S)+sub_seq(index+1,current_sum+seq[index],seq,S))

result = sub_seq(0,0,seq,S)

if S == 0:
  result-=1

print(result)