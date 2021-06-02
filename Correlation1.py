import csv
import pandas as pd
import plotly.express as px
import numpy as np





def datasource(data):
    coffee=[]
    sleep=[]
    with open ("coffeevssleep.csv") as f:
        df=csv.DictReader(f)
        for i in df:
            coffee.append(float(i["Coffee in ml"]))
            sleep.append(float(i["sleep in hours"]))
    return {'x':coffee,'y':sleep}

def findCorrelation(datasource):
    correlation=np.corrcoef(datasource["x"],datasource["y"])
    print(correlation)   


def setup():
    datapath="coffeevssleep.csv"
    datasource1=datasource(datapath)
    findCorrelation(datasource1)

setup()   


