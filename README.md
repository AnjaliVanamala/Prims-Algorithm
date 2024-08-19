# Prims-Algorithm
A simple program that takes in an input adjacency matrix and outputs the list format of the input matrix, matrix format of the matrix output after prim's algorithm, and list version of the matrix after prim's algorithm. Both list versions are intended to be directly put into cytoscape. List versions include the "importance" of each node which are calculated by the equation $\frac{\sum_{i=0}^{x}{\frac{x*y_i}{r^2}}}{x}$, where: <br> x = the number of connections to the node being calculated (node 1) <br> y_i = the number of connections that a specific node (node i) connected to node 1 has. <br> r = the correlation coefficient between node 1 and node i

## Inputs/Outputs Examples
Input file: "adjacency_matrix.txt" <br>
Prim's matrix output file: "prims_graph.txt" <br>
Flattened prim's matrix output file: "prim's_graph_flat.txt" <br>
Flattened adjacency matrix output file: "adjacency_matrix_flat.txt"