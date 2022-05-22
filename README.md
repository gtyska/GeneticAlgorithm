# Genetic algorithm
Algorithm is looking for the best placement matrix for the machines (represented by numbers). Best placement is defined by the lowest summary cost of the placement, which is counted as followed ⬇️

### The equation that counts the final cost: ∑F<sub>ij</sub>C<sub>ij</sub>D<sub>ij</sub>
* F<sub>ij</sub> – the flow of the material between i and j
* C<sub>ij</sub> – the cost of servicing the materials between i and j
* D<sub>ij</sub> – the distance between i and j.

Formula used to count distance between two machines (i and j): 𝐷 = |𝑥<sub>i</sub> − 𝑥<sub>j</sub>| + |𝑦<sub>i</sub> − 𝑦<sub>j</sub>|

## Tech stack
![Python](https://img.shields.io/badge/Python-14354C?style=for-the-badge&logo=python&logoColor=white)
