import os
from parallelHillClimber import  *

phc = PARALLEL_HILL_CLIMBER()
phc.Evolve()
phc.Show_Best()
phc.Results()

# for _ in range(5):
#    os.system("python generate.py")
#   os.system("python simulate.py")
