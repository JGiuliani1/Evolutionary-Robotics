import matplotlib.pyplot as plt

# store data
file1 = open("quadData1/averageFitness.txt", 'r')
list1 = []
file2 = open("quadData2/averageFitness.txt", 'r')
list2 = []
file3 = open("quadData3/averageFitness.txt", 'r')
list3 = []
file4 = open("quadData4/averageFitness.txt", 'r')
list4 = []
file5 = open("quadData5/averageFitness.txt", 'r')
list5 = []

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

file1.close()
file2.close()
file3.close()
file4.close()
file5.close()

finalAverageFitness = []
initialAverageFitness = []

finalAverageFitness.append(list1[499])
finalAverageFitness.append(list2[499])
finalAverageFitness.append(list3[499])
finalAverageFitness.append(list4[499])
finalAverageFitness.append(list5[499])

initialAverageFitness.append(list1[0])
initialAverageFitness.append(list2[0])
initialAverageFitness.append(list3[0])
initialAverageFitness.append(list4[0])
initialAverageFitness.append(list5[0])


# plot data
plt.plot(initialAverageFitness, label="Initial Average Fitness")
plt.plot(finalAverageFitness, label="Final Average Fitness")
plt.legend()
plt.xlabel("Trial #")
plt.ylabel("Fitness")
plt.show()