import networkx as nx
import heapq

# Використовуємо граф, створений у першому завданні
city_network = nx.Graph()

# Додаємо вузли та ребра з вагами
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

# Реалізація алгоритму Дейкстри
def dijkstra(graph, start):
    distances = {node: float('inf') for node in graph.nodes}  # Ініціалізуємо відстані до всіх вузлів як нескінченність
    distances[start] = 0  # Відстань до початкового вузла = 0
    priority_queue = [(0, start)]  # Черга з пріоритетом, ініціалізована початковим вузлом
    
    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)  # Витягуємо вузол з мінімальною відстанню
        
        if current_distance > distances[current_node]:
            continue
        
        for neighbor, attributes in graph[current_node].items():
            weight = attributes['weight']
            distance = current_distance + weight
            
            # Якщо знайдена коротша відстань, оновлюємо і додаємо в чергу
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))
    
    return distances

# Знаходимо найкоротші шляхи для кожної вершини
shortest_paths = {}
for node in city_network.nodes:
    shortest_paths[node] = dijkstra(city_network, node)

# Виведення результатів
for start_node, paths in shortest_paths.items():
    print(f"Найкоротші шляхи від {start_node}:")
    for destination, distance in paths.items():
        print(f"  До {destination}: {distance}")
    print()

''' Пояснення коду
Ініціалізація графа з вагами: Вершини та ваги на ребрах додаються так, як у попередніх завданнях.

Алгоритм Дейкстри: Використовується пріоритетна черга для зберігання вузлів, які потрібно обробити. 
Для кожного вузла алгоритм перевіряє, чи можна знайти коротший шлях до його сусідів. 
Якщо так, то оновлює відстань і додає вузол до черги.

Знаходження шляхів для всіх вершин: Функція dijkstra викликається для кожної вершини графа, 
щоб знайти найкоротші шляхи до всіх інших вершин.'''