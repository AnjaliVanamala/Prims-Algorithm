# -*- coding: utf-8 -*-
"""
Created on Tue Jun 11 10:39:11 2024

@author: anjal
"""

# Make node class
class Node():
    def __init__(self, num, num2, weight):
        self.x = num 
        self.y = num2
        self.weight = abs(weight)
        if (weight != 0):
            self.sign = (weight)/abs(weight)
        else:
            self.sign = 1
        
    def __str__(self):
        return(str(self.x) + " " + str(self.y) + " " + str(self.weight))
        
# Build adjacency matrix from file 
def load_adj():
    lines = [[float(x) for x in line.rstrip().split('\t')] for line in open("adjacency_matrix_treatment20.txt", "r")]
    adj = [[] for i in range(len(lines))]
    for i in range(len(lines)):
       for j in range(len(lines[i])):
           if (lines[i][j] != 0):
               adj[i].append(Node(i, j, lines[i][j]))
               #adj[j].append(Node(j, i, lines[i][j]))
               #print(str(i) + " " + str(j))
    return(adj)
    
# Define Graph class
class Graph():
    def __init__(self, taxa):
        self.graph = [[0 for column in range(taxa)]
                      for row in range(taxa)]
    
# Sort adjacencies near zero 
    def max_edge(self, nodelist, adj):
        maxe = Node(-1, -1, 0)
        for i in nodelist:
            for j in range(len(adj[i])):
                if (adj[i][j].y not in nodelist and adj[i][j].weight > maxe.weight):
                    maxe = adj[i][j]
        return(maxe)
            
# Add to graph 
    def add(self, maxe):
        self.graph[maxe.x][maxe.y] = maxe.weight * maxe.sign
        return()

# If find_max returns 0, add next node that's not in list 
    def next_n(self, taxanum, nodelist):
        for i in range(taxanum):
            if (i not in nodelist):
                nodelist.append(i)
                break
        return()
# When all original nodes are in the nodes list stop
    def Prims(self, adj):
        taxa = len(adj)
        nodelist = [0]
        while (len(nodelist) < taxa):
            maxe = self.max_edge(nodelist, adj)
            if maxe.weight != 0:
                self.add(maxe)
                nodelist.append(maxe.y)
            else:
                self.next_n(taxa, nodelist)
        return(self.graph)
# Print out the adjacency matrix for the new graph

# Main 
if __name__ == '__main__':
    adj = load_adj()
    #adj = [[], [], [], [], []]
    """matrix = [[0, 2, 0, 6, 0],
           [2, 0, 3, 8, 5],
               [0, 3, 0, 0, 7],
               [6, 8, 0, 0, 9],
               [0, 5, 7, 9, 0]]
    
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            adj[i].append(Node(i, j, matrix[i][j]))
            adj[j].append(Node(j, i, matrix[i][j]))
          """  
    graph = Graph(len(adj))
    prims = graph.Prims(adj)
    
    f = open("prims_graph.txt", "w") 
    for i in prims:
        for j in i:
            f.write(str(j) + "\t")
        f.write("\n")
    f.close()
    
    list1 = []
    list2 = []
    
    # Weights for nodes 
    nodeImp = []
    for i in range(len(adj)):
        summed = 0
        for j in adj[i]:
            summed += (len(adj[i]) * len(adj[j.y])) / (j.weight)**2
        if summed != 0:
            nodeImp.append(summed/len(adj[i]))
        else:
            nodeImp.append(0)
    nodeImp = [imp/max(nodeImp) for imp in nodeImp]
            
            
    f = open("prims_graph_flat.txt", "w") 
    f.write("Taxa1\tTaxa1Imp\tTaxa2\tCorrelation\n")
    for i in range(len(prims)):
        for j in range(len(prims[i])):
            if (prims[i][j] != 0):
                print(i)
                f.write(str(i) + "\t" + str(nodeImp[i]) + "\t" + str(j) + "\t" + str(prims[i][j]) + "\n")
                #f.write(str(j) + "\t" + str(j) + "\t" + str(i) + "\t" + str(prims[i][j]) + "\n")
                if i not in list1:
                    list1.append(i)
                if j not in list1:
                    list1.append(j)
        f.write(str(i) + "\t" + str(nodeImp[i]) + "\t" + str(i) + "\t" + str(prims[i][i]) + "\n")
    f.close()
    
    f = open("adjacency_matrix_flat.txt", "w") 
    f.write("Taxa1\tTaxa1Imp\tTaxa2\tTaxa2Imp\tCorrelation\n")
    for i in range(len(adj)):
        for j in range(len(adj[i])):
            if (adj[i][j] != 0):
                if (adj[i][j].x, adj[i][j].y) not in list2 and (adj[i][j].y, adj[i][j].x) not in list2:
                    f.write(str(adj[i][j].x) + "\t" + str(nodeImp[adj[i][j].x]) + "\t" + str(adj[i][j].y) + "\t" + str(nodeImp[adj[i][j].y]) + "\t" + str(adj[i][j].weight*adj[i][j].sign) + "\n")
                    print(str(adj[i][j].x) + "\t" + str(adj[i][j].y) + "\t" + str(adj[i][j].weight*adj[i][j].sign) + "\n")
                    list2.append((adj[i][j].x, adj[i][j].y))
        f.write(str(i) + "\t" + str(nodeImp[i]) + "\t" + str(i) + "\t" + str(nodeImp[i]) + "\t" + str(0) + "\n")        
    f.close()
    
            