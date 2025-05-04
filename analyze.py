import matplotlib.pyplot as plt

# store data
file1 = open("hexData1/averageFitness.txt", 'r')
list1 = []
file2 = open("hexData2/averageFitness.txt", 'r')
list2 = []
file3 = open("hexData3/averageFitness.txt", 'r')
list3 = []
file4 = open("hexData4/averageFitness.txt", 'r')
list4 = []
file5 = open("hexData5/averageFitness.txt", 'r')
list5 = []

file6 = open("quadData1/finalFitness.txt", 'r')
list6 = []
file7 = open("quadData2/finalFitness.txt", 'r')
list7 = []
file8 = open("quadData3/finalFitness.txt", 'r')
list8 = []
file9 = open("quadData4/finalFitness.txt", 'r')
list9 = []
file10 = open("quadData5/finalFitness.txt", 'r')
list10 = []

for line in file1:
    list1.append(float(line))
for line in file2:
    list2.append(float(line))
for line in file3:
    list3.append(float(line))
for line in file4:
    list4.append(float(line))
for line in file5:
    list5.append(float(line))

for line in file6:
    list6.append(float(line.split()[1]))
for line in file7:
    list7.append(float(line.split()[1]))
for line in file8:
    list8.append(float(line.split()[1]))
for line in file9:
    list9.append(float(line.split()[1]))
for line in file10:
    list10.append(float(line.split()[1]))

file1.close()
file2.close()
file3.close()
file4.close()
file5.close()

file6.close()
file7.close()
file8.close()
file9.close()
file10.close()

hexAverage = []
hexMax = []

hexAverage.append(list1[499])
hexAverage.append(list2[499])
hexAverage.append(list3[499])
hexAverage.append(list4[499])
hexAverage.append(list5[499])

hexMax.append(max(list6))
hexMax.append(max(list7))
hexMax.append(max(list8))
hexMax.append(max(list9))
hexMax.append(max(list10))


# plot data
#plt.plot(hexAverage, label="Average Hexapod Fitness")
plt.plot(hexMax, label="Max Quadruped Fitness")
plt.legend()
plt.xlabel("Trial #")
plt.ylabel("Fitness")
plt.show()