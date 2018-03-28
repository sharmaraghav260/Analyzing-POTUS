import pandas as pd
import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt

# Read top 20 words of the file
d = pd.read_csv('t20.csv')
Words = d['Word']
Frequency = d['Frequency']
y_pos = np.arange(len(Words))
plt.barh(Words, Frequency, align='center', alpha=0.5)
plt.xlabel("Frequency")
plt.yticks(y_pos)
plt.title('Top 20 Words Tweeted by @realDonaldTrump')
plt.show()
