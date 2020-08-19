'''
어떤 양의 정수 X의 각 자리가 등차수열을 이룬다면, 그 수를 한수라고 한다.
등차수열은 연속된 두 개의 수의 차이가 일정한 수열을 말한다.
N이 주어졌을 때, 1보다 크거나 같고, N보다 작거나 같은 한수의 개수를 출력하는 프로그램을 작성하시오.
첫째 줄에 1,000보다 작거나 같은 자연수 N이 주어진다.
'''

def hansu(n):
    list_n = list(map(int, str(n)))
    diff = list_n[0] - list_n[1]
    for i in range(1, len(list_n)-1):
        if diff is not list_n[i] - list_n[i+1]:
            return False
    return True

import sys
N = int(sys.stdin.readline())
if N < 100:
    print(N)
    exit()
cnt = 99
for n in range(111, N+1):
    if hansu(n):
        cnt += 1
print(cnt)