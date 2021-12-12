with open("day12.txt") as f:
    lines = [line.strip().split("-") for line in f]

count = 0
def explore(node, visited):
    if node == "end":
        global count
        count += 1
        return

    c1 = [line[1] for line in lines if line[0] == node]
    c2 = [line[0] for line in lines if line[1] == node]
    c1.extend(c2)
    connections = [conn for conn in c1 if (conn.lower() == conn and conn not in visited) or conn.upper() == conn]
    for conn in connections:
        visited.append(conn)
        explore(conn, visited)
        visited.pop()
    
    return

explore("start", ["start"])
print(count)
    
