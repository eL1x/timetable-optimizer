import sys
import os.path
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

import src.configuration as conf
import pickle
from src.BeeAlgorithm import BeeAlgorithm


names = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
for num_of_students in [60, 80, 100]:
    for index in [5, 6, 7]:
        conf.NAMES_OF_SUBJECTS = names[:index]
        conf.NUM_OF_STUDENTS = num_of_students

        bee_algorithm = BeeAlgorithm(conf.NUM_OF_BEES, conf.NUM_OF_SITES, conf.NUM_OF_ELITE_SITES, conf.PATCH_SIZE,
                                     conf.NUM_OF_ELITE_BEES, conf.NUM_OF_OTHER_BEES, conf.MAX_GENS)


        bee_algorithm.search()
        with open('{}_{}'.format(num_of_students, index), 'wb') as f:
            pickle.dump(bee_algorithm, f, pickle.HIGHEST_PROTOCOL)



