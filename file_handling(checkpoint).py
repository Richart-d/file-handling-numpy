# File Handling: File Handling Checkpoint

import numpy as np

with open("Loan.csv", "r") as f:
    data = f.read()

data = np.genfromtxt("Loan.csv", delimiter=",", usecols=8, filling_values=0)

## creating a 1D array
array = np.array(data)

#calculating the mean, median and standard deviation of the loan_amount array
mean = np.mean(array)
print(f"The mean is: {mean}")

median = np.median(array)
print(f"\nThe median is: {median}")

std = np.std(array)
print(f"\nThe std is: {std}")

