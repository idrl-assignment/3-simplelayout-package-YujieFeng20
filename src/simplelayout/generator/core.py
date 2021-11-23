"""
数据生成的主要逻辑
"""


import numpy as np


def generate_matrix(
    board_grid: int, unit_grid: int, unit_n: int, positions: list
) -> np.ndarray:
    """生成指定布局矩阵

    Args:
        board_grid (int): 布局板分辨率，代表矩形区域的边长像素数
        unit_grid (int): 矩形组件分辨率
        unit_n (int): 组件数
        positions (list): 每个元素代表每个组件的位置
    Returns:
        np.ndarray: 布局矩阵
    """
    if board_grid % unit_grid or unit_n != len(positions):
        exit()
    for item in positions:
        if item < 1 or item > (board_grid / unit_grid) ** 2:
            exit()
    m = np.zeros((board_grid, board_grid))
    n = int(board_grid/unit_grid)  # 每一行、列的组件数
    b = board_grid
    for item in positions:
        p = int(item//n)
        q = item % n
        if q == 0:
            m[unit_grid*(p-1):unit_grid*p, b-unit_grid:b] = [1]
        else:
            m[unit_grid*p:unit_grid*(p+1), unit_grid*(q-1):unit_grid*q] = [1]
    return m
