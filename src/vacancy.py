class Vacancy:
    """Класс для работы с вакансиями"""
    def __init__(self, name, link, salary, responsibility, requirement, vacancy_id):
        self.name = name
        self.link = link
        self.salary = salary
        self.responsibility = responsibility
        self.requirement = requirement
        self.vacancy_id = vacancy_id

    @classmethod
    def cast_to_object_list(cls, json_vacancies):
        """Метод добавления вакансий в список"""
        object_list = []
        for vacancy in json_vacancies:
            name = vacancy.get("name")
            link = vacancy.get("alternate_url")
            salary = vacancy.get("salary", 'Не указано')
            vacancy_id = vacancy.get("id")
            if salary is None:
                salary = 0
            else:
                salary = cls.validate__int(vacancy.get("salary").get("from"))
            responsibility = cls.validate__str(vacancy.get("snippet").get("responsibility"))
            requirement = cls.validate__str(vacancy.get("snippet").get("requirement"))
            vacancy_obj = cls(name, link, salary, responsibility, requirement, vacancy_id)
            object_list.append(vacancy_obj)
        return object_list

    def __str__(self):
        """Метод вывода информации по вакансиям"""

        return (f"Название вакансии: {self.name} \n"
                f"Заработная плата: {self.salary} \n"
                f"Описание: {self.responsibility} \n"
                f"Ссылка: {self.link} \n"
                f"ID: {self.vacancy_id} \n")

    @staticmethod
    def validate__str(value):
        """Метод вывода информации при нулевой строке"""
        if value:
            return value
        return "Информация не была найдена"

    @staticmethod
    def validate__int(value):
        """Метод вывода информации при вводе 0"""
        if value:
            return value
        return 0

    def __lt__(self, other):
        """Метод сравнения зарплат "меньше чем" """
        if self.salary is not None and other.salary is not None:
            return self.salary < other.salary

    def __gt__(self, other):
        """Метод сравнения зарплат "больше чем" """
        return self.salary > other.salary
