import csv
import os
import numpy as np
import matplotlib.pyplot as plt

from decimal import *


def process_file(file_name):
    """
    Reads given file and sums sepal and petal length for all three classes of iris plant

    :param file_name: csv file to be read and processed
    :return: Dictionary of iris classes and their average sepal and petal length
    """
    iris_classes = {'Iris-setosa': [0, 0], 'Iris-versicolor': [0, 0], 'Iris-virginica': [0, 0]}

    # open file
    with open(file_name, 'r', newline='') as csvfile:
        # read file
        reader = csv.reader(csvfile)
        for row in reader:
            # sum sepal length
            iris_classes[row[4]][0] += Decimal(row[0])
            # sum petal length
            iris_classes[row[4]][1] += Decimal(row[2])

    return iris_classes


def process_result(result):
    """
    Prints out average sepal and petal lengths for each iris  class and returns a 2 lists of corresponding values

    :param result: dictionary of iris class with sum of sepal and petal length
    :return: list of average sepal length and list of average petal length
    """
    sepal_length = []
    petal_length = []

    # iterate through each iris class
    for k, v in result.items():
        # average sepal length
        v[0] = v[0] / 50
        # average petal length
        v[1] = v[1] / 50
        
        sepal_length.append(v[0])
        petal_length.append(v[1])

        # print average sepal and petal length
        print()
        print(f'{k}:')
        print(f'Average sepal Length: {v[0]}')
        print(f'Average petal Length: {v[1]}')
    
    return sepal_length, petal_length


def plot_result(sepal, petal):
    """
    Plot a double bar graph of each iris class and their average sepal and petal lengths

    :param sepal: list of average sepal length
    :param petal: list of average petal length
    :return: None
    """
    index = np.arange(3)
    bar_width = 0.3

    # bar 1: sepal length
    p1 = plt.bar(index, sepal, bar_width)

    # bar 2: petal length
    p2 = plt.bar(index + bar_width, petal, bar_width)

    # plot configuration
    plt.xlabel('Iris Class')
    plt.ylabel('Length (cm)')
    plt.title('Iris Class Average Length')
    plt.xticks(index + (bar_width / 2), ('Iris-setosa', 'Iris-versicolor', 'Iris-virginica'))
    plt.legend((p1, p2), ('Average Sepal Length',  'Average Petal Length'))
    
    plt.tight_layout()

    # check if output folder exits. If it doesn't, create it
    if not os.path.exists('./output'):
        os.makedirs('./output')

    plt.savefig('./output/iris.png')


if __name__ == "__main__":
    result_dict = process_file('./input/iris.csv')
    sepal_lengths, petal_lengths = process_result(result_dict)
    plot_result(sepal_lengths, petal_lengths)
