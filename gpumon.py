from collections import deque
import numpy as np
import GPUtil
import matplotlib.pyplot as plt
import matplotlib.animation as animation


fig = plt.figure("gpumon", figsize=(12, 4))
ax = plt.axes(xlim=(0, 200), ylim=(0, 1))

gpus = GPUtil.getGPUs()

lines = []
y_lists = []
for gpu in gpus:
    line, = ax.plot([],[], label=f'{gpu.name}')
    y_list = deque([0]*400)
    lines.append(line)
    y_lists.append(y_list)

plt.legend(loc="upper left")
x_list = deque(np.linspace(200, 0, num=400))


def init():
    for line in lines:
        line.set_data([], [])
    return lines


def animate(i):
    gpus = GPUtil.getGPUs()
    for gpuid in range(len(gpus)):
        y_lists[gpuid].pop()
        y_lists[gpuid].appendleft(gpus[gpuid].load)
        lines[gpuid].set_data(x_list,y_lists[gpuid])
    return lines


anim = animation.FuncAnimation(fig, animate, init_func=init, frames=200, interval=100, blit=True)
plt.show()

exit(0)
