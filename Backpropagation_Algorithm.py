import numpy as np

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

x = np.array([0.0, 1.0])
target = 1.0
lr = 0.25

v11, v21, v01 = 0.6, -0.1, 0.3
v12, v22, v02 = -0.3, 0.4, 0.5
w1, w2, w0 = 0.4, 0.1, -0.2

z1_in = v01 + x[0] * v11 + x[1] * v21
z2_in = v02 + x[0] * v12 + x[1] * v22

z1 = sigmoid(z1_in)
z2 = sigmoid(z2_in)

y_in = w0 + z1 * w1 + z2 * w2
y = sigmoid(y_in)

delta_output = (target - y) * y * (1 - y)
delta_hidden1 = delta_output * w1 * z1 * (1 - z1)
delta_hidden2 = delta_output * w2 * z2 * (1 - z2)

dw1 = lr * delta_output * z1
dw2 = lr * delta_output * z2
dw0 = lr * delta_output

dv11 = lr * delta_hidden1 * x[0]
dv21 = lr * delta_hidden1 * x[1]
dv01 = lr * delta_hidden1

dv12 = lr * delta_hidden2 * x[0]
dv22 = lr * delta_hidden2 * x[1]
dv02 = lr * delta_hidden2

print("Forward Pass")
print("z1 =", round(z1, 4))
print("z2 =", round(z2, 4))
print("Output =", round(y, 4))

print("\nUpdated Weights")
print("v11 =", round(v11 + dv11, 5))
print("v21 =", round(v21 + dv21, 5))
print("v01 =", round(v01 + dv01, 5))
print("v12 =", round(v12 + dv12, 5))
print("v22 =", round(v22 + dv22, 5))
print("v02 =", round(v02 + dv02, 5))
print("w1 =", round(w1 + dw1, 5))
print("w2 =", round(w2 + dw2, 5))
print("w0 =", round(w0 + dw0, 5))
