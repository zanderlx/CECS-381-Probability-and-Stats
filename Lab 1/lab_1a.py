
import numpy as np
import matplotlib.pyplot as plt
import random

# 1
num1 = np.random.rand()
num2 = np.random.randn()
num3 = np.random.randint(50)

array1 = np.random.rand(5)
array2 = np.random.randn(5)

# Random with output as single number
print("Using np.random.rand()   :", num1)
print("Using np.random.randn()  :", num2)
print("Using np.random.randint():", num3)

# Random with output as array
print("Using np.random.rand() (Array)   :", array1)
print("Using np.random.randn() (Array)  :", array2)

# 2
# Random Walk - Not using numpy
position = 0
walk = [position]
n_steps = 500
for n in range(n_steps):
    w_step = 1 if random.randint(0,1) else -1
    position += w_step
    walk.append(position)
    
plt.plot(walk[:100], 'g')   
plt.show()

# Random Walk - Using numpy
n_steps = 500
rand_draws = np.random.randint(0, 2, size = n_steps)
w_steps = np.where(rand_draws > 0, 1, -1)
walk = w_steps.cumsum()

plt.plot(walk[:100], 'y')
plt.show()

# 3
# Random Walk - 5 Instances
n_steps = 500

# Hard coded walk
# # Process 1
# rand_draws_1 = np.random.randint(0, 2, size = n_steps)
# w_steps_1 = np.where(rand_draws_1 > 0, 1, -1)
# walk_1 = w_steps_1.cumsum()

# # Process 2
# rand_draws_2 = np.random.randint(0, 2, size = n_steps)
# w_steps_2 = np.where(rand_draws_2 > 0, 1, -1)
# walk_2 = w_steps_2.cumsum()

# # Process 3
# rand_draws_3 = np.random.randint(0, 2, size = n_steps)
# w_steps_3 = np.where(rand_draws_3 > 0, 1, -1)
# walk_3 = w_steps_3.cumsum()

# # Process 4
# rand_draws_4 = np.random.randint(0, 2, size = n_steps)
# w_steps_4 = np.where(rand_draws_4 > 0, 1, -1)
# walk_4 = w_steps_4.cumsum()

# # Process 5
# rand_draws_5 = np.random.randint(0, 2, size = n_steps)
# w_steps_5 = np.where(rand_draws_5 > 0, 1, -1)
# walk_5 = w_steps_5.cumsum()

# Looped walk
colors = ['r', 'g', 'b', 'm', 'y']
for x in colors:
    rand_draws = np.random.randint(0, 2, size = n_steps)
    w_steps = np.where(rand_draws > 0, 1, -1)
    walk = w_steps.cumsum()
    plt.plot(walk[:100], x)
plt.show()

np.random.seed()

# Hard code walk
# plt.plot(walk_1[:100], 'r')
# plt.plot(walk_2[:100], 'g')
# plt.plot(walk_3[:100], 'b')
# plt.plot(walk_4[:100], 'y')
# plt.plot(walk_5[:100], 'm')
# plt.show()

# 4
walk_list = []
n_steps = 1000
for x in colors:
    count = 0
    rand_draws = np.random.randint(0, 2, size = n_steps)
    w_steps = np.where(rand_draws > 0, 1, -1)
    walk = w_steps.cumsum()
    plt.plot (walk [:5000], x )
    for x in range(len(walk)):
        if (walk[x] == 25 or walk[x] == -25):
            walk_list.append(x)
            break
plt.show()
print (walk_list)
average  = 0

for i in range(len(walk_list)):
    average += walk_list[i]

average /= len(walk_list)

print ("Number of trials reaching +/-25 is", len(walk_list))
print ("Average from completed trials:", average)