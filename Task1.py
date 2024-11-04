# ** Завдання 1 **  
# Створення графу за допомогою бібліотеки networkX для моделювання певної реальної мережі 
# (наприклад, транспортної мережі міста, соціальної мережі, інтернет-топології). 
# Запустіть в терміналі: pip install networkx

import networkx as nx
import matplotlib.pyplot as plt

# Створення графа транспортної мережі міста
city_network = nx.Graph()

# Додавання вузлів (наприклад, станцій або зупинок)
nodes = ["Station A", "Station B", "Station C", "Station D", "Station E", "Station F", "Station G"]
city_network.add_nodes_from(nodes)

# Додавання ребер з вагами (наприклад, відстані між станціями)
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

# Візуалізація графа
plt.figure(figsize=(10, 7))
pos = nx.spring_layout(city_network)  # обираємо вигляд розташування вузлів
nx.draw(city_network, pos, with_labels=True, node_color="skyblue", node_size=1000, edge_color="gray")
labels = nx.get_edge_attributes(city_network, 'weight')
nx.draw_networkx_edge_labels(city_network, pos, edge_labels=labels)
plt.title("Транспортна мережа міста")
plt.show()

# Аналіз основних характеристик графа
print("Основні характеристики транспортної мережі:")
print(f"Кількість вузлів (станцій): {city_network.number_of_nodes()}")
print(f"Кількість ребер (сполучень): {city_network.number_of_edges()}")

# Ступінь вузлів
degrees = dict(city_network.degree())
print("Ступінь кожного вузла (кількість з'єднань):")
for node, degree in degrees.items():
    print(f"{node}: {degree}")

# Середній ступінь вузлів
average_degree = sum(degrees.values()) / city_network.number_of_nodes()
print(f"Середній ступінь вузла: {average_degree:.2f}")

# Середня довжина шляху (якщо граф зв'язний)
if nx.is_connected(city_network):
    avg_path_length = nx.average_shortest_path_length(city_network)
    print(f"Середня довжина найкоротшого шляху: {avg_path_length:.2f}")
else:
    print("Граф не є зв'язним, середня довжина шляху не обчислюється.")

# Коефіцієнт кластеризації
clustering_coeff = nx.average_clustering(city_network)
print(f"Середній коефіцієнт кластеризації: {clustering_coeff:.2f}")

''' *Пояснення коду:*
Створення графа: 
Ми створили граф, який представляє транспортну мережу міста. 
Кожна станція є вузлом, а відстань між станціями — вагою ребра.

Візуалізація графа: 
Використовуємо matplotlib для графічного зображення графа 
з позначенням станцій та відстаней між ними.

Аналіз характеристик:
Кількість вузлів та ребер: Аналізуємо загальну кількість станцій і сполучень.
Ступінь вузлів: Показуємо кількість сполучень кожної станції.
Середній ступінь вузла: Обчислюємо середній ступінь.
Середня довжина шляху: Якщо граф зв'язний, визначаємо середню довжину найкоротшого шляху.
Коефіцієнт кластеризації: Обчислюємо середній коефіцієнт кластеризації, 
який показує рівень "згуртованості" станцій.'''
