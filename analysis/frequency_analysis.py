from util import util
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

    def plot(self, title):
        letters = [util.to_letter(i) for i in range(26)]
        xpos = np.arange(len(letters))

        width = 0.5
        bars = plt.bar(xpos, self.frequency, width)

        plt.xticks(xpos, letters)

        plt.xlabel('Letter')
        plt.ylabel('Frequency')

        plt.title(title)

        def label():
            """
            Attach a text label above each bar displaying its height
            """
            for bar in bars:
                x = bar.get_x()
                height = bar.get_height()
                plt.text(x + width / 2., height + 0.1, '%d' % int(height),
                         ha='center', va='bottom')

        label()

        def max_frequency():
            max_freq = self.frequency[0]
            for i in range(1, len(self.frequency)):
                if max_freq < self.frequency[i]:
                    max_freq = self.frequency[i]
            return max_freq

        plt.ylim([0, max_frequency() * 1.1])
        plt.show()
