
from random import choice
from numpy import array, dot, random
rs = lambda x: 0 if x < 0 else 1
training_data = [ (array([0,0,1]), 0),
                    (array([0,1,1]), 1),
                    (array([1,0,1]), 1),
                    (array([1,1,1]), 1), ]
weights = random.rand(3)
errors = []
learning_rate = 0.2
num_iterations = 100
 
for i in range(num_iterations):
    input, truth = choice(training_data)
    result = dot(weights, input)
    error = truth - rs(result)
    errors.append(error)
    weights += learning_rate * error * input
    
for x, w in training_data:
    result = dot(x, w)
    print("{}: {} -> {}".format(input[:2], result, rs(result)))

