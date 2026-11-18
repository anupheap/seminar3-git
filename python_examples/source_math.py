"""The supplied slides are the numerical source for every new demo.

Run this file to execute every displayed code stage, check its mathematics and
write sources/code-lessons.json. Manim imports the same constants below.
No browser-side Python execution or hand-written expected output is required.
"""
import contextlib
import io
import json
from pathlib import Path

import numpy as np

ROW_A = [[2, -1], [-1, 2]]
ROW_B = [0, 3]
THREE_A = [[2, -1, 0], [-1, 2, -1], [0, -3, 4]]
THREE_B = [0, -1, 4]
ELIM_A = [[1, 2, 1], [3, 8, 1], [0, 4, 1]]
ELIM_B = [2, 12, 2]
PRODUCT_A = [[1, 2], [3, 4]]
PRODUCT_B = [[5, 6], [7, 8]]
INVERSE_A = [[1, 3], [2, 5]]
PERM_A = [[0, 1, 2], [1, 2, 3], [2, 6, 9]]
PERM_P = [[0, 1, 0], [1, 0, 0], [0, 0, 1]]
GRAM_R = [[1, 2], [3, 0], [0, 4]]
CANVA_A = [[3, 4, 7], [2, 7, 9], [5, 2, 7]]


def lesson(lecture, key, title, source, scene, parts, captions):
    code = ''
    stages = []
    for part, caption in zip(parts, captions, strict=True):
        code += ('\n' if code else '') + part.strip('\n')
        stages.append({'code': code, 'caption': caption})
    return dict(lecture=lecture, key=key, title=title, source=source, scene=scene, stages=stages)


