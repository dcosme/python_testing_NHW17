import sys
import numpy as np
import pandas

age = pd.read_csv(sys.argv[1], sep="\t").age

#age = np.loadtxt(sys.argv[1], skiprows=1, usecols=2)

mean_age = sum(age)/len(age)

np.savetxt("demeaned_" + sys.argv[1], age-mean_age)

assert mean_age < 100
assert mean_age > 10 

print("done!")