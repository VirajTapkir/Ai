# Implementing BFS algorithm
graph = {
    'A' :['B','C'],
    'B':['E','F'],
    'C':['G','H'],
    'E':['I'],
    'F':[],
    'G':['J'],
    'H':['K'],
    'I':[],
    'J':[],
    'K':[]
}
visited = []
queue = []

def BFS(graph,visited,Node):
    visited.append(Node)
    queue.append(Node)

    while queue:
        m = queue.pop(0)
        print(m,end=" ")

        for item in graph[m]:
            if item not in visited:
                visited.append(item)
                queue.append(item)


print("BFS result will be: ")
BFS(graph,visited,'A')

