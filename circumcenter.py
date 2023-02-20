import numpy as np
from numpy.linalg import solve


def solve_circumcenter(p1: np.ndarray, p2: np.ndarray, p3: np.ndarray):
    # 平面の連立方程式
    left = [p1, p2, p3]
    right = [1, 1, 1]
    res = solve(left, right)

    # 外心点の連立方程式
    vector_p1_p2 = p2 - p1
    vector_p1_p3 = p3 - p1
    center_p1_p2 = (p1 + p2) / 2
    center_p1_p3 = (p1 + p3) / 2

    left = [res, vector_p1_p2, vector_p1_p3]
    right = [
        1, 
        (vector_p1_p2 * center_p1_p2).sum(),
        (vector_p1_p3 * center_p1_p3).sum()
    ]
    res = solve(left, right)
    
    # 完了
    return res


if __name__ == '__main__':
    # 座標
    p1 = np.array([2, 5, 3])
    p2 = np.array([-4, 2, -1])
    p3 = np.array([1, -3, 2])
    # リザルト
    res = solve_circumcenter(p1, p2, p3)
    print(res)