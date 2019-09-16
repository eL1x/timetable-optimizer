import random
import src.configuration as conf


class Student:
    def __init__(self, id, first_name='Jan', last_name='Kowalski'):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.timetable = []
        self.fitness = 0

    def generate_random_timetable(self, subjects):
        for subject in subjects:
            while True:
                random_term = random.choice(subject.terms)
                if random_term.num_of_students < conf.MAX_NUM_OF_STUDENTS:
                    break
            
            self.timetable.append(random_term)
            random_term.num_of_students += 1

    def calculate_student_fitness(self):
        fitness = 0
        for day in conf.DAYS_SPACE:
            day_classwork = self.get_classwork_from_one_day(day)
            fitness += self.calculate_day_overlapping(day_classwork)

        not_free_days_penalty = self.penalty_for_not_free_days()
        self.fitness = fitness + not_free_days_penalty
        return fitness + not_free_days_penalty

    def calculate_not_free_days(self):
        not_free = set()
        for classwork in self.timetable:
            not_free.add(classwork.day)

        return len(not_free)

    def penalty_for_not_free_days(self):
        not_free_days = self.calculate_not_free_days()
        return max(not_free_days - conf.NOT_FREE_DAYS_ALLOWED, 0) * conf.PENALTY_FOR_NOT_FREE_DAYS

    def get_classwork_from_one_day(self, day):
        classwork_day = [classwork for classwork in self.timetable if classwork.day == day]
        return sorted(classwork_day, key=lambda x: x.hour)

    def calculate_day_overlapping(self, day_classwork):
        overlapped_in_minutes = []
        for index in range(len(day_classwork)):
            self.calculate_difference_for_one_classwork(day_classwork, overlapped_in_minutes, index)

        return sum(overlapped_in_minutes)

    def calculate_difference_for_one_classwork(self, day_classwork, overlapped_in_minutes, classwork_index):
        for index in range(classwork_index, len(day_classwork)):
            if index != classwork_index:
                slot_difference = abs(day_classwork[index].hour - day_classwork[classwork_index].hour)
                if slot_difference < conf.TIME_SLOTS:
                    overlapped_in_minutes.append((conf.SLOTS_DURING_ONE_CLASSWORK - slot_difference) *
                                                 conf.DIFFERENCE_BETWEEN_STARTING_CLASSES)
