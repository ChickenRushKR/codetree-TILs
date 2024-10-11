class revenue:
    def __init__(self, id_, money, dst, distance):
        self.id = id_
        self.money = money
        self.dst = dst
        self.distance = distance
        self.profit = -1
    def __lt__(self, other):
        return self.profit < other.profit
    

def get_smallest(visit, cost):
    min_val = 100000
    idx = 0
    for i in range(len(visit)):
        if cost[i] < min_val and not visit[i]:
            min_val = cost[i]
            idx = i
    return idx

def dijkstra(graph, src):
    visit = [0] * len(list(graph.keys()))
    cost = [99999] * len(list(graph.keys()))
    cost[src] = 0
    visit[src] = 1
    for i in graph[src]:
        cost[i[0]] = i[1]
    
    for _ in range(len(visit)-1):
        idx = get_smallest(visit, cost)
        visit[idx] = 1

        for j in graph[idx]:
            if cost[j[0]] > cost[idx] + j[1]:
                cost[j[0]] = cost[idx] + j[1]
    return cost

def main():
    n_of_cmds = int(input())
    cmds = [list(map(int, input().split(' '))) for n in range(n_of_cmds)]
    graph = {}
    revenues = []
    recent_distances = []
    for cmd in cmds:
        if cmd[0] == 100: # 100 n m v_1 u_1 w_1 v_2 u_2 w_2 ... v_m u_m w_m
            for n in range(cmd[1]):
                graph[n] = []
            for m in range(0, cmd[2]*3, 3):
                graph[cmd[m+3]].append((cmd[m+4], cmd[m+5]))
                graph[cmd[m+4]].append((cmd[m+3], cmd[m+5]))
            for n in range(cmd[1]):
                graph[n] = list(set(graph[n]))
                graph[n].sort(key=lambda x:(x[1], x[0]))
            recent_distances = dijkstra(graph, 0)
        elif cmd[0] == 200: # 200 id revenue dest
            newrevenue = revenue(cmd[1], cmd[2], cmd[3], -1)
            newrevenue.distance = recent_distances[newrevenue.dst]
            newrevenue.profit = newrevenue.money - newrevenue.distance
            revenues.append(newrevenue)
        elif cmd[0] == 300: # 300 id
            for i in range(len(revenues)):
                if revenues[i].id == cmd[1]:
                    revenues.pop(i)
                    break
        elif cmd[0] == 400:
            if len(revenues) == 0:
                print(-1)
                continue
            revenues.sort(key=lambda x:(-x.profit, x.id))
            if revenues[0].profit >= 0:
                print(revenues[0].id)
                revenues.pop(0)
            else:
                print(-1)
        else:
            recent_distances = dijkstra(graph, cmd[1])
            for r in revenues:
                r.distance = recent_distances[r.dst]
                r.profit = r.money - r.distance
            

if __name__ == '__main__':
    main()