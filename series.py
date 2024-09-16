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