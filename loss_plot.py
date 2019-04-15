import pickle
import sys
import os
import matplotlib.pyplot as plt

hist = {}

filename = sys.argv[1]
print(filename)

with open(filename, 'rb') as f:
    hist = pickle.load(f)

x = range(int(len(hist['D_loss'])/20))

y1_original = hist['D_loss']
y2_original = hist['G_loss']

y1 = []
y2 = []

for index in range(int(len(hist['D_loss'])/20)):
	y1.append(sum(y1_original[index*20:index*20+20])/20)
	y2.append(sum(y2_original[index*20:index*20+20])/20)

plt.plot(x, y1, label='D_loss')
plt.plot(x, y2, label='G_loss')

plt.xlabel('Iter')
plt.ylabel('Loss')

plt.legend(loc=4)
plt.grid(True)
plt.tight_layout()

plt.show()

plt.close()
