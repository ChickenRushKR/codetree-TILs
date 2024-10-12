from collections import deque
def main():
    K, M = map(int, input().split(' '))
    board = [list(map(int, input().split(' '))) for _ in range(5)]
    written = list(map(int, input().split(' ')))
    values = deque(written)

    def circular(b, ci, cj, angle):
        # if ci not in range(1,4) or cj not in range(1,4):
            # return -1
        for _ in range(angle):
            b[ci-1][cj-1], b[ci-1][cj], b[ci-1][cj+1], b[ci][cj+1], b[ci+1][cj+1], b[ci+1][cj], b[ci+1][cj-1], b[ci][cj-1] = \
            b[ci+1][cj-1], b[ci][cj-1], b[ci-1][cj-1], b[ci-1][cj], b[ci-1][cj+1], b[ci][cj+1], b[ci+1][cj+1], b[ci+1][cj]
            # b[ci-1][cj-1], b[ci-1][cj], b[ci-1][cj+1], b[ci][cj+1], b[ci+1][cj+1], b[ci+1][cj], b[ci+1][cj-1], b[ci][cj-1] = \
            # b[ci][cj-1], b[ci-1][cj-1], b[ci-1][cj], b[ci-1][cj+1], b[ci][cj+1], b[ci+1][cj+1], b[ci+1][cj], b[ci+1][cj-1]
        return b

    def calculate(b):
        res = []
        for i in range(5):
            for j in range(5):
                if b[i][j] != 0:
                    bcopy = [b_[:] for b_ in b]
                    area, newboard = bfs(bcopy, i, j)
                    if area >= 3:
                        res.append(area)
                        b = newboard
        return sum(res), b
    
    def bfs(b, i, j):
        value = b[i][j]
        visit = [[0]* 5 for _ in range(5)]
        cnt = 0
        di = [-1,1,0,0]
        dj = [0,0,-1,1]
        queue = deque([[i,j]])
        while queue:
            i, j = queue.popleft()
            visit[i][j] = 1
            b[i][j] = 0
            cnt += 1
            for k in range(4):
                newi, newj = i + di[k], j + dj[k]
                if newi not in range(5) or newj not in range(5):
                    continue
                if b[newi][newj] == value and visit[newi][newj] == 0:
                    queue.append([newi,newj])
                    visit[newi][newj] = 1
        return cnt, b
    # def dfs(b, v, i, j, cnt):
    #     if i not in range(5) or j not in range(5):
    #         return 0, b
    #     elif b[i][j] != v:
    #         return 0, b
    #     else:
    #         if b[i][j] == v:
    #             b[i][j] = 0
    #             cnt += 1
    #             cnt += dfs(b, v, i-1, j, cnt)[0]
    #             cnt += dfs(b, v, i+1, j, cnt)[0]
    #             cnt += dfs(b, v, i, j-1, cnt)[0]
    #             cnt += dfs(b, v, i, j+1, cnt)[0]
    #             return cnt, b
        
    def fill_values():
        for j in range(5):
            for i in range(4,-1,-1):
                if values:
                    if board[i][j] == 0:
                        board[i][j] = values.popleft()
                else:
                    return
    # operation: value, angle, col, row
    # operations = [
        # [0,1,1,1],
        # [0,2,1,1],
        # [0,3,1,1],
        # [0,1,2,1],
        # [0,2,2,1],
        # [0,3,2,1],
        # ...
    # ] 
    operations = [[0] * 4 for _ in range(27)]
    for i in range(3):
        for j in range(3):
            for k in range(3):
                operations[i*3*3+j*3+k][1] = k+1
                operations[i*3*3+j*3+k][2] = j+1
                operations[i*3*3+j*3+k][3] = i+1
    # print(operations)
    score = [0 for k in range(K)]
    for k in range(K):
        ocopy = [o[:] for o in operations]
        for o in ocopy:
            bcopy = [b[:] for b in board]
            bcopy = circular(bcopy, o[3], o[2], o[1])
            o[0], bcopy = calculate(bcopy)
        ocopy.sort(key=lambda x:(-x[0], x[1],x[2],x[3]))
        if ocopy[0][0] > 0:
            board = circular(board, ocopy[0][3], ocopy[0][2], ocopy[0][1])
            _, board = calculate(board)
            score[k] += ocopy[0][0]
        else:
            break
        while True:
            fill_values()
            chainscore, board = calculate(board)
            if chainscore != 0:
                score[k] += chainscore
            else:
                break
    for s in score:
        if s == 0:
            break
        else:
            print(s, end=' ')
        

if __name__ == '__main__':
    main()