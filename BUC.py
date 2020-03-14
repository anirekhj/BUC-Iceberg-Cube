import csv


def partition(dataset_list, dimension_index, dimension_attributes, lst):
    item = []
    for attribute in dimension_attributes:
        item.append(sum(list(map(int, [(i[4] if i[dimension_index] == attribute else 0) for i in dataset_list]))))
    lst[dimension_index] = item


def new_input(dataset_list, d, dimension_attribute_name):
    res = [i for i in dataset_list if i[d] == dimension_attribute_name]
    return res


min_sup = 93
records = []
headers = []
with open('Product_Sales_Data_Set.csv', newline='', encoding='utf-8-sig') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',')
    for row in spamreader:
        records.append(row)

headers = records[0]
records = records[1:]

items = ['Computer', 'Camera', 'Phone', 'Printer']
locations = ['Toronto', 'Vancouver', 'New York', 'Chicago']
years = ['2017', '2018']
dimensions = [items, locations, years]

dataCount = [[None], [None], [None]]


def BUC(input, d):
    x = input
    while d < 3:
        C = len(dimensions[d])
        if (d == 1 and len(input) == 128) or (d == 2 and len(input) == 32):
            break
        partition(input, d, dimensions[d], dataCount)
        tc = dataCount
        for i in range(C):
            c = tc[d][i]
            if c >= min_sup:
                print('\t\t' * 2*d, end="")
                print(dimensions[d][i] + '\t' + str(c))
                BUC(new_input(input, d, dimensions[d][i]), d + 1)
            else:
                print('\t\t' * 2*d, end="")
                print(dimensions[d][i] + '\t' + '*')
                BUC(new_input(input, d, dimensions[d][i]), d + 1)
        d = d + 1


BUC(records, 0)