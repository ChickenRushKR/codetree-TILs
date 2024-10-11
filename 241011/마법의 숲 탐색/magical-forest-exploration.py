# 0: empty
# 1: gollem
# 2: wjdfud
# 3: out
from collections import deque

def main():
    R, C, K = map(int, input().split(' '))
    gollems = [list(map(int, input().split(' '))) for k in range(K)]
    board = [[0] * C for r in range(R+3)]

    di = [-1, 0, 1, 0, 0]
    dj = [0, 1, 0, -1, 0]


    def check_pos(ci, cj):
        di = [-1, 0, 1, 0, 0]
        dj = [0, 1, 0, -1, 0]
        movable = True
        for d in range(1,5):
            newi, newj = ci+di[d], cj+dj[d]
            if board[newi][newj] != 0:
                movable = False
                break
        return movable

    def mov_pos(ci, cj, new_ci, new_cj, direction):
        di = [-1, 0, 1, 0, 0]
        dj = [0, 1, 0, -1, 0]
        for d in range(5):
            newi, newj = ci+di[d], cj+dj[d]
            board[newi][newj] = 0

        for d in range(5):
            newi, newj = new_ci+di[d], new_cj+dj[d]
            board[newi][newj] = 1
        board[new_ci][new_cj] = 2
        board[new_ci + di[direction]][new_cj + dj[direction]] = 3
        
        return new_ci, new_cj, direction


    def is_down(ci, cj):
        if ci+2 >= R+3:
            return False
        if board[ci+2][cj] == 0 and board[ci+1][cj-1] == 0 and board[ci+1][cj+1] == 0:
            return True
        else:
            return False
        
    def is_south(ci, cj):
        if cj-2 < 0 or ci+2 >= R+3:
            return False
        if board[ci-1][cj-1] == 0 and board[ci][cj-2] == 0 and board[ci+1][cj-1] == 0:
            if board[ci+1][cj-2] == 0 and board[ci+2][cj-1] == 0:
                return True
        return False

    def is_east(ci, cj):
        if cj+2 >= C or ci+2 >= R+3:
            return False
        if board[ci-1][cj+1] == 0 and board[ci][cj+2] == 0 and board[ci+1][cj+1] == 0:
            if board[ci+1][cj+2] == 0 and board[ci+2][cj+1] == 0:
                return True
        return False

    def get_max_i(ci, cj):
        maxi = 0
        di, dj = [-1, 1, 0, 0], [0, 0, -1, 1]
        visited = [[0] * len(board[0]) for _ in range(len(board))]
        queue = deque([[ci, cj]])
        while queue:
            ij = queue.popleft()
            visited[ij[0]][ij[1]] = 1
            maxi = max(maxi, ij[0])
            for k in range(4):
                newi = ij[0] + di[k]
                newj = ij[1] + dj[k]
                if newi not in range(len(board)) or newj not in range(len(board[0])):
                    continue
                if visited[newi][newj] == 0 and board[newi][newj] != 0:
                    visited[newi][newj] = 0
                    queue.append([newi, newj])
        return maxi

    score = 0
    for idx, gollem in enumerate(gollems):
        # first_check
        ci, cj = 1, gollem[0]-1
        direction = gollem[1]
        if check_pos(ci, cj) == False:
            board = [[0] * C for r in range(R+3)]
            continue
        else:
            for k in range(5):
                board[ci+di[k]][cj+dj[k]] = 1
            board[ci][cj] = 2
            board[ci+di[direction]][cj+dj[direction]] = 3
        while True:
            if is_down(ci, cj):
                ci, cj, direction = mov_pos(ci, cj, ci+1, cj, direction)
                continue
            elif is_south(ci, cj):
                direction -= 1
                if direction == -1:
                    direction = 3
                ci, cj, direction = mov_pos(ci, cj, ci+1, cj-1, direction)
            elif is_east(ci, cj):
                direction += 1
                if direction == 4:
                    direction = 0
                ci, cj, direction = mov_pos(ci, cj, ci+1, cj+1, direction)
            else:
                flag = False
                for i in range(3):
                    if sum(board[i]) != 0:
                        flag = True
                if flag:
                    board = [[0] * C for r in range(R+3)]
                    break
                outi, outj = ci + di[direction], cj + dj[direction]
                conn_flag = False
                for i in range(4):
                    newi, newj = outi+di[i], outj+dj[i]
                    if newi not in range(R+3) or newj not in range(C):
                        continue
                    elif board[newi][newj] == 1:
                        conn_flag = True
                
                board[ci][cj] = 1
                board[outi][outj] = 1
                if conn_flag:
                    score += (get_max_i(outi, outj) + 1 - 3)
                else:
                    score += (ci + 1 + 1 - 3)
                break
    
    print(score)
            
        

if __name__ == '__main__':
    main()