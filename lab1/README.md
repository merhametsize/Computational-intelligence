Gabriele Cassetta s296284 

October 15th 2022

# Set covering
Given a number $N$ and some lists of integers $P = (L_0, L_1, L_2, ..., L_n)$, determine, if possible, $S = (L_{s_0}, L_{s_1}, L_{s_2}, ..., L_{s_n})$, such that each number between $0$ and $N-1$ appears in at least one list, and that the total numbers of elements in all $L_{s_i}$ is minimum.

## Approach
I used a recursive search function with pruning to explore the solution space. Pruning is done when the current candidate is certainly worse than the best solution found insofar, i.e. when the #elements of the former is greater than the #elements of the latter.
I wrote the code from scratch.

## Results
With N>~30 the program starts to face expensive computations, and waiting times exceed the few seconds heading towards infinity.

* N=5: k=3, nodes=21887 <br/>
[[2, 4], [0, 1], [3]]
* N=10: k=4, nodes=122923 <br/>
[[1, 7], [8, 2], [4, 5, 6], [0, 9, 3]]
* N=20: k=5, nodes=118752 <br/>
[[8, 4, 7], [2, 6, 8, 10, 12, 15, 18], [16, 9, 19, 6], [0, 5, 11, 16, 17], [1, 3, 13, 14]]
* N=30: k=5 nodes=24484845 <br/>
[[1, 3, 12, 20, 21], [10, 13, 16, 18, 21, 29], [2, 5, 7, 9, 11, 14, 17, 22, 26, 28], [0, 1, 4, 6, 7, 15, 19, 25, 27], [6, 8, 15, 18, 23, 24]]
* N=50: ...too expensive computations
