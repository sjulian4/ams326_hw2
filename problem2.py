import numpy as np

# (1) (30 pts) Solving the Linear System: Write a computer program to solve the linear system Ax = b, where A is the given coefficient matrix and b is the given right-hand side vector with N = 126.

N = 126

np.random.seed(2) # consistency

# generate random matrix A
A = np.random.uniform(-1, 1, (N, N))

# vector of ones
b = np.ones(N)

# solve Ax = b
x = np.linalg.solve(A, b)

# todo make this not .solve






# (2) (20 pts) Verifying the Solution: Write a computer program (or extend the program from (1)) to verify the accuracy of your solution x by computing the L1 residual norm |AX − b|_1

# compute L1 residual norm
# residual = np.linalg.norm(A @ x - b, 1)
residual = 0
for i in range(N):
    residual += abs((np.matmul(A, x) - b)[i])

print("L1 residual norm:", residual)


# 3.7416736375917026e-12