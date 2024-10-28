from collections import deque
A = input()
B = input()
queue = deque(B)
idx = 0
cnt = 0
while queue:
    word = queue.popleft()
    while A[idx] != word:
        idx += 1
        if idx >= len(A):
            idx = 0
    cnt += 1
    idx += 1
    if idx >= len(A):
        idx = 0
print(cnt)