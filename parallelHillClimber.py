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
        os.system("del del brain*.nndf")
        os.system("del fitness*.txt")

    
    def Evolve(self):
        #self.parent.Start_Simulation("GUI")
        #for currentGeneration in range(0, c.NUMBER_OF_GENERATIONS):
        #    
        self.Evaluate(self.parents)
        self.Evolve_For_One_Generation()

    
    def Evolve_For_One_Generation(self):
        self.Spawn()
        self.Mutate()
        self.Evaluate(self.children)
        #print("\nParent fitness: " + str(self.parent.fitness) + " Child fitness: " + str(self.child.fitness) + "\n")
        #self.Select()
    

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
        if self.parent.fitness > self.child.fitness:
            self.parent = self.child

    
    def Show_Best(self):
        #self.child.Evaluate("GUI")
        pass


    def Evaluate(self, solutions):
        for parent in solutions:
            self.parents[parent].Start_Simulation("DIRECT")
        for parent in solutions:
            self.parents[parent].Wait_For_Simulation_To_End()