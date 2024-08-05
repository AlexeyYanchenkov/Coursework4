from abc import ABC, abstractmethod
import requests


class API(ABC):
    """Абстрактный класс для получения API с сайта"""

    @abstractmethod
    def get_vacancies(self, query):
        """Абстрактный метод для получения API с сайта и преобразования его в json-объекта"""
        pass


class HHAPI(API):
    """Класс для получения API с сайта по указанной вакансии """
    def __init__(self):
        self.__url = 'https://api.hh.ru/vacancies'
        self.__headers = {'User-Agent': 'HH-User-Agent'}
        self.__params = {'text': '', 'page': 0, 'per_page': 100}
        self.__vacancies = []

    def get_vacancies(self, keyword):
        """
        Метод отправки запроса и получения данных из API HeadHunter
                """
        self.__params['text'] = keyword
        while self.__params.get('page') != 2:
            response = requests.get(self.__url, headers=self.__headers, params=self.__params)
            vacancies = response.json()['items']
            self.__vacancies.extend(vacancies)
            self.__params['page'] += 1
        return self.__vacancies
