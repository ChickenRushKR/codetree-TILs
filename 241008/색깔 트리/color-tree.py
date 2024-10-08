class node:
    def __init__(self,  m_id, p_id, color, max_depth):
        self.m_id = m_id
        self.p_id = p_id
        self.color = color
        self.max_depth = max_depth
        self.parent = None
        self.heads = []
        self.childs = []

    def search(self, m_id):
        if len(self.heads) == 0:
            return None
        else:
            for head in self.heads:
                queue = [head]
                while len(queue) != 0:
                    ptr = queue.pop(0)
                    if ptr.m_id == m_id:
                        break
                    else:
                        for c in ptr.childs:
                            queue.append(c)
        return ptr

    def insert_node(self, m_id, p_id, color, max_depth):
        if p_id == -1:
            newnode = node(m_id, p_id, color, max_depth)
            self.heads.append(newnode)
            return 1
        else:
            target = self.search(p_id)
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
                return 1
            else:
                return 0

    def color_change(self, m_id, color):
        target = self.search(m_id)
        queue = [target]
        while len(queue) != 0:
            ptr = queue.pop(0)
            ptr.color = color
            if len(ptr.childs) == 0:
                continue
            else:
                for c in ptr.childs:
                    queue.append(c)
        return 0
        
    def color_view(self, m_id):
        target = self.search(m_id)
        print(target.color)

    def score_view(self):
        for head in self.heads:
            queue = [head]
            score = 0
            while len(queue) != 0:
                ptr = queue.pop(0)

                subtreeq = [ptr]
                colors = []
                while len(subtreeq) != 0:
                    ptr2 = subtreeq.pop(0)
                    if ptr2.color not in colors:
                        colors.append(ptr2.color)
                    if len(ptr2.childs) == 0:
                        continue
                    else:
                        for c in ptr2.childs:
                            subtreeq.append(c)
                score += (len(colors) ** 2)

                if len(ptr.childs) == 0:
                    continue
                else:
                    for c in ptr.childs:
                        queue.append(c)
        print(score)
        

def main():
    Q = int(input())
    commands = []
    for _ in range(Q):
        commands.append(input())

    root = node(m_id=-1, p_id=-1, color=-1, max_depth=999)
    
    for command in commands:
        op = int(command.split(' ')[0])
        if op == 100:
            _, m_id, p_id, color, max_depth = map(str, command.split(' '))
            root.insert_node(int(m_id), int(p_id), int(color), int(max_depth))
        elif op == 200:
            _, m_id, color = map(str, command.split(' '))
            root.color_change(int(m_id), int(color))
        elif op == 300:
            _, m_id = map(str, command.split(' '))
            root.color_view(int(m_id))
        elif op == 400:
            root.score_view()


if __name__ == '__main__':
    main()