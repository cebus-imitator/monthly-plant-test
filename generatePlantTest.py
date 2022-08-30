#!/usr/bin/env python
# coding: utf-8

# ## Monthly Plant ID test
#
#

# load libraries
import os
import sys
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import random

from IPython.display import display, HTML
display(HTML("<style>div.output_scroll { height: 50em; }</style>"))

monero = input("Enter your 3-letter code: ").upper()
month = input("Enter test month (as integer): ")

fruit = pd.read_excel("fruits_top30_by_month.xlsx", keep_default_na = False)
fruit = fruit[(fruit['Month'].astype(str)==month)]
fruit = list(set(fruit.plant))
random.shuffle(fruit)

pictures = os.listdir("plants/")

answers = {}

for f in fruit:
    print("++++++++++++++++++++++++++++++")
    pics = [x for x in pictures if x[0:2]==f][0:6]
    random.shuffle(pics)
    if len(pics) > 0:
        fig, axarr = plt.subplots(2,3, figsize=(15, 10))
        for i in range(0,len(pics)):
            img = mpimg.imread(f"plants/{pics[i]}")
            if i < 3:
                row = 0
                col = i
            else:
                row = 1
                col = i - 3
            axarr[row,col].imshow(img)
        plt.show()
        choice = input("Enter 2-letter code of plant: ")
        entry = {f : choice}
        answers.update(entry)
        plt.close()
    else:
        print(f"no photos available for {f}")

df = pd.DataFrame(answers.items(), columns=['plant', f"answer"])
df['answer'] = df['answer'].str.upper()
df['incorrect'] = ''
df.loc[df['plant']!=df['answer'], "incorrect"] = 1
print("")
print(df)

score = df['incorrect'].sum()/len(df)
print(f"Your score: {score}")

df.to_excel(f"tests/MonthlyPlantTest_{month}_{monero}.xlsx", index=False)
sys.exit("Goodbye, and have a nice day!")

# In[ ]:
