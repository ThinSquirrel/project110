import plotly.figure_factory as ff
import statistics
import random
import pandas as pd
import csv

from class1 import randSetOfMean

df = pd.read_csv("data2.csv")

data = df["reading_time"].tolist()

graph = ff.create_distplot([data],["reading time"], show_hist = False)
graph.show()

print("Population mean is: ",statistics.mean(data))

def randSet(counter):
    dataSet = []
    for i in range(0,counter):
        random_index = random.randint(0,len(data))
        value = data[random_index]
        dataSet.append(value)
    
    mean =  statistics.mean(dataSet)
    return mean

def showGraph(meanlist):
    df = meanlist
    graph = ff.create_distplot([df],["reading time"],show_hist = False)
    graph.show()

def setup():
    meanlist = []
    
    for i in range(0,100):
        setofmean = randSetOfMean(10)
        meanlist.append(setofmean)

    showGraph(meanlist)
    print("Sample mean is: ",statistics.mean(meanlist))

setup()