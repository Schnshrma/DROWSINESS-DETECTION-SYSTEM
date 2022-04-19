import pickle
import matplotlib.pyplot as plt

# with open("eyeBlinkingData", "rb") as fp:   # Unpickling
#     y = pickle.load(fp)

# x = [no for no in range(1, len(y)+1)]
# plt.plot(x, y)  # Plot the chart

# plt.xlabel("points")  # add X-axis label
# plt.ylabel("Eye Blinking Ratio")  # add Y-axis label
# plt.title("Eye Blinking Ratio")  # add title

# plt.show() 


# with open("mouthData", "rb") as fp:   # Unpickling
#     y = pickle.load(fp)

# x = [no for no in range(1, len(y)+1)]

# plt.plot(x, y)  # Plot the chart

# plt.xlabel("points")  # add X-axis label
# plt.ylabel("Mouth Ratio")  # add Y-axis label
# plt.title("Mouth Ratio")  # add title

# plt.show() 


with open("mouthData2", "rb") as fp:   # Unpickling
    y1 = pickle.load(fp)

with open("eyeBlinkingData2", "rb") as fp:   # Unpickling
    y2 = pickle.load(fp)

x = [no for no in range(1, len(y1)+1)]

fig, (ax1, ax2) = plt.subplots(2)
fig.suptitle('Mouth and Eye Ratios')
ax1.plot(x, y1)
ax2.plot(x, y2)

plt.show()