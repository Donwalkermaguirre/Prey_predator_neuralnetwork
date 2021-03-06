from pyevolve import G1DList
from pyevolve import GSimpleGA
from pyevolve import Selectors
from pyevolve import Statistics
from funcionevaluacion import evalfun
from pyevolve import DBAdapters
import pyevolve
from funcionevaluacionrepetida import evalfunrep
from funcionevaluacionv1v2 import evalfun2
# This function is the evaluation function, we want
# to give high score to more zero'ed chromosomes
"""def eval_func(chromosome):
   score = 0.0

   # iterate over the chromosome
   # score = len(filter(lambda x: x==0, chromosome.genomeList))
   for value in chromosome:
      if value==0:
         score += 1

   return score"""

# Enable the pyevolve logging system
pyevolve.logEnable()

# Genome instance, 1D List of 50 elements
genome = G1DList.G1DList(32)

# Sets the range max and min of the 1D List
genome.setParams(rangemin=-10, rangemax=10)

# The evaluator function (evaluation function)
genome.evaluator.set(evalfun)

# Genetic Algorithm Instance
ga = GSimpleGA.GSimpleGA(genome)

# Set the Roulette Wheel selector method, the number of generations and
# the termination criteria
ga.selector.set(Selectors.GRouletteWheel)
ga.setGenerations(500)
ga.terminationCriteria.set(GSimpleGA.ConvergenceCriteria)
"ga.terminationCriteria.set(GSimpleGA.FitnessStatsCriteria)"
ga.setMutationRate(0.001)
ga.setCrossoverRate(0.15)
ga.setPopulationSize(500)
# Sets the DB Adapter, the resetDB flag will make the Adapter recreate
# the database and erase all data every run, you should use this flag
# just in the first time, after the pyevolve.db was created, you can
# omit it.
sqlite_adapter = DBAdapters.DBSQLite(identify="ex1", resetDB=True)
ga.setDBAdapter(sqlite_adapter)

def step_callback(gp_engine):
    a=ga.bestIndividual()
    b=a.genomeList
    print(b)


ga.stepCallback.set(step_callback)
# Do the evolution, with stats dump
# frequency of 20 generations
ga.evolve(freq_stats=1)

# Best individual

"""print ga.bestIndividual() """
