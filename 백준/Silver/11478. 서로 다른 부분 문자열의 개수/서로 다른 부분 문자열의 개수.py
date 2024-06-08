S = input()

cnt = set()

data_length = len(S)

for i in range(data_length):
    for j in range(i+1, data_length+1):
        cnt.add(S[i:j])

print(len(cnt))