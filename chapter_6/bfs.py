from collections import deque

def person_is_seller(name):
    return name[-1] == 'm' #very simple function which assumes that every name ended in 'm' is a mango seller

def search(name):
    search_line = deque()
    search_line += grafo[name]
    verified = []
    while search_line:
        person = search_line.popleft()
        if not person in verified:
            if person_is_seller(person):
                print (person + " is an mango seller!")
                return True
            else:
                search_line += grafo[person]
                verified.append(person)
    return False

grafo = {}
grafo["you"] = ["alice", "bob", "claire"]
grafo["bob"] = ["anuj", "peggy"]
grafo["alice"] = ["peggy"]
grafo["claire"] = ["thom", "jonny"]
grafo["anuj"] = []
grafo["peggy"] = []
grafo["thom"] = []
grafo["jonny"] = []

search("you")