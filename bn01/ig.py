import csv
import math

def read_data(filename):
    with open(filename, newline='') as f:
        data = []
        csv_reader = csv.reader(f, delimiter=',')
        for row in csv_reader:
            data.append(row)
    attribute = data[0]

    return attribute, data[1:]

def average_attribute(data, attr_col:int) -> float:
    sum = 0
    for row in data:
        sum += float(row[attr_col])
    avg = sum / len(data)

    return avg

def get_threshold(data, attr_col):
    avg = average_attribute(data, attr_col)

    max_ig = -1
    max_attr_val = -1

    for attr_val in range(int(avg)-50, int(avg)+50):
        if information_gain(data,attr_col,attr_val) > max_ig:
            max_ig = information_gain(data,attr_col,attr_val)
            max_attr_val = attr_val
    
    return avg, max_ig, max_attr_val

def entropy(data) -> float:
    count = {}
    for row in data:
        label = row[-1]
        if label not in count:
            count[label] = 0
        count[label] += 1
    entropy = 0

    for label in count:
        p_label = count[label] / len(data)
        entropy -= p_label * math.log2(p_label)
    return entropy

def information_gain(data, col_attr:int, thressold:float) -> float:
    positive_rows, negative_rows = [],[]

    for row in data:
        if float(row[col_attr]) >= thressold:
            positive_rows.append(row)
        elif float(row[col_attr]) < thressold:
            negative_rows.append(row)

    # Entropy = 0 if all samples in S have the same size
    if len(positive_rows) == 0 or len(negative_rows) == 0:
        return 0
    
    # print(positive_rows, type(positive_rows), len(positive_rows))
    
    pos_ratio = len(positive_rows) / len(data)
    neg_ratio = len(negative_rows) / len(data)

    ig = entropy(data) - (pos_ratio * entropy(positive_rows) + neg_ratio * entropy(negative_rows))

    return ig




'''
+-----+-----------+---------+--------+----------+
| col | attribute | average | max_ig | attr_val |
+-----+-----------+---------+--------+----------+
| 0   | age       | 54.434  | 0.0610 | 55       |
| 1   | sex       | 0.696   | 0.0580 | 1        |
| 2   | cp        | 0.942   | 0.2046 | 1        |
| 3   | trestbps  | 131.612 | 0.0160 | 107      |
| 4   | chol      | 246.000 | 0.0195 | 274      |
| 5   | fbs       | 0.149   | 0.0012 | 1        |
| 6   | restecg   | 0.530   | 0.0186 | 1        |
| 7   | thalach   | 149.114 | 0.1281 | 148      |
| 8   | exang     | 0.337   | 0.1451 | 1        |
| 9   | oldpeak   | 1.072   | 0.1249 | 1        |
| 10  | slope     | 1.385   | 0.1124 | 2        |
| 11  | ca        | 0.754   | 0.1629 | 1        |
| 12  | thal      | 2.324   | 0.1737 | 3        |
| 13  | target    | 0.513   | 0.9995 | 1        |
+-----+-----------+---------+--------+----------+

---------------------------------------------------------------------------
    # for i in range(len(table_data)):
    #     row = list(table_data[i])
    #     row[2] = '{:.4f}'.format(row[2])
    #     row[3] = '{:.4f}'.format(row[3])
    #     table_data[i] = tuple(row)
        
    # lines = []
    # lines.append('+{:-<5}+{:-<11}+{:-<10}+{:-<8}+{:-<10}+'.format('', '', '', '', ''))
    # header = '| {:<3} | {:<9} | {:<7}  | {:<6} | {:<8} |'.format('col', 'attribute', 'average', 'max_ig', 'attr_val')
    # lines.append(header)
    # lines.append('+{:-<5}+{:-<11}+{:-<10}+{:-<8}+{:-<10}+'.format('', '', '', '', ''))
    # for row in table_data:
    #     row_line = '| {:<3} | {:<9} | {:<8} | {:<6} | {:<8} |'.format(*row)
    #     lines.append(row_line)
    #     lines.append('+{:-<5}+{:-<11}+{:-<10}+{:-<8}+{:-<10}+'.format('', '', '', '', ''))

    # table = '\n'.join(lines)
    # print(table)
RESULT:
+-----+-----------+----------+--------+----------+
| col | attribute | average  | max_ig | attr_val |
+-----+-----------+----------+--------+----------+
| 0   | age       | 54.4341  | 0.0610 | 55       |
+-----+-----------+----------+--------+----------+
| 1   | sex       | 0.6956   | 0.0580 | 1        |
+-----+-----------+----------+--------+----------+
| 2   | cp        | 0.9424   | 0.2046 | 1        |
+-----+-----------+----------+--------+----------+
| 3   | trestbps  | 131.6117 | 0.0160 | 107      |
+-----+-----------+----------+--------+----------+
| 4   | chol      | 246.0000 | 0.0195 | 274      |
+-----+-----------+----------+--------+----------+
| 5   | fbs       | 0.1493   | 0.0012 | 1        |
+-----+-----------+----------+--------+----------+
| 6   | restecg   | 0.5298   | 0.0186 | 1        |
+-----+-----------+----------+--------+----------+
| 7   | thalach   | 149.1141 | 0.1281 | 148      |
+-----+-----------+----------+--------+----------+
| 8   | exang     | 0.3366   | 0.1451 | 1        |
+-----+-----------+----------+--------+----------+
| 9   | oldpeak   | 1.0715   | 0.1249 | 1        |
+-----+-----------+----------+--------+----------+
| 10  | slope     | 1.3854   | 0.1124 | 2        |
+-----+-----------+----------+--------+----------+
| 11  | ca        | 0.7541   | 0.1629 | 1        |
+-----+-----------+----------+--------+----------+
| 12  | thal      | 2.3239   | 0.1737 | 3        |
+-----+-----------+----------+--------+----------+
| 13  | target    | 0.5132   | 0.9995 | 1        |
+-----+-----------+----------+--------+----------+

---------------------------------------------------------------------------
    # align = 18
    # print("{:<{align}}: {}".format("Average attribute", avg, align=align))
    # print("{:<{align}}: {}".format("Maximum of IG", max_ig, align=align))
    # print("{:<{align}}: {}".format("Attribute value", max_attr_val, align=align))
RESULT:
Average attribute : 0.14926829268292682
Maximum of IG     : 0.0012222219885129615
Attribute value   : 1
'''
