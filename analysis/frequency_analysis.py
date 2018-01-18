import util
import numpy as np
from matplotlib import pyplot as plt


class FrequencyAnalysis:
    def __init__(self, text):
        self.frequency = [0 for i in range(26)]
        self.text = text.lower()

    def analyze(self):
        for i in range(len(self.text)):
            char = self.text[i]
            if util.is_letter(char):
                charcode = util.to_number(char)
                self.frequency[charcode] += 1

    def plot(self):
        letters = [util.to_letter(i) for i in range(26)]
        xpos = np.arange(len(letters))
        width = 0.5
        plt.bar(xpos, self.frequency, width)
        plt.xticks(xpos, letters)
        plt.xlabel('Letter')
        plt.ylabel('Frequency')
        plt.title('')
        plt.show()
