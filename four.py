import random
import statistics
import plotly.figure_factory as px
count=[]
dice = []
for i in range(0,1000):
    dice1=random.randint(1,6)

    dice2=random.randint(1,6)
    count.append(i)

    dice.append(dice1+dice2)

mean = sum(dice)/len(dice)
standaredDeviation = statistics.stdev(dice)

print("mean is",mean)
print("standered deviation",standaredDeviation)

median = statistics.median(dice)
mode = statistics.mode(dice)

print("median is",median)
print("mode is",mode)

fig=px.create_distplot([dice], ["Result"],show_hist=False)
fig.show()

firstStandaredDeviationStart, firstStandaredDeviationEnd = mean-standaredDeviation, mean+standaredDeviation
secondStandaredDeviationStart, secondStandaredDeviationEnd = mean-(2*standaredDeviation), mean + (2*standaredDeviation)
thirdStandaredDeviationStart, thirdStandaredDeviationEnd = mean-(3*standaredDeviation), mean + (3*standaredDeviation)
listOfFirstStandaredDeviation = [result for result in dice if result>firstStandaredDeviationStart and result<firstStandaredDeviationEnd] 
listOfSecondStandaredDeviation = [result for result in dice if result>secondStandaredDeviationStart and result<secondStandaredDeviationEnd] 
listOfThirdStandaredDeviation = [result for result in dice if result>thirdStandaredDeviationStart and result<thirdStandaredDeviationEnd] 
print("{}% of data lies within one standered deviaion", format(len(listOfFirstStandaredDeviation)*100.0/len(dice)))
print("{}% of data lies within two standered deviaion", format(len(listOfSecondStandaredDeviation)*100.0/len(dice)))
print("{}% of data lies within three standered deviaion", format(len(listOfThirdStandaredDeviation)*100.0/len(dice)))