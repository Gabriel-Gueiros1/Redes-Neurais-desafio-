import numpy as np

inputs = np.array([[1, 2, 3, 2.5],
                   [2, 5, -1, 2],
                   [-1.5, 2.7, 3.3, -0.8]])

weights = np.array([[0.2, 0.8, -0.5, 1],
                    [0.5, -0.91, 0.26, -0.5],
                    [-0.26, -0.27, 0.17, 0.87]])

biases = np.array([2, 3, 0.5])

weights2 = np.array([[0.1, -0.14, 0.5],
                     [-0.5, 0.12, -0.33],
                     [-0.44, 0.73, -0.13]])

biases2 = np.array([-1, 2, -0.5])


layer1_output = np.dot(inputs, weights.T) + biases

output = np.dot(layer1_output, weights2.T) + biases2

print("Output:\n", output)