LESSONS = [
    lesson(1, 'l1-rows', 'Solve the original row picture', 'Seminar.pptx, slides 5–6', 'L1Rows', [
        'import numpy as np\nA = np.array([[2., -1.], [-1., 2.]])\nb = np.array([0., 3.])',
        'x = np.linalg.solve(A, b)\nprint("Intersection:", x)',
        'print("A @ x:", A @ x)\nprint("Residual:", A @ x - b)\nassert np.allclose(x, [1., 2.])\nassert np.allclose(A @ x, b)',
    ], ['Enter the two source equations as A and b.', 'The rows meet at (1, 2).', 'Substitution verifies both equations.']),
    lesson(1, 'l1-columns', 'Build the original column combination', 'Seminar.pptx, slides 8–11', 'L1Columns', [
        'import numpy as np\na1 = np.array([2, -1])\na2 = np.array([-1, 2])',
        'b = a1 + 2 * a2\nprint("a1 + 2*a2:", b)',
        'A = np.column_stack((a1, a2))\nprint("A @ [1, 2]:", A @ [1, 2])\nassert np.array_equal(b, [0, 3])\nassert np.array_equal(A @ [1, 2], b)',
    ], ['Take the exact columns from the source.', 'One blue vector plus twice the orange vector reaches b.', 'The row and column pictures use the same weights.']),
    lesson(1, 'l1-3d', 'Verify the three-dimensional system', 'Seminar.pptx, slides 7 and 12', 'L1ThreePlanes', [
        'import numpy as np\nA = np.array([[2., -1., 0.],\n              [-1., 2., -1.],\n              [0., -3., 4.]])\nb = np.array([0., -1., 4.])',
        'x = np.linalg.solve(A, b)\nprint("Intersection:", x)',
        'print("Third column:", A[:, 2])\nassert np.allclose(x, [0., 0., 1.])\nassert np.allclose(A @ x, b)\nassert np.allclose(A[:, 2], b)',
    ], ['The three planes use the source matrix.', 'All three meet at (0, 0, 1).', 'The target is already the third column.']),
    lesson(2, 'l2-elimination', 'Eliminate the original augmented matrix', 'Seminar.pptx, slides 21–24', 'L2Elimination', [
        'import numpy as np\nAb = np.array([[1., 2., 1., 2.],\n               [3., 8., 1., 12.],\n               [0., 4., 1., 2.]])\nprint(Ab)',
        'Ab[1] -= 3 * Ab[0]\nprint("R2 - 3*R1:")\nprint(Ab)',
        'Ab[2] -= 2 * Ab[1]\nprint("R3 - 2*R2:")\nprint(Ab)\nx = np.linalg.solve(Ab[:, :3], Ab[:, 3])\nprint("Solution:", x)\nassert np.allclose(x, [2., 1., -2.])',
    ], ['Start with [A | b] from the PowerPoint.', 'Clear the entry below the first pivot.', 'Pivots 1, 2 and 5 give the solution (2, 1, -2).']),
    lesson(2, 'l2-failure', 'Check the original failure case', 'Seminar.pptx, slide 23', None, [
        'import numpy as np\nAb = np.array([[1., 2., 1., 2.],\n               [3., 8., 1., 12.],\n               [0., 4., -4., 2.]])',
        'Ab[1] -= 3 * Ab[0]\nAb[2] -= 2 * Ab[1]\nprint("Last row:", Ab[2])',
        'assert np.allclose(Ab[2], [0, 0, 0, -10])\nprint("0 = -10: no solution")',
    ], ['The changed last equation is 4y - 4z = 2.', 'Apply the same row operations.', 'The contradiction proves inconsistency.']),
    lesson(3, 'l3-products', 'Compute all four multiplication views', 'Presentation2.pptx, slides 3–6 and 10', 'L3Products', [
        'import numpy as np\nA = np.array([[1, 2], [3, 4]])\nB = np.array([[5, 6], [7, 8]])\nC = A @ B\nprint(C)',
        'columns = np.column_stack([A @ B[:, j]\n                           for j in range(2)])\nrows = np.vstack([A[i, :] @ B\n                  for i in range(2)])\nassert np.array_equal(columns, C)\nassert np.array_equal(rows, C)',
        'outer = sum(np.outer(A[:, k], B[k, :])\n            for k in range(2))\nprint("Outer-product sum:")\nprint(outer)\nassert np.array_equal(outer, [[19, 22], [43, 50]])',
    ], ['Entries are row-column dot products.', 'Computing by rows or columns gives the same C.', 'The sum of column-times-row pieces also gives C.']),
    lesson(3, 'l3-inverse', 'Follow the source Gauss–Jordan steps', 'Presentation2.pptx, slides 8–11', 'L3Inverse', [
        'import numpy as np\nA = np.array([[1., 3.], [2., 5.]])\naug = np.column_stack((A, np.eye(2)))\nprint(aug)',
        'aug[1] -= 2 * aug[0]\naug[1] *= -1\nprint(aug)',
        'aug[0] -= 3 * aug[1]\nAinv = aug[:, 2:]\nprint("Inverse:")\nprint(Ainv)\nassert np.allclose(Ainv, [[-5, 3], [2, -1]])\nassert np.allclose(A @ Ainv, np.eye(2))',
    ], ['Write [A | I] using the source matrix.', 'Clear and normalize the second pivot.', 'The right half is the inverse when the left half is I.']),
    lesson(5, 'l5-permutation', 'Verify the original PA = LU', 'Lecture5.pptx, slides 3–4', 'L5Permutation', [
        'import numpy as np\nA = np.array([[0, 1, 2],\n              [1, 2, 3],\n              [2, 6, 9]])\nP = np.eye(3, dtype=int)[[1, 0, 2]]',
        'PA = P @ A\nprint("After swapping rows:")\nprint(PA)',
        'L = np.array([[1, 0, 0], [0, 1, 0], [2, 2, 1]])\nU = np.array([[1, 2, 3], [0, 1, 2], [0, 0, -1]])\nprint("PA = LU:", np.array_equal(PA, L @ U))\nassert np.array_equal(PA, L @ U)\nassert np.array_equal(P.T @ P, np.eye(3))',
    ], ['The first pivot is zero.', 'P swaps the first two rows.', 'The source factors reproduce the permuted matrix.']),
    lesson(5, 'l5-symmetry', 'Run the original symmetry example', 'Lecture5.pptx, slides 6–7', 'L5Symmetry', [
        'import numpy as np\nR = np.array([[1, 2], [3, 0], [0, 4]], dtype=float)\nprint("R transpose:")\nprint(R.T)',
        'G = R.T @ R\nprint("R.T @ R:")\nprint(G)',
        'print("Symmetric:", np.allclose(G, G.T))\nassert np.allclose(G, [[10, 2], [2, 20]])\nassert np.allclose(G, G.T)',
    ], ['The transpose exchanges rows and columns.', 'Multiply the exact R from the source.', 'Matching off-diagonal entries confirm symmetry.']),
    lesson(5, 'l5-column-space', 'Test the source column space', 'Lecture5.pptx, slides 8–11, using R from slides 6–7', 'L5ColumnSpace', [
        'from sympy import Matrix\nR = Matrix([[1, 2], [3, 0], [0, 4]])\nprint("Basis:", R.columnspace())',
        'u, v = R[:, 0], R[:, 1]\nb = u + 2*v\nprint("A combination:", b.T)\nassert b == Matrix([5, 3, 8])',
        'print("Rank:", R.rank())\nprint("Contains zero:", R * Matrix([0, 0]) == Matrix.zeros(3, 1))\nassert R.row_join(b).rank() == R.rank()\nassert R.rank() == 2',
    ], ['Use the source R to illustrate C(R).', 'Combinations stay inside its column space.', 'Two independent columns span a plane through zero.']),
    lesson(9, 'l9-dependence', 'Run the Canva dependence example', 'Canva Lecture 9, pages 10–19 and 25', 'L9Dependence', [
        'from sympy import Matrix\nA = Matrix([[3, 4, 7], [2, 7, 9], [5, 2, 7]])\nn_vectors = A.shape[1]\nprint("Number of vectors:", n_vectors)',
        'rank = A.rank()\nprint("Rank:", rank)\nprint("Linearly independent?", rank == n_vectors)',
        'relation = Matrix([-1, -1, 1])\nprint("A @ relation:", (A * relation).T)\nassert A[:, 2] == A[:, 0] + A[:, 1]\nassert A * relation == Matrix.zeros(3, 1)\nassert rank == 2',
    ], ['These are the three columns displayed in Canva.', 'Rank two means the three columns are dependent.', 'The third column is the sum of the first two.']),
    lesson(9, 'l9-basis', 'Find the source basis and dimensions', 'Canva Lecture 9, pages 14–24 and 26', 'L9Basis', [
        'from sympy import Matrix\nA = Matrix([[3, 4, 7], [2, 7, 9], [5, 2, 7]])\nreduced, pivots = A.rref()\nprint("RREF:")\nprint(reduced)',
        'basis = [A[:, j] for j in pivots]\nprint("Pivot columns:", pivots)\nprint("Column-space basis:", basis)',
        'rank, nullity = A.rank(), len(A.nullspace())\nprint("Dimensions:", rank, nullity)\nassert (rank, nullity) == (2, 1)\nassert rank + nullity == A.cols',
    ], ['Row reduction identifies the pivot positions.', 'Take basis columns from the original A.', 'The column space has dimension 2 and the nullspace dimension 1.']),
]


def build():
    results = []
    for item in LESSONS:
        result = {**item, 'stages': []}
        previous_output = ''
        for stage in item['stages']:
            stdout = io.StringIO()
            with contextlib.redirect_stdout(stdout):
                exec(compile(stage['code'], item['key'], 'exec'), {})
            full_output = stdout.getvalue()
            added_output = full_output[len(previous_output):] if full_output.startswith(previous_output) else full_output
            result['stages'].append({**stage, 'output': added_output.rstrip(), 'stdout': full_output.rstrip()})
            previous_output = full_output
        results.append(result)
    output = Path(__file__).resolve().parents[1] / 'sources/code-lessons.json'
    output.write_text(json.dumps(results, indent=2, ensure_ascii=False) + '\n', encoding='utf-8')
    print(f'Executed and verified {sum(len(x["stages"]) for x in results)} code stages in {len(results)} new source-based lessons.')
    return results


if __name__ == '__main__':
    build()
