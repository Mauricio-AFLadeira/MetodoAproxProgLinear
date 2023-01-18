destination = ['Afeganistão',
               'Argélia',
               'Brasil',
               'Canadá',
               'França',
               'Gana',
               'Hungria',
               'Indonesia',
               'Japão',
               'Líbano',
               'Malásia',
               'Marrocos',
               'México',
               'Nepal',
               'Paquistão',
               'Peru',
               'Portugal',
               'Quênia',
               'Romenia',
               'Ruanda',
               'Samoa',
               'Singapura',
               'Tunisia',
               'Uruguai',
               'Zimbabue']

origin = ['Brasil',
          'Canadá',
          'França',
          'Japão',
          'Singapura',
          'Zimbabue']

matrix = [
    [6.69,9.55,0.00,8.28,5.10,5.41,5.73,7.96,7.64,8.92,4.78,5.10,3.82,8.28,8.60,8.92,3.50,4.78,6.69,4.78,4.14,3.18,4.14,6.37,4.46],
    [8.92,5.41,3.50,0.00,8.60,7.64,4.14,7.96,8.92,9.55,5.73,7.96,5.73,8.60,9.55,4.14,4.14,7.01,7.96,6.69,3.50,7.96,4.14,7.32,7.01],
    [5.73,6.05,6.69,3.50,0.00,3.50,7.01,8.92,4.14,9.55,8.28,6.05,8.28,8.60,9.24,8.28,3.18,4.78,5.73,8.92,5.41,7.64,6.69,4.14,5.41],
    [6.05,6.69,3.18,7.01,6.37,9.55,5.73,6.37,0.00,6.05,8.60,7.32,7.96,3.50,6.37,9.24,3.18,3.18,4.14,4.14,6.05,5.10,4.46,9.55,7.32],
    [5.41,4.46,6.05,9.55,4.78,8.92,5.10,8.60,4.14,8.92,4.14,4.78,4.14,6.37,3.18,3.50,6.05,5.10,5.73,3.50,7.64,0.00,6.69,4.78,4.78],
    [7.96,3.82,5.41,9.55,6.69,9.24,7.96,6.37,7.96,3.50,8.28,5.73,9.55,5.73,9.24,5.73,6.05,8.60,7.64,3.18,7.64,6.37,7.96,9.55,0.00]
          
    ]


availability = [7500, 8100, 4900, 5300, 3900, 3600]

need = [1673, 963, 1444, 1282, 2193, 782, 683, 906, 1195, 962, 1782, 1147,
        1711, 1441, 1878, 1172, 1254, 548, 643, 1986, 929, 2173, 1907, 1908, 666]


result_matrix = []


def reset_result_matrix():
    column = []
    for i in range(0, len(matrix)):
        for j in range(0, len(matrix[0])):
            column.append(0)
        result_matrix.append(column.copy())
        column.clear()


def sum_without_none(iterable):
    result = 0
    for number in iterable:
        if number is not None:
            result += number
    return result


def insert_artificial_origin():
    origin.append('dummy')
    line = []
    for i in range(0, len(destination)):
        line.append(0)
    matrix.append(line)
    availability.append(sum(need) - sum(availability))


def insert_artificial_destination():
    destination.append('dummy')
    for line in matrix:
        line.append(999)
    need.append(sum(availability) - sum(need))


def calculate_penalties():
    origin_penalty = []
    destination_penalty = []
    column = []

    for i, line in enumerate(matrix):
        origin_penalty.append(difference_lower_costs(
            iterable_without_none(line.copy(), need)))

    for j in range(0, len(matrix[0])):
        for k in range(0, len(matrix)):
            column.append(matrix[k][j])
        destination_penalty.append(difference_lower_costs(
            iterable_without_none(column, availability)))
        column.clear()

    return [origin_penalty, destination_penalty]


def difference_lower_costs(iterable):

    best = min(iterable)
    iterable.remove(best)

    if len(iterable) == 0:
        return best

    alternative = min(iterable)

    return abs(alternative - best)


def get_column(index):
    column = []
    for j in range(0, len(matrix)):
        column.append(matrix[j][index])
    return column


def iterable_without_none(iterable, comparable=None):
    iterable_remove_none = []
    for i, x in enumerate(iterable):
        if comparable is not None:
            if comparable[i] is not None:
                iterable_remove_none.append(x)
        else:
            if iterable[i] is not None:
                iterable_remove_none.append(x)
    return iterable_remove_none


def find_lower_cell(origin_penalty, destination_penalty):
    result = []

    max_difference_origin = max(origin_penalty)
    max_difference_destination = max(destination_penalty)

    if max_difference_origin < max_difference_destination:
        index_max_difference = destination_penalty.index(
            max_difference_destination)
        result.append(index_max_difference)
        column = get_column(index_max_difference)
        lower_cost_value = min(iterable_without_none(column, availability))
        result.append(lower_cost_value)
        result.append(column.index(lower_cost_value))
    else:
        index_max_difference = origin_penalty.index(max_difference_origin)
        result.append(index_max_difference)
        line = matrix[index_max_difference]
        lower_cost_value = min(iterable_without_none(line, need))
        result.append(lower_cost_value)
        result.append(line.index(lower_cost_value))
        result.reverse()

    return result


def calculate_result():
    z = 0
    for i in range(0, len(result_matrix)):
        for j in range(0, len(result_matrix[0])):
            z += result_matrix[i][j]
    return z


def main():
    if sum(need) > sum(availability):
        insert_artificial_origin()
    elif sum(availability) > sum(need):
        insert_artificial_destination()

    reset_result_matrix()

    while (sum_without_none(availability) + sum_without_none(need)) != 0:

        origin_penalty, destination_penalty = calculate_penalties()
        index_column_need, lower_cost_value, index_line_availability = find_lower_cell(
            origin_penalty, destination_penalty)

        value_availability = availability[index_line_availability]
        value_need = need[index_column_need]

        if value_need < value_availability:
            result_matrix[index_line_availability][index_column_need] = lower_cost_value * value_need
            for i in range(0, len(matrix)):
                matrix[i][index_column_need] = 0
            need[index_column_need] = None
            availability[index_line_availability] -= value_need
        else:
            result_matrix[index_line_availability][index_column_need] = lower_cost_value * \
                value_availability
            for i in range(0, len(matrix[0])):
                matrix[index_line_availability][i] = 0
            availability[index_line_availability] = None
            need[index_column_need] -= value_availability


main()
# print(result_matrix)
print(calculate_result())