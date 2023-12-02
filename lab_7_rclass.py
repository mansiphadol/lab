#single layer perceptron final
import numpy as np

NUM_FEATURES = 4
LEARNING_RATE = 0.1
ITER = 100

def dot_product(weights, input):
    return np.dot(weights, input)

def update_weights(weights, input, desired_output, actual_output):
    error = desired_output - actual_output
    weights += LEARNING_RATE * error * input

def main():
    Wo = np.array([1, -1, 0, 0.5])
    X1 = np.array([1, -2, 1.5, 0])
    X2 = np.array([1, -0.5, -2, -1.5])
    X3 = np.array([0, 1, -1, 1.5])
    d1 = 1
    d2 = -1
    d3 = 1

    for iteration in range(ITER):
        error_count = 0

        # Train with X1
        output1 = dot_product(Wo, X1)
        actual_output1 = 1 if output1 > 0 else -1
        print("O1"+str(actual_output1))
        if actual_output1 != d1:
            update_weights(Wo, X1, d1, actual_output1)
            error_count += 1

        # Train with X2
        output2 = dot_product(Wo, X2)
        actual_output2 = 1 if output2 > 0 else -1
        print("O2"+str(actual_output2))
        if actual_output2 != d2:
            update_weights(Wo, X2, d2, actual_output2)
            error_count += 1

        # Train with X3
        output3 = dot_product(Wo, X3)
        actual_output3 = 1 if output3 > 0 else -1
        print("O3"+str(actual_output3))
        if actual_output3 != d3:
            update_weights(Wo, X3, d3, actual_output3)
            error_count += 1

        if error_count == 0:
            print(f"error count is 0")
            print(f"Perceptron converged after {iteration + 1} iterations.")
            break

    print("Trained Weights (Wo):", " ".join(f"{w:.2f}" for w in Wo))

if __name__ == "__main__":
    main()
