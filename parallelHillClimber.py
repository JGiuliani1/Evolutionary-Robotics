import constants as c
import copy
import os
from solution import SOLUTION
from solutionHex import SOLUTION_HEX


class PARALLEL_HILL_CLIMBER:
    def __init__(self):
        self.parents = {}
        self.nextAvailableID = 0
        for i in range(0, c.POPULATION_SIZE):
            self.parents[i] = SOLUTION(self.nextAvailableID) # quadruped
            #self.parents[i] = SOLUTION_HEX(self.nextAvailableID) # hexapod
            self.nextAvailableID += 1
        os.system("del brain*.nndf")
        os.system("del fitness*.txt")
        os.system("del world*.sdf")
        os.system("del body*.urdf")

    
    def Evolve(self):
        for currentGeneration in range(0, c.NUMBER_OF_GENERATIONS):
            self.Evaluate(self.parents)
            self.Evolve_For_One_Generation() 

    
    def Evolve_For_One_Generation(self):
        self.Spawn()
        self.Mutate()
        self.Evaluate(self.children)
        self.Calculate_Average_Fitness()
        self.Show_Generation()
        self.Print()
        self.Select()
    

    def Spawn(self):
        self.children = {}
        for i in self.parents:
            self.children[i] = copy.deepcopy(self.parents[i])
            self.children[i].Set_ID(self.nextAvailableID)
            self.nextAvailableID += 1
    

    def Mutate(self):
        for child in self.children:
            self.children[child].Mutate()
    

    def Select(self):
       for i in self.children:
           if self.children[i].fitness > self.parents[i].fitness:
               self.parents[i] = self.children[i]

    
    def Show_Best(self):
        best = self.parents[0].fitness
        bestID = self.parents[0].myID
        for parent in self.parents:
            if self.parents[parent].fitness > best:
                best = self.parents[parent].fitness
                bestID = self.parents[parent].myID
        for parent in self.parents:
            if self.parents[parent].myID == bestID:
                self.parents[parent].Start_Simulation("GUI", False)

    
    def Save_Final_Fitness(self):
        file = open("finalFitness.txt", 'a')
        for parent in self.parents:
            file.write(str(self.parents[parent].myID) + ": " + str(self.parents[parent].fitness) + "\n")
        file.close()    
        

    def Save_All(self):
        for parent in self.parents:
            self.parents[parent].Start_Simulation("DIRECT", True)


    def Evaluate(self, solutions):
        for i in solutions:
            solutions[i].Start_Simulation("DIRECT", False)
        for j in solutions:
            solutions[j].Wait_For_Simulation_To_End()


    def Calculate_Average_Fitness(self):
        # calculate average fitness of parent population
        total_parent_fitness = 0
        for parent in self.parents:
            total_parent_fitness += self.parents[parent].fitness
        self.average_parent_fitness = total_parent_fitness / len(self.parents)

        # save value to file
        file = open("averageFitness.txt", "a")
        file.write(str(self.average_parent_fitness) + "\n")
        file.close()


    def Show_Generation(self):
        with open('averageFitness.txt', 'r') as file:
            self.line_count = sum(1 for _ in file)
        file.close()


    def Print(self):
        print("\n")
        print("Generation:", self.line_count)
        for i in range(0, len(self.parents)):
            print("Parent fitness: " + str(self.parents[i].fitness) + " Child fitness: " + str(self.children[i].fitness))
        print("Average parent fitness: ", str(self.average_parent_fitness))
        print("\n")