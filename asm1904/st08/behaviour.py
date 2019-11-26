class Behaviour:

    def action(self):
        raise NotImplementedError()


class Chinese_Tea_Behaviour(Behaviour):

    def action(self):
        return "Китайский чай."


class Indian_Tea_Behaviour(Behaviour):

    def action(self):
        return "Индийский чай."
