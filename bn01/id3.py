import os
from ig import read_data
from ig import entropy, get_threshold

class Node:
    def __init__(self, attribute, attribute_val, avg):
        self.attribute = attribute
        self.attribute_val = attribute_val
        self.avg = avg
        self.child = {}

    def add_child(self, value, node):
        self.child[value] = node

def id3(data, attributes):
    
    labels = [row[-1] for row in data]
    # print(labels,len(labels))

    if labels.count(labels[0]) == len(labels):
        return labels[0]
    
    if len(attributes) == 0:
        return most_common_label(labels)
    
    entropy_s = entropy(data)
    
    max_ig = -1
    best_attribute = None
    for attribute in attributes:
        avg, ig, attr_val = get_threshold(data, attribute)
        if ig > max_ig:
            max_ig = ig
            best_attribute = (attribute, attr_val, avg)

    if max_ig < 0.01:
        return most_common_label(labels)
    
    node = Node(best_attribute[0], best_attribute[1], best_attribute[2])
    attribute_values = get_attribute_values(data, best_attribute[0])

    for value in attribute_values:
        sub_data = get_sub_data(data, best_attribute[0], value)
        if sub_data:
            child_node = id3(sub_data, [attr for attr in attributes if attr != best_attribute[0]])
            node.add_child(value, child_node)
    
    return node

def get_sub_data(data, attribute, value):
    """
    Trả về tập dữ liệu con chứa các mẫu có giá trị của thuộc tính attribute bằng value.
    """
    sub_data = []
    for row in data:
        if row[attribute] == value:
            sub_data.append(row)
    return sub_data


def get_attribute_values(data, attribute):
    """Trả về danh sách các giá trị khác nhau của thuộc tính attribute trong tập dữ liệu data."""
    return list(set([row[attribute] for row in data]))


def most_common_label(labels:list):
    label_count = {}
    for label in labels:
        if label in label_count:
            label_count[label] += 1
        else:
            label_count[label] = 1
    
    most_common = None
    cnt = 0
    for label, num in label_count.items():
        if num > cnt:
            most_common = label
            cnt = num

    return most_common

def main():
    filename = 'heart_disease.csv'
    filepath = os.path.join(os.path.dirname(__file__),filename)

    attribute, data = read_data(filepath)
    id3(data,attribute[:-1])
    

if __name__ == '__main__':
    main()