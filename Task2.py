import networkx as nx
from collections import deque

# Використовуємо граф, створений у першому завданні
city_network = nx.Graph()

# Додаємо вузли та ребра (як у першому завданні)
nodes = ["Station A", "Station B", "Station C", "Station D", "Station E", "Station F", "Station G"]
city_network.add_nodes_from(nodes)
edges = [
    ("Station A", "Station B", 5),
    ("Station A", "Station C", 7),
    ("Station B", "Station D", 3),
    ("Station C", "Station D", 4),
    ("Station C", "Station E", 8),
    ("Station D", "Station F", 6),
    ("Station E", "Station F", 2),
    ("Station E", "Station G", 10),
    ("Station F", "Station G", 5)
]
city_network.add_weighted_edges_from(edges)

# Функція для виконання DFS-пошуку шляху
def dfs(graph, start, goal, path=None, visited=None):
    if path is None:
        path = []
    if visited is None:
        visited = set()
    
    path.append(start)
    visited.add(start)
    
    if start == goal:
        return path
    
    for neighbor in graph.neighbors(start):
        if neighbor not in visited:
            result = dfs(graph, neighbor, goal, path.copy(), visited.copy())
            if result is not None:
                return result
    return None

# Функція для виконання BFS-пошуку шляху
def bfs(graph, start, goal):
    queue = deque([[start]])
    visited = set([start])
    
    while queue:
        path = queue.popleft()
        node = path[-1]
        
        if node == goal:
            return path
        
        for neighbor in graph.neighbors(node):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(path + [neighbor])
    return None

# Виконуємо пошук шляхів від "Station A" до "Station G"
start = "Station A"
goal = "Station G"

dfs_path = dfs(city_network, start, goal)
bfs_path = bfs(city_network, start, goal)

# Виведення результатів
print("Шлях DFS:", dfs_path)
print("Шлях BFS:", bfs_path)

# Аналіз та порівняння шляхів
with open("README.md", "w") as file:
    file.write("# Порівняння алгоритмів DFS і BFS для пошуку шляху\n\n")
    file.write("### Результати:\n")
    file.write(f"- Шлях, знайдений алгоритмом DFS від {start} до {goal}: {dfs_path}\n")
    file.write(f"- Шлях, знайдений алгоритмом BFS від {start} до {goal}: {bfs_path}\n\n")
    file.write("### Порівняння та пояснення:\n")
    file.write("DFS (пошук у глибину) заглиблюється в граф до максимальної глибини перед тим, як повернутися назад. Це означає, що DFS знаходить шлях, який може бути не найкоротшим, але зосереджується на першому можливому шляху, глибоко досліджуючи граф.\n")
    file.write("BFS (пошук у ширину) відвідує всі сусідні вузли поточного рівня, перш ніж перейти на наступний рівень. Це забезпечує знаходження найкоротшого шляху в графі.\n\n")
    file.write("**Висновок:** BFS забезпечує оптимальний шлях за кількістю кроків, тоді як DFS може знайти інший шлях, залежно від структури графа. У випадках, коли граф має багато шляхів, BFS часто знаходить коротший шлях, а DFS може застрягнути в одній гілці.\n")

'''Пояснення коду
Алгоритм DFS: Реалізує рекурсивний пошук у глибину, додаючи поточний вузол до шляху та переходячи 
до непереглянутих сусідів. Це заглиблюється в граф до кінця шляху, що може не бути найкоротшим.

Алгоритм BFS: Виконує пошук у ширину, використовуючи чергу deque. Кожен сусід додається в чергу, 
що забезпечує знаходження найкоротшого шляху за кількістю кроків.

Висновки та пояснення: У README.md документуються результати та порівняння обох алгоритмів. 
DFS зазвичай не забезпечує найкоротшого шляху, особливо в складних графах, 
тоді як BFS знаходить найкоротший шлях для незваженого графа.

Результат роботи
Результати пошуку шляхів і висновки зберігаються у файлі README.md, 
де порівнюються знайдені шляхи та пояснюється різниця між алгоритмами DFS і BFS.'''