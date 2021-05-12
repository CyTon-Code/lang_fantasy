class Variables:
    """
        класс-тип - переменные
    """

    variables = {}

    def __init__(self):
        """
            Вначале переменные обнуляються
        """

        self.variables.clear()

    def setter(self, key, value):
        """
            функция присвоения значения в переменную

            :param key: имя переменной
            :param value: значение, как правило это массив строк
            :return: None
        """

        self.variables[key] = value

    def delete(self, key):
        """
            функция удаления переменной

            :param key: имя переменной
            :return: None
        """

        if self.search(key):
            del self.variables[key]

    def getter(self, key):
        """
            функция копирования значения переменной

            :param key: имя переменной
            :return: значение
        """

        try:
            return self.variables[key]

        except KeyError:
            return None

    def search(self, key):
        """
            функция проверки на наличие переменной
            :param key:
            :return:
        """
        try:
            bool(self.variables[key])
            return True

        except KeyError:
            return False


def create_value():
    """
        функция отвечающая за образование массива строк

        ИМХО: принимать строку слов между которыми запятые и по ней
            образовывать массив
    """

    value = []
