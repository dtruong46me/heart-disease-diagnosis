import os
from ig import read_data, get_threshold

def main():
    filename = 'heart_disease.csv'
    filepath = os.path.join(os.path.dirname(__file__),filename)

    attribute, data = read_data(filepath)

    table_data = []
    for attr_col in range(len(attribute)):
        avg, max_ig, max_attr_val = get_threshold(data, attr_col)
        table_data.append([attr_col,attribute[attr_col], avg, max_ig, max_attr_val])
    
    # print table
    col_names = ['col', 'attribute', 'average', 'max_ig', 'attr_val']
    col_widths = [int(len(col_names[x])) for x in range(len(col_names))]
    col_aligns = ['<' for _ in range(len(col_names))]

    lines = []
    title_line = '+' + '+'.join(['-' * (w+2) for w in col_widths]) + '+'
    lines.append(title_line)

    head_line = '| ' + ' | '.join([f'{name:<{width}}' for name, width in zip(col_names, col_widths)]) + ' |'
    lines.append(head_line)
    lines.append(title_line)

    for value in table_data:
        row = list(value)
        row[2] = '{:.3f}'.format(row[2])
        row[3] = '{:.4f}'.format(row[3])

        row_line = '| ' + ' | '.join([f'{str(val):<{width}}' for val, width in zip(row, col_widths)]) + ' |'
        lines.append(row_line)
    lines.append(title_line)

    for line in lines:
        print(line)

if __name__ == '__main__':
    main()