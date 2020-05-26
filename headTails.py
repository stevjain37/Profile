import numpy as np

def coinFlip(p): 
    result = np.random.binomial(1,p)
    #adds result to numpy array
    return result

probability = .5
inquireFlips = input("How many flips?")
n = int(inquireFlips)

#initiate array
fullResults = np.arange(n)

for i in range(0,n):
    fullResults[i] = coinFlip(probability)
    i += 1

print("probability is set to ", probability)
print("Tails = 0, Heads = 1: ", fullResults)
print("Head Count: ", np.count_nonzero(fullResults == 1))
print("Tail Count: ", np.count_nonzero(fullResults == 0))
