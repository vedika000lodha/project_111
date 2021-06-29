import csv
import pandas as pd 
import statistics 
import plotly.figure_factory as ff 
import plotly.graph_objects as go
import random

df = pd.read_csv("medium_data.csv")
data = df["reading_time"].tolist()
population_mean = statistics.mean(data)
fig = ff.create_distplot([data], ["reading_time"], show_hist = False)
fig.show()

population_std_dev = statistics.stdev(data)
print("population mean : ", population_mean)
print("population standard deviation : ", population_std_dev)

def random_set_of_mean(counter):
    dataset = []
    for i in range(0, counter):
        random_index = random.randint(0, len(data)-1)
        value = data[random_index]
        dataset.append(value)
    
    mean = statistics.mean(dataset)
    return mean

mean_list = []
for i in range(0, 100):
    set_of_means = random_set_of_mean(30)
    mean_list.append(set_of_means)


std_dev = statistics.stdev(mean_list)
mean = statistics.mean(mean_list)
print("mean of sampling distribution : ", mean)
print("std dev of sampling distibution : ", std_dev)

fig =  ff.create_distplot([mean_list],["reading time"], show_hist = False)
fig.add_trace(go.Scatter(x = [mean, mean], y = [0, 0.8], mode = "lines", name = "mean"))
fig.show()

first_sdv_start, first_sdv_end = mean-std_dev, mean+std_dev
second_sdv_start, second_sdv_end = mean-2*std_dev, mean+2*std_dev
third_sdv_start, third_sdv_end = mean-3*std_dev, mean+3*std_dev
print("first stdev : ", first_sdv_start, first_sdv_end)
print("second stdev : ", second_sdv_start, second_sdv_end)
print("third stdev : ", third_sdv_start, third_sdv_end)

fig = ff.create_distplot([mean_list],["reading time"], show_hist = False)
fig.add_trace(go.Scatter(x = [mean,mean], y = [0, 0.8], mode = "lines", name = "mean"))
fig.add_trace(go.Scatter(x = [first_sdv_start,first_sdv_start], y = [0, 0.8], mode = "lines", name = "first stdev start"))
fig.add_trace(go.Scatter(x = [first_sdv_end,first_sdv_end], y = [0, 0.8], mode = "lines", name = "first stdev end"))
fig.add_trace(go.Scatter(x = [second_sdv_start,second_sdv_start], y = [0, 0.8], mode = "lines", name = "second stdev start"))
fig.add_trace(go.Scatter(x = [second_sdv_end,second_sdv_end], y = [0, 0.8], mode = "lines", name = "sesond stdev end"))
fig.add_trace(go.Scatter(x = [third_sdv_start,third_sdv_start], y = [0, 0.8], mode = "lines", name = "third stdev start"))
fig.add_trace(go.Scatter(x = [third_sdv_start,third_sdv_start], y = [0, 0.8], mode = "lines", name = "third stdev end"))
fig.show()

zscore = (population_mean - mean)/population_std_dev
print("z score : ",zscore)