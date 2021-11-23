# TODO 正确导入函数 generate_matrix, save_matrix, save_fig
from simplelayout.generator.core import generate_matrix
from simplelayout.generator.utils import save_matrix, save_fig, make_dir
from simplelayout.cli import get_options  # TODO: 保证不修改本行也可以正确导入


def main():
    # TODO 使用导入的函数按命令行参数生成数据，包括 mat 文件与 jpg 文件
    opt = get_options()
    outdir = opt.outdir
    name = opt.file_name
    matrix = generate_matrix(opt.board_grid, opt.unit_grid, opt.unit_n,
                             opt.positions)
    make_dir(outdir)
    path = outdir + '/' + name
    save_matrix(matrix, path)
    save_fig(matrix, path)
    return


if __name__ == "__main__":
    main()
