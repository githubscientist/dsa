import sys

# java: varargs: variable arguments
# javascript: rest arguments


# def main(*args):
#     print(sys.argv[1])

#     sum = 0
#     for arg in args:
#         sum += arg

#     print(sum)


# # boilerplate code
# if __name__ == "__main__":
#     main(1, 2, 3, 4, 5)

def main(**kwargs):
    print(kwargs)


# boilerplate code
if __name__ == "__main__":
    main(a=1, b=2, c=3)
