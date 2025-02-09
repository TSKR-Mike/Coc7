from math import pi, sqrt

import matplotlib
matplotlib.use('WXagg')
#matrix_file = open('matrix.CocMatrixInfo', 'r')

def load_matrix_from_CocaMatrixInfo(file_name):
    with open(file_name, 'r') as matrix_file:
        try:
            file_data = []
            all_matrix = []
            file_data = matrix_file.readlines()
            for curr in file_data:
                name, actual_data_str = curr.split('>>>')[0], curr.split('>>>')[1]
                curr_matrix = []
                all_curr_lines = actual_data_str.split('|')
                for matrix_line in all_curr_lines:
                    curr_matrix.append([int(item) for item in matrix_line.split(';')])
                all_matrix.append((name, curr_matrix))
            return all_matrix
        except Exception as e:
            raise e

def write_matrix_to_CocMatrixInfo(file_name, matrix):
    """
    :param file_name: str
    :param matrix: [( <matrix name>, <data -> list[list[int...]]> ), ...]
    :return:
    """
    with open(file_name, 'w') as matrix_file:
        try:
            all_matrix = []
            for matrix in matrix:
                name = matrix[0]
                matrix_file.write(str(name)+'>>>')
                data = matrix[1]
                data_str = ''
                data_length = len(data)
                for line, line_index in zip(data, range(len(data))):
                    curr_line_str = ''
                    line_length = len(line)
                    for item, index in zip(line, range(len(line))):
                        curr_line_str += str(item)
                        if index != line_length - 1:
                            curr_line_str += ';'
                    data_str += curr_line_str
                    if line_index != data_length - 1:
                        data_str += '|'
                matrix_file.write(data_str+'\n')

        except Exception as e:
            raise e


print(load_matrix_from_CocaMatrixInfo('matrix2.CocMatrixInfo'))
#write_matrix_to_CocMatrixInfo('matrix2.CocMatrixInfo', [('m1', [[1, 2, 3],[1, 2, 3],[1, 2, 3]]),  ('m2', [[1, 2, 3],[1, 2, 3],[1, 2, 3]])])
