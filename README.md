# traveling salesperson comparison
 Comparison between different solutions to tsp.

complete_salesman O(n!):
Computes every permutation.

dynamic_salesman O(n^2 2^n):
Based on c++ example from https://algo.is/aflv16/aflv_06_dynamic_programming.pdf
Does not work perfectly (yet).

genetic_salesman:
Based on genetic algorithm: https://en.wikipedia.org/wiki/Selection_(genetic_algorithm)
Uses SCX as described here https://pdfs.semanticscholar.org/a1e6/50daed4ed9c6a403b08e5d50b3ea9f3b5de4.pdf