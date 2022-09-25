import random
import numpy
import math
import pprint
import matplotlib.pyplot as plt

pp = pprint.PrettyPrinter(indent=4)

def bubbleSort(arr,dict):
    n = len(arr)
    distances = []
    distances.append(calculateUnorderness(arr,dict))
    for i in range(n-1):
        for j in range(0, n-i-1):
            if arr[j] > arr[j + 1] :
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
            distances.append(calculateUnorderness(arr,dict))       
    return arr,distances

def calculateUnorderness(list,dict):
    unorderness = 0
    for i in range(len(list)):
        unorderness += abs(dict[list[i]]['correct'] - i)
    return unorderness


LIST_SIZE = 25
normalized_distance_list = []

def order_distrubution():
    order_percentage_list = []
    for j in range(100000):
        to_be_ordered = []
        while(len(to_be_ordered) < LIST_SIZE):
            single_value = random.randint(0, 100)
            if single_value not in to_be_ordered:
                to_be_ordered.append(single_value)

        sorted = numpy.sort(to_be_ordered)
        value_dict = {}
        for i in range(len(to_be_ordered)):
            for j in range(len(sorted)):
                if to_be_ordered[i] == sorted[j]:
                    value_dict[to_be_ordered[i]] = {'starting' : i,'correct' : j}
                    break
        orderings = calculateUnorderness(to_be_ordered,value_dict)
        order_percentage_list.append(100-(orderings/LIST_SIZE*2))

    plt.hist(order_percentage_list,bins=100)
    plt.show()

def orderLoop():

    for j in range(100):
        to_be_ordered = []


        while(len(to_be_ordered) < LIST_SIZE):
            single_value = random.randint(0, 100)
            if single_value not in to_be_ordered:
                to_be_ordered.append(single_value)

        indices =numpy.argsort(to_be_ordered)
        sorted = numpy.sort(to_be_ordered)
    

        value_dict = {}
        for i in range(len(to_be_ordered)):
            for j in range(len(sorted)):
                if to_be_ordered[i] == sorted[j]:
                    value_dict[to_be_ordered[i]] = {'starting' : i,'correct' : j}
                    break


        sorted, distances = bubbleSort(to_be_ordered,value_dict)
        normalized_distance = [round(100-(distance/LIST_SIZE*2),1) for distance in distances]
        normalized_distance_list.append(normalized_distance)
    

    for i in range(len(normalized_distance_list)):
        plt.plot(normalized_distance_list[i])
        plt.axvline(normalized_distance_list[i].index(100.0), color='r')

    plt.show()

orderLoop()
