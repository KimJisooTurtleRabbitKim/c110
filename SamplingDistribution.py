import pandas as pd
import plotly.figure_factory as ff
import plotly.graph_objects as go
import statistics
import random as rd

df = pd.read_csv("Newdata.csv")
data = df["Index"].tolist()

#figure = ff.create_distplot([data],["temp"],show_hist=False)
#figure.show()
mean = statistics.mean(data)
standardDeviation = statistics.stdev(data)
print("mean of entire data set is ",mean)
print("standard deviation of whole data set is ",standardDeviation)

def random_setOf_data():
    dataSet = []
    for i in range(0,100):
        randomIndex = rd.randint(0,len(data)-1)
        dataSet.append(data[randomIndex])
    mean = statistics.mean(dataSet)
    return mean

def main():
    meanList = []
    for i in range(0,1000):
        meanOf_Data_Set = random_setOf_data()
        meanList.append(meanOf_Data_Set)
    samplingMean = statistics.mean(meanList)
    standard_Deviation_Ofsampling = statistics.stdev(meanList)
    print("mean of sampling distribution is ",samplingMean)
    print("standard deviation of sampling distribution  is ",standard_Deviation_Ofsampling)

    figure = ff.create_distplot([meanList],["Sampling Distribution"],show_hist=False)
    figure.show()

main()

        
        
    