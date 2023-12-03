import sys
input = sys.stdin.readline

N = list(map(str ,input().split()))
M = int(input())
num = list(map(int ,input().split()))

tmp = [i for i in range(10) if i not in num]

print(tmp)