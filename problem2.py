import numpy as np

# (1) (30 pts) Solving the Linear System: Write a computer program to solve the linear system Ax = b, where A is the given coefficient matrix and b is the given right-hand side vector with N = 126.

N = 126

np.random.seed(2) # consistency

# generate random matrix A
A = np.random.uniform(-1, 1, (N, N))

# vector of ones
b = np.ones(N)

# solve Ax = b:
A_original = A.copy()
b_original = b.copy()
# forward elimination
for k in range(N-1):
    for i in range(k+1, N):
        factor = A[i,k] / A[k,k]
        A[i,k:] = A[i,k:] - factor * A[k,k:]
        b[i] = b[i] - factor * b[k]


# back substitution
x = np.zeros(N)

for i in range(N-1, -1, -1):
    s = 0
    for j in range(i+1, N):
        s += A[i,j] * x[j]
    x[i] = (b[i] - s) / A[i,i]

# todo make this not .solve

print("Solved x: " + str(x))




# (2) (20 pts) Verifying the Solution: Write a computer program (or extend the program from (1)) to verify the accuracy of your solution x by computing the L1 residual norm |AX − b|_1

# compute L1 residual norm
# residual = np.linalg.norm(A @ x - b, 1)
residual = 0
for i in range(N):
    residual += abs((np.matmul(A_original, x) - b_original)[i])

print("L1 residual norm:", residual)


# 2.3175339425307584e-10