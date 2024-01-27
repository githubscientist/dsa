# Recursion: A function calling itself is called recursion

# # example of a recursive function
# def sayHello():
#     print("Hello")
#     sayHello()


# sayHello()

'''
    Recursive Tree

    sayHello()
        - print("Hello")
        - sayHello()
            - print("Hello")
            - sayHello()
                - print("Hello")
                - sayHello()
                    - print("Hello")
                    ...
                    ...
'''

# purpose / use of a recursion function
# 1. To solve a problem that can be broken down into smaller repetitive problems
# 2. It is used in many algorithms like divide and conquer (quick sort, merge sort), dynamic programming, backtracking, tree traversal, etc.

# iterative approach vs recursive approach
# iterative approach: using loops
# recursive approach: using functions calling itself

# Problem: print 'hello' N times
# iterative approach
# def sayHelloIterative(N):
#     for i in range(N):
#         print('hello')


# sayHelloIterative(5)


# recursive approach
def sayHelloRecursive(N):
    if N == 0:
        return
    print('hello')
    sayHelloRecursive(N - 1)


sayHelloRecursive(3)

'''
    sayHelloRecursive(3)
        - N = 3
        - print('hello')
        - sayHelloRecursive(2)
            - N = 2
            - print('hello')
            - sayHelloRecursive(1)
                - N = 1
                - print('hello')
                - sayHelloRecursive(0)
                    - N = 0; 0 == 0; true; return
    
    sayHelloRecursive(3)
'''

'''
    Exercises:

    1. Write a function with an iterative approach and a recursive approach to print the first N natural numbers in reverse order (from N to 1)

    Input: 5

    Output: 5 4 3 2 1

    2. Write a function with an iterative approach and a recursive approach to print the sum of the first N natural numbers.

    Input: 5

    Output: 15

    Explanation: 1 + 2 + 3 + 4 + 5 = 15

    Input: 10

    Output: 55

    Explanation: 1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 + 10 = 55

    3. Write a function with an iterative approach and a recursive approach to print the first N even natural numbers.

    Input: 5

    Output: 2 4 6 8 10

    4. Write a function with an iterative approach and a recursive approach to print the first N odd natural numbers.

    Input: 5

    Output: 1 3 5 7 9

    5. Write a function with an iterative approach and a recursive approach to print the first N natural numbers that are divisible by 3.

    Input: 5

    Output: 3 6 9 12 15

    6. Write a function with an iterative approach and a recursive approach to print the sum of the digits of a given number.

    Input: 123

    Output: 6

    Explanation: 1 + 2 + 3 = 6

    Input: 2347

    Output: 16

    Explanation: 2 + 3 + 4 + 7 = 16

    https://www.hackerrank.com/contests/data-structures-and-algorithms-using-python/

    https://github.com/githubscientist/dsa.git
'''
