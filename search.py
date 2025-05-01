from parallelHillClimber import PARALLEL_HILL_CLIMBER
import os

phc = PARALLEL_HILL_CLIMBER()
phc.Evolve()
phc.Save_Final_Fitness()
phc.Save_All()
#phc.Show_Best()