from collections import deque

def person_is_seller(name):
    return name[-1] == 'm' #very simple function which assumes that every name ended in 'm' is a mango seller

def search(name):
    search_line = deque()
    search_line += grafo[name]
    verified = [] #This vector is the way that we mantain registered the names that were already verified 
    while search_line:
        person = search_line.popleft() #takes in the first person on the line
        if not person in verified: #only verifiy the names of the persons who were not verified before
            if person_is_seller(person):
                print (person + " is an mango seller!")
                return True
            else:
                search_line += grafo[person] #add all the "frieds" of this person to the list to be verified
                verified.append(person) #mark the person as verified
    return False #if you got here, it means that no person on the line is a mango seller

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