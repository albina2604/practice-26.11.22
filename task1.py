class Soda:
    """Определение типа газированной воды"""

    def __init__(self, ingridient):
        if isinstance(ingridient, str):
            self.ingridient = ingridient
        else:
            self.ingridient = None

    def show_my_drink(self):
        if self.ingridient:
            print(f'Газировка и {self.ingridient}')
        else:
            print("Обычная газировка")
