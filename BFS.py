import dataclasses
from numpy import random
import queue


@dataclasses.dataclass(unsafe_hash=True)
class Vertice:
    name: str
    speciality: str


arr_of_people = []

# 16

specs = ["IT", "BIO", "LIT", "HIS", "CHEM", "MATH", "GEO", "BIO", "LIT", "HIS", "CHEM", "MATH", "GEO", "BIO", "LIT",
         "HIS", "CHEM", "MATH", "GEO"]
for i in range(16):
    temp_spec = specs[random.randint(0, len(specs) - 1)]
    temp_name = ""
    for j in range(random.randint(5, 10)):
        temp_name += chr(random.randint(97, 122))
    arr_of_people.append(Vertice(temp_name, temp_spec))

# 97-122
graph = {}

graph[arr_of_people[0]] = [arr_of_people[1], arr_of_people[2], arr_of_people[3], arr_of_people[4]]
graph[arr_of_people[1]] = [arr_of_people[5], arr_of_people[6], arr_of_people[7]]
graph[arr_of_people[2]] = [arr_of_people[7], arr_of_people[8]]
graph[arr_of_people[3]] = [arr_of_people[13], arr_of_people[15]]
graph[arr_of_people[4]] = [arr_of_people[5], arr_of_people[9], arr_of_people[15]]
graph[arr_of_people[5]] = [arr_of_people[9], arr_of_people[10]]
graph[arr_of_people[6]] = [arr_of_people[10]]
graph[arr_of_people[7]] = []
graph[arr_of_people[8]] = [arr_of_people[14]]
graph[arr_of_people[9]] = []
graph[arr_of_people[10]] = []
graph[arr_of_people[11]] = [arr_of_people[12]]
graph[arr_of_people[12]] = []
graph[arr_of_people[13]] = [arr_of_people[11]]
graph[arr_of_people[14]] = []
graph[arr_of_people[15]] = [arr_of_people[9]]

print(graph)


def BFS(start):
    search_queue = queue.Queue()
    for k in range(len(graph[start])):
        search_queue.put(graph[start][k])
    checked = []
    while not search_queue.empty():
        person = search_queue.get()
        if person not in checked:
            if person.speciality == "IT":
                print(f"Found an IT specialist! {person.name} {person.speciality}")
                return True
            for m in range(len(graph[person])):
                search_queue.put(graph[person][m])
            checked.append(person)
        # print(search_queue.qsize(), len(checked),checked)
    print(f"There are no IT specialists")
    return False


print()
BFS(arr_of_people[0])
