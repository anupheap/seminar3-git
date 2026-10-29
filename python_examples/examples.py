"""Run all twelve complete numerical walkthroughs: python python_examples/examples.py"""


# Python: solving the intersection
print('Python: solving the intersection')
import numpy as np
A = np.array([[2., -1.], [-1., 2.]])
b = np.array([0., 3.])
x = np.linalg.solve(A, b)
print(x)  # [1. 2.]
print(A @ x - b)  # [0. 0.]
assert np.allclose(A @ x, b)


# Python: the weights are coordinates
print('Python: the weights are coordinates')
import numpy as np
A = np.array([[2., -1.], [-1., 2.]])
a1, a2 = A[:, 0], A[:, 1]
b = a1 + 2 * a2
print(b)  # [0. 3.]
x = np.array([1., 2.])
assert np.allclose(b, A @ x)
print(A @ x)  # [0. 3.]


# Python: elimination one row at a time
print('Python: elimination one row at a time')
import numpy as np
Ab = np.array([[1., 2., 1., 4.],
               [2., 5., 3., 10.],
               [1., 0., 8., 9.]])
Ab[1] -= 2 * Ab[0]
Ab[2] -= Ab[0]
Ab[2] += 2 * Ab[1]
print(Ab)
# [[1. 2. 1. 4.]
#  [0. 1. 1. 2.]
#  [0. 0. 9. 9.]]


# Python: solving upward from the last row
print('Python: solving upward from the last row')
import numpy as np
U = np.array([[1., 2., 1.],
              [0., 1., 1.],
              [0., 0., 9.]])
c = np.array([4., 2., 9.])
x = np.zeros(3)
x[2] = c[2] / U[2, 2]
x[1] = (c[1] - x[2]) / U[1, 1]
x[0] = c[0] - 2*x[1] - x[2]
print(x)  # [1. 1. 1.]
assert np.allclose(U @ x, c)


# Python: three equivalent products
print('Python: three equivalent products')
import numpy as np
A = np.array([[2, -1], [-1, 2]])
B = np.array([[1, 2], [0, 1]])
C = A @ B
by_columns = np.column_stack(
    [A @ B[:, j] for j in range(2)])
assert np.allclose(C, by_columns)
terms = [np.outer(A[:, k], B[k])
         for k in range(2)]
by_outer = sum(terms)
assert np.allclose(C, by_outer)
print(C)      # [[2, 3], [-1, 0]]
print(B @ A)  # [[0, 3], [-1, 2]]


# Python: reducing both halves together
print('Python: reducing both halves together')
import numpy as np
A = np.array([[1., 3.], [2., 7.]])
aug = np.column_stack((A, np.eye(2)))
aug[1] -= 2 * aug[0]
aug[0] -= 3 * aug[1]
inverse = aug[:, 2:]
print(inverse)  # [[7, -3], [-2, 1]]
assert np.allclose(aug[:, :2], np.eye(2))
assert np.allclose(A @ inverse, np.eye(2))


# Python: transpose and row permutation
print('Python: transpose and row permutation')
import numpy as np
A = np.arange(1, 7).reshape(2, 3)
print(A.shape)  # (2, 3)
R = A.T
print(R.shape)  # (3, 2)
print(R)  # [[1, 4], [2, 5], [3, 6]]
P = np.array([[0, 1, 0],
              [0, 0, 1],
              [1, 0, 0]])
print(P @ R)  # [[2, 5], [3, 6], [1, 4]]
assert np.allclose(P.T @ P, np.eye(3))


# Python: closure examples and a counterexample
print('Python: closure examples and a counterexample')
import numpy as np
u = np.array([1, 2])
v = np.array([-2, -4])
assert u[1] == 2*u[0]
assert v[1] == 2*v[0]
w = 3*u - 2*v
print(w)  # [7 14]
assert w[1] == 2*w[0]
q = np.array([1, 1])
assert np.all(q >= 0)
print(np.all(-q >= 0))  # False


# Python: testing whether b belongs to C(B)
print('Python: testing whether b belongs to C(B)')
import numpy as np
B = np.array([[1, 2, 3], [2, 4, 6]])
r = np.linalg.matrix_rank(B)
print(r)  # 1
good = np.column_stack((B, [4, 8]))
print(np.linalg.matrix_rank(good) == r)
# True: the target is in C(B)
bad = np.column_stack((B, [4, 7]))
assert np.linalg.matrix_rank(good) == r
print(np.linalg.matrix_rank(bad) == r)
# False: the target is outside C(B)


# Python: adding a nullspace vector
print('Python: adding a nullspace vector')
import numpy as np
B = np.array([[1, 2, 3], [2, 4, 6]])
N = np.array([[-2, -3], [1, 0], [0, 1]])
assert np.allclose(B @ N, 0)
xp = np.array([4., 0., 0.])
x = xp + N @ np.array([0.5, 1.0])
print(x)  # [0.  0.5 1. ]
assert np.allclose(B @ x, [4, 8])
print(B @ x)  # [4. 8.]


# Python: coordinates in a different basis
print('Python: coordinates in a different basis')
import numpy as np
V = np.array([[1., 1.], [0., 1.]])
v = np.array([3., 2.])
c = np.linalg.solve(V, v)
print(c)  # [1. 2.]
assert np.allclose(V @ c, v)
assert np.linalg.matrix_rank(V) == 2


# Python: rank plus nullity
print('Python: rank plus nullity')
import numpy as np
from scipy.linalg import null_space
M = np.array([[1., 0., 1.],
              [2., 1., 3.],
              [0., 1., 1.]])
r = np.linalg.matrix_rank(M)
N = null_space(M)
print(r, N.shape[1])  # 2 1
assert np.allclose(M @ N, 0)
assert r + N.shape[1] == M.shape[1]
print(r, N.shape[1], M.shape[1])  # 2 1 3
