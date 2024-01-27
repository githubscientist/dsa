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

# Problem: Printing the first N natural numbers in reverse order (from N to 1)


# def fP(N):
#     if N == 0:
#         return

#     print(N)
#     fP(N-1)


# fP(5)


'''
    fP(5)
        - N = 5; 5 == 0; false
        - print(5)
        - fP(4)
            - N = 4; 4 == 0; false
            - print(4)
            - fP(3)
                - N = 3; 3 == 0; false
                - print(3)
                - fP(2)
                    - N = 2; 2 == 0; false
                    - print(2)
                    - fP(1)
                        - N = 1; 1 == 0; false
                        - print(1)
                        - fP(0)
                            - N = 0; N == 0; true; return

    
    fP(5)

                        


'''


# Problem: Printing the first N natural numbers from 1 to N.

'''
    Input: 5

    Output:

    1
    2
    3
    4
    5

    Input: 10

    Output:

    1
    2
    3
    4
    5
    6
    7
    8
    9
    10

'''


# def fP(N):
#     if N == 6:
#         return

#     print(N)
#     fP(N+1)


# fP(1)

'''
    fP(1)
        - N = 1; 1 == 5; false
        - fP(2)
            - N = 2; 2 == 5; false
            - fP(3)
                - N = 3; 3 == 5; false
                - fP(4)
                    - N = 4; 4 == 5; false
                    - fP(5)
                        - N = 5; 5 == 5; true; return
                    - print(4) x
                - print(3) x
            - print(2) x
        - print(1) x

'''


# def fP(N):
#     if N == 0:
#         return

#     fP(N-1)
#     print(N)


# fP(4)

'''
    Write a function with an iterative approach and a recursive approach to print the sum of the first N natural numbers.

    Input: 5

    Output: 15

    Explanation: 1 + 2 + 3 + 4 + 5 = 15

    Input: 10

    Output: 55

    Explanation: 1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 + 10 = 55
'''


def S(N):
    # your code goes here
    pass


print(S(5))  # 15
print(S(10))  # 55
print(S(4))  # 10
print(S(6))  # 21
print(S(0))  # 0
