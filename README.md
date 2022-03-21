# Genetic algorithm
## Implementation of genetic algoithm in python.
Algorithm is looking for the best placement matrix for the machines [represented by numbers], which have a values, that effect on the final cost and which depends on the pair of the machines. 

The goal is to reduce the summary cost to the minimum.
### The equation that counts the final cost: ∑FijCijDij
* Fij – the flow of the material between i and j
* Cij – the cost of servicing the materials jest to koszt obsługi materiałów between i and j
* Dij – the distance between i and j.

Formula used to count distance between two machines (i and j): 𝐷 =|𝑥 −𝑥|+|𝑦 −𝑦|
