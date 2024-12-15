class Tree:
    """
    Класс для описания дерева.
    """

    def __init__(self, height: float, age: int, species: str):
        """
        :param height: Высота дерева в метрах. Должна быть положительной.
        :param age: Возраст дерева в годах. Должен быть неотрицательным.
        :param species: Вид дерева.
        """
        if height <= 0:
            raise ValueError("Высота должна быть положительной.")
        if age < 0:
            raise ValueError("Возраст не может быть отрицательным.")

        self.height = height
        self.age = age
        self.species = species

    def grow(self, years: int) -> None:
        """
        Увеличивает возраст дерева на указанное количество лет и высоту на 10 см за год.

        :param years: Количество лет, на которое дерево должно вырасти. Должно быть положительным.
        :raises ValueError: Если переданное значение отрицательное.

        >>> tree = Tree(3.0, 5, "Oak")
        >>> tree.grow(2)
        >>> tree.age
        7
        >>> tree.height
        3.2
        """
        if years <= 0:
            raise ValueError("Количество лет должно быть положительным.")

        self.age += years
        self.height += years * 0.1

    def describe(self) -> str:
        """
        Возвращает строку с описанием дерева.

        :return: Описание дерева в формате "Вид: species, Возраст: age лет, Высота: height м".

        >>> tree = Tree(5.0, 10, "Pine")
        >>> tree.describe()
        'Вид: Pine, Возраст: 10 лет, Высота: 5.0 м'
        """
        return f"Вид: {self.species}, Возраст: {self.age} лет, Высота: {self.height:.1f} м"


class Chair:
    """
    Класс для описания стула.
    """

    def __init__(self, material: str, color: str, max_weight: int):
        """
        :param material: Материал стула (например, дерево, пластик).
        :param color: Цвет стула.
        :param max_weight: Максимальный вес, который выдерживает стул. Должен быть положительным.
        """
        if max_weight <= 0:
            raise ValueError("Максимальный вес должен быть положительным.")

        self.material = material
        self.color = color
        self.max_weight = max_weight

    def repaint(self, new_color: str) -> None:
        """
        Изменяет цвет стула.

        :param new_color: Новый цвет для стула.

        >>> chair = Chair("wood", "brown", 120)
        >>> chair.repaint("black")
        >>> chair.color
        'black'
        """
        self.color = new_color

    def is_suitable_for_weight(self, weight: int) -> bool:
        """
        Проверяет, выдержит ли стул указанный вес.

        :param weight: Вес для проверки. Должен быть положительным.
        :return: True, если стул выдержит, иначе False.

        >>> chair = Chair("plastic", "white", 100)
        >>> chair.is_suitable_for_weight(90)
        True
        >>> chair.is_suitable_for_weight(110)
        False
        """
        if weight <= 0:
            raise ValueError("Вес должен быть положительным.")
        return weight <= self.max_weight


class FacebookAccount:
    """
    Класс для описания аккаунта в Facebook.
    """

    def __init__(self, username: str, age: int, friends_count: int):
        """
        :param username: Имя пользователя.
        :param age: Возраст пользователя. Должен быть не меньше 13.
        :param friends_count: Количество друзей. Не может быть отрицательным.
        """
        if age < 13:
            raise ValueError("Возраст должен быть не меньше 13 лет.")
        if friends_count < 0:
            raise ValueError("Количество друзей не может быть отрицательным.")

        self.username = username
        self.age = age
        self.friends_count = friends_count

    def add_friend(self) -> None:
        """
        Увеличивает количество друзей на 1.

        >>> account = FacebookAccount("john_doe", 20, 5)
        >>> account.add_friend()
        >>> account.friends_count
        6
        """
        self.friends_count += 1

    def post_status(self, status: str) -> str:
        """
        Публикует статус от имени пользователя.

        :param status: Текст статуса.
        :return: Строка с текстом "Username: status".

        >>> account = FacebookAccount("jane_doe", 25, 50)
        >>> account.post_status("Hello, world!")
        'jane_doe: Hello, world!'
        """
        return f"{self.username}: {status}"
