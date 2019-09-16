

class Classwork:
    def __init__(self, classwork_name, random_day, random_hour, id, num_of_students=0):
        self._classwork_name = classwork_name
        self._day = random_day
        self._hour = random_hour
        self._id = id
        self._num_of_students = num_of_students

    @property
    def classwork_name(self):
        return self._classwork_name

    @property
    def day(self):
        return self._day

    @property
    def hour(self):
        return self._hour

    @property 
    def id(self):
        return self._id
    
    @property 
    def num_of_students(self):
        return self._num_of_students

    @hour.setter
    def hour(self, value):
        self._hour = value

    @num_of_students.setter
    def num_of_students(self, value):
        self._num_of_students = value