"""
辅助函数
"""

from pathlib import Path
import matplotlib.pyplot as plt
import scipy.io as sio


def save_matrix(matrix, file_name):
    # TODO: 存储 matrix 到 file_name.mat, mdict 的 key 为 "matrix"
    mdic = {'matrix': matrix}
    sio.savemat(file_name + ".mat", mdic)
    return


def save_fig(matrix, file_name):
    # TODO: 将 matrix 画图保存到file_name.jpg
    plt.imsave(file_name + ".jpg", matrix)
    return


def make_dir(outdir):
    Path(outdir).mkdir(exist_ok=True, parents=True)
    return
