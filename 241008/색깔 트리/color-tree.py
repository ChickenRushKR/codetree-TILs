#https://www.codetree.ai/training-field/frequent-problems/problems/color-tree/submissions?page=1&pageSize=5
nodes = []
heads = []
class node:
    def __init__(self,  m_id, p_id, color, max_depth):
        self.m_id = m_id
        self.p_id = p_id
        self.color = color
        self.max_depth = max_depth
        self.parent = None
        self.childs = []

def search(m_id):
    global nodes
    for node_ in nodes:
        if node_.m_id == m_id:
            return node_

def insert_node(m_id, p_id, color, max_depth):
    global nodes, heads
    if p_id == -1:
        newnode = node(m_id, p_id, color, max_depth)
        heads.append(newnode)
        nodes.append(newnode)
        return 1
    else:
        # headidx, target = self.search(p_id)
        target = search(p_id)
        newnode = node(m_id, p_id, color, max_depth)
        newnode.parent = target
        ptr = target
        depth = 2
        # while ptr.parent != None:
        while ptr != None:
            if ptr.max_depth < depth:
                depth = -1
                break
            else:
                depth += 1
                ptr = ptr.parent
        if depth != -1:
            newnode.parent.childs.append(newnode)
            nodes.append(newnode)
            return 1
        else:
            return 0

def color_change(m_id, color):
    # headidx, target = self.search(m_id)
    target = search(m_id)
    def recur_color(ptr):
        ptr.color = color
        if len(ptr.childs) == 0:
            return
        else:
            for c in ptr.childs:
                recur_color(c)
    recur_color(target)
    return 0
    
def color_view(m_id):
    # headidx, target = self.search(m_id)
    target = search(m_id)
    print(target.color)

def score_view():
    global nodes
    score = 0
    def recur_color2(ptr, colors):
        colors.append(ptr.color)
        if len(ptr.childs) == 0:
            return colors
        else:
            for c in ptr.childs:
                recur_color2(c, colors)
            return colors
    for node in nodes:
        arr = []
        colors = recur_color2(node, arr)
        score += (len(list(set(colors))) ** 2)
    print(score)
        

def main():
    Q = int(input())
    commands = []
    for _ in range(Q):
        commands.append(input())

    
    for command in commands:
        op = int(command.split(' ')[0])
        if op == 100:
            _, m_id, p_id, color, max_depth = map(str, command.split(' '))
            insert_node(int(m_id), int(p_id), int(color), int(max_depth))
        elif op == 200:
            _, m_id, color = map(str, command.split(' '))
            color_change(int(m_id), int(color))
        elif op == 300:
            _, m_id = map(str, command.split(' '))
            color_view(int(m_id))
        elif op == 400:
            score_view()


if __name__ == '__main__':
    main()