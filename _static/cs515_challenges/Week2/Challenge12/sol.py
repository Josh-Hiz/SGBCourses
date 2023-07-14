# define factorial function
#
# please practice using for/range---even if you know other methods!
def factorial(n):
    if n == 0: return 1
    r = 1
    for i in range(n,0,-1):
        r*=i
    return r 