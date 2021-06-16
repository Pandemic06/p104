import csv 
import pandas as pd
import statistics

df=pd.read_csv("SOCR-HeightWeight.csv")
weight=df["Weight(Pounds)"].tolist()
mean=statistics.mean(weight)
median=statistics.median(weight)
mode=statistics.mode(weight)
print(mean)
print(median)
print(mode)
minimum=min(weight)
maximum=max(weight)
print(minimum)
print(maximum)