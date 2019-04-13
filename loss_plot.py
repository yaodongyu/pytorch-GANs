import pickle
import sys
import matplotlib.pyplot as plt

hist = {}

filename = sys.argv[1]
print(filename)

with open(filename, 'rb') as f:
    hist = pickle.load(f)
print(hist)

x = range(len(hist['D_loss']))

y1 = hist['D_loss']
y2 = hist['G_loss']

plt.plot(x, y1, label='D_loss')
plt.plot(x, y2, label='G_loss')

plt.xlabel('Iter')
plt.ylabel('Loss')

plt.legend(loc=4)
plt.grid(True)
plt.tight_layout()

path = os.path.join(path, model_name + '_loss.png')

plt.savefig(path)

plt.close()

