import argparse


def get_options():
    parser = argparse.ArgumentParser()
    # TODO: 按 1-simplelayout-CLI 要求添加相应参数
    parser = argparse.ArgumentParser()  # 创建对象
    parser.add_argument("--board_grid", type=int, default=100,
                        help="布局板分辨率")  # 添加参数
    parser.add_argument("--unit_grid", type=int, default=10,
                        help="矩形组件分辨率")
    parser.add_argument("--unit_n", type=int, default=3, help="组件数")
    parser.add_argument("--positions", type=int, nargs='+', help="编号")
    parser.add_argument("-o", "--outdir", type=str, default="example_dir",
                        help="输出结果的目录")
    parser.add_argument("--file_name", type=str, default="example",
                        help="文件名")
    options = parser.parse_args()
    return options
