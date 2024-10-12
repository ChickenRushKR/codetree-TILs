from collections import deque
def main():
    L, Q = map(int, input().split(' '))
    cmds = [input().split(' ') for q in range(Q)]
    table = deque()
    people = {}
    sushi_names = []
    timestack = [0]

    def process(t):
        while timestack[-1] < t:
            for name in list(people.keys()):
                if people[name][0] <= t:
                    eat = 0
                    for idx in range(len(table)):
                        if table[idx-eat][2] == name:
                            curpos = (table[idx-eat][1] + t - table[idx-eat][0]) % L
                            if people[name][1] == curpos:
                                people[name][2] -= 1
                                del table[idx-eat]
                                eat += 1
                                if people[name][2] == 0:
                                    people.pop(name)
                                    break
            t -= 1

    for cmd in cmds:
        if cmd[0] == '100':
            t, x, name = int(cmd[1]), int(cmd[2]), cmd[3]
            sushi_names.append(name)
            table.append([t, x, name])
            if len(timestack) == 0:
                timestack.append(t-1)
        elif cmd[0] == '200':
            t, x, name, n = int(cmd[1]), int(cmd[2]), cmd[3], int(cmd[4])
            people[name] = [t, x, n]
        else:
            t = int(cmd[1])
            process(t)
            print(len(people.keys()), len(table))
            timestack.append(t)

    
if __name__ == '__main__':
    main()