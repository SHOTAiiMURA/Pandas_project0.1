import pandas
import pandas as pd

sushi = pd.Series(["samon","tuna","maguro","tai"])
print(sushi)
#0     samon
#1      tuna
#2    maguro
#3       tai
#dtype: object
print(sushi.index)
#RangeIndex(start=0, stop=4, step=1)
print(type(sushi.values))
#<class 'numpy.ndarray'>
##############################################################
#Excersise
# The Series below stores the number of home runs
# that a baseball player hit per game
home_runs = pd.Series([3, 4, 8, 2])

# Find the total number of home runs (i.e. the sum) and assign it
# to the total_home_runs variable below
total_home_runs = print(home_runs.sum())
#17
# Find the average number of home runs and assign it
# to the average_home_runs variable below
average_home_runs = print(home_runs.mean())
#4.25

#Parameters and arguments
fruits = ["apple","orange","plum","grape","bluberry","watermelon"]
weekdays = ["monday", "tuesday", "wednesday", "thursday", "friday","saturday"]
print(pd.Series(fruits))
print(pd.Series(weekdays))
print(pd.Series(data=fruits, index=weekdays))

mydataset = {'cars':["BMW","Volvo","Ford"],'passings':[3,7,2]}

myvar = pandas.DataFrame(mydataset)
print(myvar)

print(pd.__version__)

a = [1,7,2]

myvar2 = pd.Series(a)

print(myvar2[0])

myvar3 = pd.Series(a,index=["x","y","z"])
print(myvar3)
print(myvar3["z"])

data = {
    "calories": [430,250,508],
    "duraiton": [40,23,50]
}
#load data into a DataFrame object:
df = pd.DataFrame(data)

print(df.loc[0,1])

#df = pd.DataFrame(data, index=["day1","day2","day3"])
#print(df)

df1 = pandas.read_csv('data.csv')
print(df1.to_string())
print(df1)