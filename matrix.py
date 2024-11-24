import numpy as np
import argparse
import ast

def matrix_multiply(matrices: list[np.matrix]) -> np.matrix:
    return np.linalg.multi_dot(matrices)

def matrix_inverse(matrices: list[np.matrix]) -> np.matrix:
    return np.linalg.inv(matrices)

def matrix_transpose(matrix: np.matrix) -> np.matrix:
    return np.transpose(matrix)

def matrix_power(matrix: np.matrix, n: int) -> np.matrix:
    return np.linalg.matrix_power(matrix, n)

def matrix_addition(matrices: list[np.matrix]) -> np.matrix:
    aggr = matrices[0]
    for i in range(1, len(matrices)):
        aggr = aggr + matrices[i]
    return aggr

def matrix_subtraction(matrices: list[np.matrix]) -> np.matrix:
    aggr = matrices[0]
    for i in range(1, len(matrices)):
        aggr = aggr - matrices[i]
    return aggr

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        prog="matrix_cli_tool",
        description="Simple matrix cli tool"
    )

    parser.add_argument("--func", 
                        help="a: addition, i:inverse, m: multiplication, s: subtraction, p: power, t: transpose",
                        required=True
                        )
    parser.add_argument("matrix", 
                        help="type the matrix/matrices in 2d array here",
                        nargs="+")
    parser.add_argument("--pow",
                        help="power for matrix power function")
    args = parser.parse_args()
    # print(args.func)
    # print(args.matrix)
    matrices = [np.array(ast.literal_eval(matrix_str)) for matrix_str in args.matrix]
    
    if args.func == "a":
        print(matrix_addition(matrices))
    elif args.func == "s":
        print(matrix_subtraction(matrices))
    elif args.func == "i":
        print(matrix_inverse(matrices))
    elif args.func == "p":
        power = int(args.pow)
        assert len(matrices) == 1
        print(matrix_power(matrices[0], power))
    elif args.func == "t":
        assert len(matrices) == 1
        print(matrix_transpose(matrices[0]))
    elif args.func == "m":
        print(matrix_multiply(matrices))


