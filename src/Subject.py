import random
from src.Classwork import Classwork
import src.configuration as conf


class Subject:
    def __init__(self, name, id, num_of_terms):
        self.id = id
        self.name = name
        self.num_of_terms = num_of_terms
        self.terms = []

    def generate_random_terms(self):
        for index in range(self.num_of_terms):
            random_day = random.randrange(max(conf.DAYS_SPACE))
            random_hour = random.randrange(max(conf.HOURS_SPACE))

            self.terms.append(Classwork(self.name, random_day, random_hour, index))
