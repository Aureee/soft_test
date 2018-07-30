# read data by importing from csv file
#import numpy as np
#
#age = np.loadtxt("participants.tsv", skiprows=1, usecols=3)
#
#mean_age = sum(age)/len(age)
#
#np.savetxt("demeaned_age.txt", age-mean_age)
#
#print("done!")


# read data directly from command line
import sys
import numpy as np
import pandas as pd

#age = np.loadtxt(sys.argv[1], skiprows=1, usecols=1)
df = pd.read_csv(sys.argv[1],sep='\t')

mean_age = sum(df.age)/len(df.age)
assert mean_age < 100
assert mean_age > 10

np.savetxt("demeaned_" + sys.argv[1], age-mean_age)


print("done!")
