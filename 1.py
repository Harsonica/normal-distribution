import random
import plotly.express as px
count=[]
dice = []
for i in range(0,100):
    dice1=random.randint(1,6)

    dice2=random.randint(1,6)
    count.append(i)

    dice.append(dice1+dice2)
fig=px.bar(x=dice, y=count)
fig.show()