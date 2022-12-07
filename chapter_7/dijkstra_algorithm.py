   
#CREATING THE HASH TABLES
grafo = {}

grafo["start"] = {}
grafo["start"]["a"] = 6
grafo["start"]["b"] = 2

grafo["a"] = {}
grafo["a"]["end"] = 1

grafo["b"] = {}
grafo["b"]["a"] = 3
grafo["b"]["end"]=5

grafo["end"] = {} #end vertices doesnt have neighbors

#CREATING THE COST HASH TABLE
infinity = float("inf")
costs = {}
costs["a"] = 6
costs["b"] = 2
costs["end"] = infinity

#CREATING THE PARENTS HASH TABLE
parents = {}
parents["a"] = "start"
parents["b"] = "end"
parents["end"] = None

#CREATING AN ARRAY TO MANTAIN THE REGISTY OF EVERY PROCESSED VERTICE, BECAUSE IT IS NOT NEEDED TO VERIFY THEM MORE THAN ONCE
processed = []


def find_cheapest_cost(costs):
    cheapest_cost = float("inf")
    node_cheapest_cost = None
    for node in costs: #go through each node
        cost = costs[node]
        if cost < cheapest_cost and node not in processed: #if the cheapest cost node has not been processed yet...
            cheapest_cost = cost #assign it as the new cheapest cost node
            node_cheapest_cost = node
    return node_cheapest_cost     

node = find_cheapest_cost(costs) #Find the cheapest costs which was not processed yet
while node is not None: #In case every vertices were processed, this loop ends
    cost = costs[node]
    neighbors = grafo[node]
    for n in neighbors.keys(): #run through all the neighbors of this vertice
        new_cost = cost + neighbors[n]
        if costs[n] > new_cost: #in case it is cheaper to reach a neighbor from this vertice
            costs[n] = new_cost #...update its cost
            parents[n] = node #this vertice becomes a new parent for its neighbor
    processed.append(node) #marks the node as 'processed'
    node = find_cheapest_cost(costs) #finds the next node to be processed and the algorithm continue