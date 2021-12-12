with open("day12.txt") as f:
    lines = [line.strip().split("-") for line in f]

count = 0
def explore(node, visited, smallTwice):
    if node == "end":
        global count
        count += 1
        return

    c1 = [line[1] for line in lines if line[0] == node]
    c2 = [line[0] for line in lines if line[1] == node]
    c1.extend(c2)
    connections = [conn for conn in c1 if ((conn.lower() == conn and conn != "start" and (conn not in visited or not smallTwice)) or (conn.upper() == conn))]
    for conn in connections:
        newSmallTwice = smallTwice if smallTwice else (conn.lower() == conn and conn in visited)
        visited.append(conn)
        explore(conn, visited, newSmallTwice)
        visited.pop()
    
    return

explore("start", ["start"], False)
print(count)
    
