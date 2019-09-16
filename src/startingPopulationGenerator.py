import sys
import os.path
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

import src.configuration as conf
from src.Bee import Bee
import pickle

starting_population = [Bee(conf.NUM_OF_STUDENTS, conf.NAMES_OF_SUBJECTS) for _ in range(conf.NUM_OF_BEES)]
with open('startingPopulation.pickle', 'wb') as f:
    pickle.dump(starting_population, f)