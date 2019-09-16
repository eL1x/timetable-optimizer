import sys
import os.path
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

import random
from copy import deepcopy
import src.configuration as conf
from src.Bee import Bee
from src.Classwork import Classwork


class BeeAlgorithm:
    def __init__(self, num_of_bees, num_of_sites, num_of_elite_sites, patch_size, num_of_elite_bees, num_of_other_bees, max_gens):
        self.num_of_bees = num_of_bees
        self.num_of_sites = num_of_sites
        self.num_of_elite_sites = num_of_elite_sites
        self.patch_size = patch_size
        self.num_of_elite_bees = num_of_elite_bees
        self.num_of_other_bees = num_of_other_bees
        self.max_gens = max_gens
        self.population = []
        self.fitness = []
        self.training = []
        self.returned_best = None
        print('num of students')
        print(conf.NUM_OF_STUDENTS)


    def search(self):
        best = None
        self.population = self.generate_population()
        for gen in range(self.max_gens):
            if best and best.fitness == 0:
                break
            print('Gen : ' + str(gen))
            best = self.choose_best_solution(best)
            self.update_population()
            
            self.fitness.append(best.fitness)
        
        print("Num of students: ")
        for index, subject in enumerate(best.subjects):
            print("Zajęcia #", index)
            for term in subject.terms:
                print(term.num_of_students)
        self.returned_best = best
        return best

    def generate_population(self):
        return [Bee(conf.NUM_OF_STUDENTS, conf.NAMES_OF_SUBJECTS) for _ in range(self.num_of_bees)]

    def choose_best_solution(self, best):
        for bee in self.population:
            bee.calculate_bee_fitness()
        self.population = sorted(self.population, key=lambda x: x.fitness)
        self.training.append(self.population[0].fitness)
        if not best or self.population[0].fitness < best.fitness:
            best = deepcopy(self.population[0])
            print(best.fitness)

        return best

    def generate_next_gen(self):
        next_gen = []
        for index, bee in enumerate(self.population[:self.num_of_sites]):
                neigh_size = self.num_of_elite_bees if index < self.num_of_elite_sites else self.num_of_other_bees
                next_gen.append(self.search_neigh(bee, neigh_size, self.patch_size))
        
        return next_gen
    
    def update_population(self):
        next_gen = self.generate_next_gen()
        scouts = self.create_scout_bees(self.num_of_bees - self.num_of_sites)
        self.population = next_gen + scouts
        self.patch_size = self.patch_size * conf.PATCH_SIZE_DECREASE_FACTOR

    def search_neigh(self, parent, neigh_size, patch_size):
        neigh = []
        for _ in range(neigh_size):
            neigh.append(self.create_neigh_bee(parent, patch_size))
        
        for bee in neigh:
            bee.calculate_bee_fitness()

        return sorted(neigh, key=lambda x: x.fitness)[0]
        
    def create_neigh_bee(self, parent, patch_size):
        new_bee = deepcopy(parent)
        for subject_index, subject in enumerate(parent.subjects):
            new_bee = self.change_term_hour(new_bee, subject, patch_size, subject_index)

        return new_bee
    
    def create_scout_bees(self, num_of_scouts):
        scouts_population = []
        for _ in range(num_of_scouts):
            scouts_population.append(Bee(conf.NUM_OF_STUDENTS, conf.NAMES_OF_SUBJECTS))

        return scouts_population
    
    def change_term_hour(self, bee, subject, patch_size, subject_index):
        for term_index, term in enumerate(subject.terms):
            new_hour = self.choose_new_hour(term, patch_size)
            bee.subjects[subject_index].terms[term_index] = Classwork(term.classwork_name, term.day, new_hour, term.id, term.num_of_students)
            bee = self.update_students(bee, term, new_hour)
            
        return bee
    
    def choose_new_hour(self, term, patch_size):
        random_number = random.random()
        new_hour = round(term.hour + random_number * patch_size if random_number < 0.5 else term.hour - random_number * patch_size)
        new_hour = min(new_hour, conf.HOURS_SPACE[-1])
        new_hour = max(new_hour, conf.HOURS_SPACE[0])

        return new_hour
    
    def update_students(self, bee, term, new_hour):
        for student in bee.students:
            self.update_student_classwork(student, term, new_hour)
        return bee
    
    def update_student_classwork(self, student, term, new_hour):
        for classwork in student.timetable:
            if classwork.classwork_name == term.classwork_name and classwork.id == term.id:
                classwork.hour = new_hour

    def get_fitness(self):
        return self.fitness

    def get_training_process(self):
        return self.training