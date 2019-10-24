class WebBehaviorStud:
    def __init__(self):
        pass

    @staticmethod
    def stand_do_input(student_, data):
        student_.first_name = data['firstname']
        student_.second_name = data['lastname']
        student_.gender = data['gender']
        student_.age = int(data['age'])

    @staticmethod
    def stand_do_edit(student_, data):
        student_.first_name = data['firstname'] if data['firstname'] else student_.first_name
        student_.second_name = data['lastname'] if data['lastname'] else student_.second_name
        student_.gender = data['gender'] if data['gender'] else student_.gender
        student_.age = int(data['age']) if data['age'] else student_.age
