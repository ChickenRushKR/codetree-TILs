def main():
    R, C, K = map(int, input().split(' '))
    gollems = [list(map(int, input().split(' '))) for k in range(K)]
    board = [[0] * C for r in range(R+3)]

    di = [-1, 0, 1, 0, 0]
    dj = [0, 1, 0, -1, 0]

    max_score = 0

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

    def mov_pos(ci, cj, new_ci, new_cj, direction, n_of_g):
        di = [-1, 0, 1, 0, 0]
        dj = [0, 1, 0, -1, 0]
        for d in range(5):
            newi, newj = ci+di[d], cj+dj[d]
            board[newi][newj] = 0

        for d in range(5):
            newi, newj = new_ci+di[d], new_cj+dj[d]
            board[newi][newj] = n_of_g
        board[new_ci + di[direction]][new_cj + dj[direction]] = n_of_g * 1000
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

    def get_max(ci, cj, visited):
        nonlocal max_score
        if ci not in range(R+3) or cj not in range(C):
            return
        visited[ci][cj] = 1
        max_score = max(max_score, ci)
        for k in range(4):
            newi = ci + di[k]
            newj = cj + dj[k]
            if newi not in range(len(board)) or newj not in range(len(board[0])):
                continue
            if visited[newi][newj] == 0 and board[newi][newj] != 0:
                if board[ci][cj] >= 1000 :
                    visited[newi][newj] = 0
                    get_max(newi, newj, visited)
                elif board[ci][cj] == board[newi][newj] or board[ci][cj]*1000 == board[newi][newj]:
                    visited[newi][newj] = 0
                    get_max(newi, newj, visited)
        return

    score = 0
    n_of_g = 0
    for idx, gollem in enumerate(gollems):
        # first_check
        ci, cj = 1, gollem[0]-1
        direction = gollem[1]
        n_of_g += 1
        if check_pos(ci, cj) == False:
            board = [[0] * C for r in range(R+3)]
            continue
        else:
            for k in range(5):
                board[ci+di[k]][cj+dj[k]] = n_of_g
            board[ci+di[direction]][cj+dj[direction]] = n_of_g * 1000
        while True:
            if is_down(ci, cj):
                ci, cj, direction = mov_pos(ci, cj, ci+1, cj, direction, n_of_g)
                continue
            elif is_south(ci, cj):
                direction -= 1
                if direction == -1:
                    direction = 3
                ci, cj, direction = mov_pos(ci, cj, ci+1, cj-1, direction, n_of_g)
            elif is_east(ci, cj):
                direction += 1
                if direction == 4:
                    direction = 0
                ci, cj, direction = mov_pos(ci, cj, ci+1, cj+1, direction, n_of_g)
            else:
                if ci < 4:
                    board = [[0] * C for r in range(R+3)]
                    n_of_g = 0
                    break
                outi, outj = ci + di[direction], cj + dj[direction]
                visited = [[0] * C for r in range(R+3)]
                get_max(ci, cj, visited)
                score += (max_score + 1 - 3)
                max_score = 0
                break
    
    print(score)
            
        

if __name__ == '__main__':
    main()