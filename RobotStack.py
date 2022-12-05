import math
import sys

#H represnets recursion start point
# k            k+n-1 k+n(H)
# k-1           H    k-1+n
# ...      H
# 3   H
# 2 H
# 1 2 3 .... n-2 n-1 n

def memoizedAlborithm(b,n,k, dp):  

    if dp[n][k] != 0:
        return dp[n][k]    
    if k == 1 and n >= b:
        dp[n][k] = (math.factorial(n) / ((math.factorial(b)) * (math.factorial(n-b))))
        return dp[n][k]
    if k == b and n >= b:
        dp[n][k] = (math.factorial(n+b-1) / (math.factorial(b) * math.factorial((n+b-1)-b)))
        return dp[n][k]
    if n == 1:
        if k > b:
            dp[n][k] = 1
            return dp[n][k]
        else:
            dp[n][k] = 0
            return dp[n][k]
    if b == 1:
        dp[n][k] = n
        return dp[n][k]
    if n * k < b:
        dp[n][k] = 0
        return dp[n][k]
    if n * k > b:
        dp[n][k] = ((n*k) - b) 

    for i in range(1,k+1,1):
        dp[n][k] += memoizedAlborithm(b-i, n-1, k, dp)
    return dp[n][k]

def fileReader(filename):
    b_list = []
    n_list = []
    i_list = []
    datalist = []
    with open(filename) as f:
        for line in f.readlines():
            datalist.append(line.split())

    return datalist


if __name__ == '__main__':
    import sys
    filename = sys.argv[-1]
    datalist = fileReader(filename)
    for i in datalist:
        set = (b, n, k) = i
        dp = [[0 for i in range(int(k)+1)] for j in range(int(n)+1)]
        value = memoizedAlborithm(int(b),int(n),int(k), dp)
        print("(" + b + "," + n + "," + k + ") = " + str(value))
        print(dp,'\n\n')
        