import pickle
import matplotlib.pyplot as plt

# plots the line grah of the time taken to processing each frame captured from the camera.
def plotLatencyTimes(filePath):
    with open(filePath, "rb") as fp:   # Unpickling
        y = pickle.load(fp)

    x = [no for no in range(1, len(y)+1)]
    plt.plot(x, y)  # Plot the chart

    plt.xlabel("points")  # add X-axis label
    plt.ylabel("Latency Times")  # add Y-axis label
    plt.title("Latency Times line Chart")  # add title

    plt.show() 

# plots the line chart for the eye ratio values by reading the values from the file path passed as argument.
def plotEyeRatios(filePath):
    with open(filePath, "rb") as fp:   # Unpickling
        y = pickle.load(fp)

    x = [no for no in range(1, len(y)+1)]
    plt.plot(x, y)  # Plot the chart

    plt.xlabel("points")  # add X-axis label
    plt.ylabel("Eye Blinking Ratio")  # add Y-axis label
    plt.title("Eye Blinking Ratio")  # add title

    plt.show() 

# plots the line chart for the mouth ratio values by reading values from the file path passed as argument
def plotMouthRatios(filePath):
    with open(filePath, "rb") as fp:   # Unpickling
        y = pickle.load(fp)

    x = [no for no in range(1, len(y)+1)]

    plt.plot(x, y)  # Plot the chart

    plt.xlabel("points")  # add X-axis label
    plt.ylabel("Mouth Ratio")  # add Y-axis label
    plt.title("Mouth Ratio")  # add title

    plt.show() 

# plots the line chart for both mouth ration and eye ration from the file paths specified in the arguments.
def plotMouthAndEyeBlinkingRatios(mouthRatioFilePath, eyeRatioFilePath):
    with open(mouthRatioFilePath, "rb") as fp:   # Unpickling
        y1 = pickle.load(fp)

    with open(eyeRatioFilePath, "rb") as fp:   # Unpickling
        y2 = pickle.load(fp)

    x = [no for no in range(1, len(y1)+1)]

    fig, (ax1, ax2) = plt.subplots(2)
    fig.suptitle('Mouth and Eye Ratios')
    ax1.plot(x, y1)
    ax2.plot(x, y2)

    plt.show()

testFileName = "data/eyeBlinkingData3"

# mouthData2
# eyeBlinkingData2

# plotEyeRatios(testFileName)
plotLatencyTimes("data/latencyTimes2")



