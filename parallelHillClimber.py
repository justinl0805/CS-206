from solution import *
import constants as c
import copy

class PARALLEL_HILL_CLIMBER:
    def __init__(self):
        os.system("del brain*.nndf")
        os.system("del fitness*.txt")

        self.parents = {}
        self.nextAvailableID = 0
        for i in range(c.populationSize):
            self.parents[i] = SOLUTION(self.nextAvailableID)
            self.nextAvailableID += 1


    def Evolve(self):
        self.Evaluate(self.parents)
        for currentGeneration in range(c.numberOfGenerations):
            self.Evolve_For_One_Generation()

    def Evolve_For_One_Generation(self):
        self.Spawn()
        self.Mutate()
        self.Evaluate(self.children)
        self.Print()
        self.Select()

    def Spawn(self):
        self.children = {}
        for id, robot in self.parents.items():
            self.children[id] = copy.deepcopy(robot)
            self.children[id].Set_ID(self.nextAvailableID)
            self.nextAvailableID += 1

        #self.child = copy.deepcopy(self.parent)
        #self.child.Set_ID(self.nextAvailableID)
        #self.nextAvailableID += 1

    def Mutate(self):
        for key, value in self.children.items():
            value.Mutate()

    def Select(self):
        for keys, values in self.parents.items():
            if self.children[keys].fitness < values.fitness:
                self.parents[keys] = self.children[keys]

    def Print(self):
        print('\n')
        for key in range(len(self.parents)):
            print('Parent:', self.parents[key].fitness, 'Child:', self.children[key].fitness)
        print('\n')

    def Show_Best(self):
        bestKey = 0
        bestFit = self.parents[0].fitness

        for key in range(len(self.parents)):
            if self.parents[key].fitness < bestFit:
                bestFit = self.parents[key].fitness
                bestKey = key

        self.parents[bestKey].Start_Simulation("GUI")

    def Evaluate(self, solutions):
        for i in solutions.keys():
            self.parents[i].Start_Simulation("DIRECT")

        for i in solutions.keys():
            self.parents[i].Wait_For_Simulation_To_End()
