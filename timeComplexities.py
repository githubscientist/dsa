'''
Time Complexity:

Why do we need to analyze the time complexity of an algorithm?

To compare the efficiency of different algorithms.

In order to do that, we need to analyze the time complexity of an algorithm and compare it with other algorithms.

Performance factors:

1. Running time: The time taken by the algorithm to run.
2. Memory usage: The amount of memory used by the algorithm.

Time complexity: The amount of time taken by an algorithm to run as a function of the length of the input.
Space complexity: The amount of memory used by the algorithm to run as a function of the length of the input.

Mathematical Notations: Asymptotic Notations

1. Big O Notation: O(n) - Upper bound - Worst case
2. Omega Notation: Ω(n) - Lower bound - Best case
3. Theta Notation: Θ(n) - Tight bound - Average case


Situations:

1. Best case: The minimum time taken by the algorithm to run.
2. Worst case: The maximum time taken by the algorithm to run.
3. Average case: The average time taken by the algorithm to run.

Example: Linear Search

Numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

1. Best case (first element is the key): If the key is 1, comparisons = 1 => best case time complexity = O(1)
2. Worst case (last element is the key): If the key is 10, comparisons = 10 => worst case time complexity = O(n)
3. Average case (key is in the middle): If the key is 5, comparisons = 5 => average case time complexity = O(n/2) = O(n)

Example1: 

a = 0, b = 0
for i in range(n):
    a = a + i

for j in range(m):
    b = b + j

Given the following options, which one is the correct time complexity of the above code?

a. O(1)
b. O(log n)
c. O(n)
d. O(n log n)
e. O(n^2)
f. O(2^n)
g. O(n!)

Answer: O(n)

Explanation:

a = 0, b = 0 => declarations, initializations, assignments, conditionals, etc. => 1 execution

for i in range(n):
    a = a + i

=> n executions

for j in range(m):
    b = b + j

=> m executions

Total time complexity, T(n, m) = 1 + n + m 
                               = n + m [ignoring the constant term]
                               = O(n + m) or O(n)


Example2:

a = 0, b = 0 => 1 execution
for i in range(n):
    a = a + i
=> n executions

for j in range(n):
    b = b + j
=> n executions

Time Complexity, T(n) = 1 + n + n
                      = 1 + 2 * n
                      = 2 * n
                      = O(n)    

                      
Example 3:

a = 0, b = 0
for i in range(n):
    a = a + i
    for j in range(n):
        b = b + j
                      
Time Complexity = ?

Two Ways:

1. Calculate the time complexity of the inner loop and multiply it with the time complexity of the outer loop.


a = 0, b = 0 => execution = 1

outer loop: for i in range(n) => n executions

inner loop: for j in range(n) => n executions

Total time complexity, T(n) = 1 + n * n
                            = 1 + n^2
                            = O(n^2)

2. Second way

a. Assume some random values for n

n = 4
n = 5
n = 6

b. find the number of executions

n = 4   
    i = 0; j = 0, 1, 2, 3 => 4 executions
    i = 1; j = 0, 1, 2, 3 => 4 executions
    i = 2; j = 0, 1, 2, 3 => 4 executions
    i = 3; j = 0, 1, 2, 3 => 4 executions

    total executions = 4 + 4 + 4 + 4 = 16 executions

n = 5
    i = 0; j = 0, 1, 2, 3, 4 => 5 executions
    i = 1; j = 0, 1, 2, 3, 4 => 5 executions
    i = 2; j = 0, 1, 2, 3, 4 => 5 executions
    i = 3; j = 0, 1, 2, 3, 4 => 5 executions
    i = 4; j = 0, 1, 2, 3, 4 => 5 executions

    total executions = 5 + 5 + 5 + 5 + 5 = 25 executions

n = 6   
    i = 0; j = 0, 1, 2, 3, 4, 5 => 6 executions
    i = 1; j = 0, 1, 2, 3, 4, 5 => 6 executions
    i = 2; j = 0, 1, 2, 3, 4, 5 => 6 executions
    i = 3; j = 0, 1, 2, 3, 4, 5 => 6 executions
    i = 4; j = 0, 1, 2, 3, 4, 5 => 6 executions
    i = 5; j = 0, 1, 2, 3, 4, 5 => 6 executions

    total executions = 6 + 6 + 6 + 6 + 6 + 6 = 36 executions

c. Find the pattern and write the formula

n = 4, executions = 16
n = 5, executions = 25
n = 6, executions = 36

number of executions = n^2

d. Find the time complexity

Time Complexity = T(n) = 1 + n^2
                       = O(n^2) [ignoring the constant term]


Example 4:

a = 0
i = 0
while i < n:
    j = n
    while j > i:
        a = a + i + j
        j = j - 1
    i = i + 1


1. Assume some random values for n

n = 4
n = 5
n = 6

2. Find the number of executions

n = 4
    i = 0; j = 4, 3, 2, 1 => 4 executions
    i = 1; j = 4, 3, 2 => 3 executions
    i = 2; j = 4, 3 => 2 executions
    i = 3; j = 4 => 1 execution

    total executions = 4 + 3 + 2 + 1 = 10 executions

n = 5
    i = 0; j = 5, 4, 3, 2, 1 => 5 executions
    i = 1; j = 5, 4, 3, 2 => 4 executions
    i = 2; j = 5, 4, 3 => 3 executions
    i = 3; j = 5, 4 => 2 executions
    i = 4; j = 5 => 1 execution

    total executions = 5 + 4 + 3 + 2 + 1 = 15 executions

n = 6
    i = 0; j = 6, 5, 4, 3, 2, 1 => 6 executions
    i = 1; j = 6, 5, 4, 3, 2 => 5 executions
    i = 2; j = 6, 5, 4, 3 => 4 executions
    i = 3; j = 6, 5, 4 => 3 executions
    i = 4; j = 6, 5 => 2 executions
    i = 5; j = 6 => 1 execution

    total executions = 6 + 5 + 4 + 3 + 2 + 1 = 21 executions

3. Find the pattern and write the formula

n = 4, executions = 10
n = 5, executions = 15
n = 6, executions = 21

executions = sum of first n natural numbers
        S(n) = n + n-1 + n-2 + ... + 1
        S(n) = 1 + 2 + 3 + ... + n
        -----------------------------
        2 * S(n) = n+1 + n+1 + n+1 + ... + n+1
        2 * S(n) = n * (n+1)
        S(n) = n * (n+1) / 2

4. Find the time complexity

Time Complexity = T(n) = 1 + [n * (n+1) / 2]
                       = 1 + n^2 + n / 2
                       = O(n^2 + n) [ignoring the constant term]
                       = O(n^2) [ignoring the lower order term]


Example 5:

int i, j, k = 0;
for (i = n/2; i <= n; i++) {
    for (j = 2; j <= n; j = j * 2) {
        k = k + n/2;
    }
}

Time Complexity = ?

Solution:

outer loop: for (i = n/2; i <= n; i++) => n/2 to n => n/2 + 1 => n/2 executions

inner loop:

1. Assume some random values for n

n = 10
n = 16
n = 29
n = 30
n = 31
n = 40

2. Find the number of executions

n = 10; j = 2, 4, 8 => 3 executions
n = 16; j = 2, 4, 8, 16 => 4 executions
n = 29; j = 2, 4, 8, 16 => 4 executions
n = 30; j = 2, 4, 8, 16 => 4 executions
n = 31; j = 2, 4, 8, 16 => 4 executions
n = 40; j = 2, 4, 8, 16, 32 => 5 executions

3. Find the pattern and write the formula

n = 10, executions = 3
n = 16, executions = 4
n = 29, executions = 4
n = 30, executions = 4
n = 31, executions = 4
n = 40, executions = 5

executions => what raised to the power of 2 gives n? 

For any given n, the number of executions = log(n) [base 2]

4. Find the time complexity

Time Complexity = T(n) = n/2 * log(n) = O(n log n) [ignoring the constant term]


Example 6:

Problem: Given a list of numbers, we need to find the different ways in which we can select the numbers. Print all the possible ways.

Example: [1, 2, 3]

Output:

0 numbers: []
1 number: [1], [2], [3]
2 numbers: [1, 2], [1, 3], [2, 3]
3 numbers: [1, 2, 3]

3 numbers => 2^3 = 8 ways

Example: [1, 2, 3, 4]

Output:

0 numbers: []
1 number: [1], [2], [3], [4]
2 numbers: [1, 2], [1, 3], [1, 4], [2, 3], [2, 4], [3, 4]
3 numbers: [1, 2, 3], [1, 2, 4], [1, 3, 4], [2, 3, 4]
4 numbers: [1, 2, 3, 4]

4 numbers => 2^4 = 16 ways

Time Complexity = O(2^n) [ignoring the constant term]

Example 7:

Problem: Given a word, we need to find all the possible permutations of the word.

Example: "abc"

Output: "abc", "acb", "bac", "bca", "cab", "cba"

Time Complexity = O(n!) [ignoring the constant term]

'''
# from math import log

# iterations = [10, 16, 29, 30, 31, 40]

# for n in iterations:
#     print(f"n = {n}")
#     print(f"Number of executions = {int(log(n, 2))}")
#     print()
