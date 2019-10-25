import pickle
import os

from .simple_student import SimpleStudent
from .starosta import Starosta
from .proforg import Proforg
from .student import Student
from .behav_starosta import BStarosta
from .behav_proforg import BProforg
from .behav_simp_student import BSimpStudent
from .behav_web_sim_stud import BWebSimpStudent
from .behav_web_starosta import BWebStarosta
from .behav_web_proforg import BWebProforg


class Group:
    __slots__ = ('group_menu', '_students')

    def __init__(self):
        self.group_menu = [
            ['Добавить студента', SimpleStudent, {'console': BSimpStudent, 'web': BWebSimpStudent}],
            ['Добавить старосту', Starosta, {'console': BStarosta, 'web': BWebStarosta}],
            ['Добавить профорга', Proforg, {'console': BProforg, 'web': BWebProforg}]
        ]
        self._students = []

    def add_student(self, type_student, *, data=None, type_context='console'):
        if data is None:
            self._students.append(Student(self.group_menu[type_student][1](),
                                          self.group_menu[type_student][2][type_context]))
        else:
            self._students.append(Student(self.group_menu[type_student][1](),
                                          self.group_menu[type_student][2][type_context], data))

    def change_student(self, number_stud, *, data=None):
        if data is None:
            self._students[number_stud].edit_student()
        else:
            return self._students[number_stud].edit_student(data)

    def remove_student(self, number_stud):
        del self._students[number_stud]

    def print_group(self):
        res = None
        for i, student in enumerate(self._students):
            data = student.print_info(i)
            if data is not None:
                if i == 0:
                    res = data
                else:
                    res += data
        return res

    def do_magic(self, number_stud):
        return self._students[number_stud].magic()

    def save_to_file(self):
        pickle.dump(self._students, 
                    open(os.path.join(os.path.abspath(os.path.dirname(os.path.dirname(__file__))), 
                                      'group.p'), 'wb'))

    def load_from_file(self):
        self._students = pickle.load(open(os.path.join(os.path.abspath(os.path.dirname(os.path.dirname(__file__))), 
                                                       'group.p'), 'rb'))

    @property
    def amount_students(self):
        return len(self._students)
