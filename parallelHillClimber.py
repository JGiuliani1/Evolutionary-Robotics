import constants as c
import copy
import os
from solution import SOLUTION


class PARALLEL_HILL_CLIMBER:
    def __init__(self):
        self.parents = {}
        self.nextAvailableID = 0
        for i in range(0, c.POPULATION_SIZE):
            self.parents[i] = SOLUTION(self.nextAvailableID)
            self.nextAvailableID += 1
        os.system("del brain*.nndf")
        os.system("del fitness*.txt")
        os.system("del world*.sdf")
        os.system("del body*.urdf")

    
    def Evolve(self):
        #self.parent.Start_Simulation("GUI")
        for currentGeneration in range(0, c.NUMBER_OF_GENERATIONS):
            self.Evaluate(self.parents)
            self.Evolve_For_One_Generation() 

    
    def Evolve_For_One_Generation(self):
        self.Spawn()
        self.Mutate()
        self.Evaluate(self.children)
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
       # normal fitness
       """for i in self.children:
           if self.children[i].fitness > self.parents[i].fitness:
               self.parents[i] = self.children[i]"""
       
       # MOO
       for i in self.children:
           child_fitness = self.children[i].fitness.split()
           parent_fitness = self.parents[i].fitness.split()
           if child_fitness[0] > parent_fitness[0] and child_fitness[1] > parent_fitness[1]:
               self.parents[i] = self.children[i]

    
    def Show_Best(self):
        # normal fitness
        """best = self.parents[0].fitness
        bestID = self.parents[0].myID
        for parent in self.parents:
            if self.parents[parent].fitness > best:
                best = self.parents[parent].fitness
                bestID = self.parents[parent].myID
        for parent in self.parents:
            if self.parents[parent].myID == bestID:
                self.parents[parent].Start_Simulation("GUI")"""
        
        # MOO
        best_fitness = self.parents[0].fitness.split()
        bestID = self.parents[0].myID
        for parent in self.parents:
            current_fitness = self.parents[parent].fitness.split()
            if current_fitness[0] > best_fitness[0] and current_fitness[1] > best_fitness[1]:
                best_fitness = self.parents[parent].fitness.split()
                bestID = self.parents[parent].myID
        for parent in self.parents:
            if self.parents[parent].myID == bestID:
                self.parents[parent].Start_Simulation("GUI")


    def Evaluate(self, solutions):
        for i in solutions:
            solutions[i].Start_Simulation("DIRECT")
        for j in solutions:
            solutions[j].Wait_For_Simulation_To_End()


    def Print(self):
        print("\n")
        for i in range(0, len(self.parents)):
            print("Parent fitness: " + str(self.parents[i].fitness) + " Child fitness: " + str(self.children[i].fitness))
        print("\n")