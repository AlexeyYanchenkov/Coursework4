from abc import ABC, abstractmethod
import os
from src.utils import save_to_json, read_json
from config import ROOT_DIR
import json
vacancies_file_path = os.path.join(ROOT_DIR, 'data', 'vacancies.json')


class AbstractVacancySaver(ABC):
    """Абстрактный класс для добавления вакансий в JSON файл"""

    @abstractmethod
    def add_vacancy(self, vacancy):
        pass

    @abstractmethod
    def delete_vacancy(self, vacancy, id_del: [int]):
        pass


class JSONSaver(AbstractVacancySaver):
    """Класс для добавления вакансий в JSON файл"""

    def __init__(self, file_path=vacancies_file_path):
        self.__file_path = file_path

    def add_vacancy(self, vacancy, file_path=vacancies_file_path):
        """Метод для добавления вакансий """
        id_list = []
        data = read_json(file_path)
        vac_dict = vacancy.__dict__
        vacancy_id = vac_dict.get('vacancy_id')
        for vacancy_item in data:
            vac_id = vacancy_item.get('vacancy_id')
            id_list.append(vac_id)
        if vacancy_id not in id_list:
            print(f'добавлена вакансия \n{vacancy}')
            data.append(vac_dict)
        else:
            print(f'вакансия существует \n{vacancy}')
        save_to_json(data)

    def delete_vacancy(self, id_del, file_path=vacancies_file_path):
        """Метод удаления вакансии"""
        new_list = []
        data = read_json(file_path)
        for vacancy_item in data:
            item_id = vacancy_item.get('vacancy_id')
            if item_id == id_del:
                continue
            new_list.append(vacancy_item)
        save_to_json(new_list)

    def save_filtred_vacancices(self, vacancies_list):
        """Метод для фильтрации и сохранении вакансий"""
        filtred_vacancies = []
        for vacancy in vacancies_list:
            vac_dict = vacancy.__dict__
            filtred_vacancies.append(vac_dict)
            save_to_json(filtred_vacancies, self.__file_path)

    def load_vacancies(self):
        """Метод получения данных из файла"""
        with open(self.__file_path, 'r', encoding='utf-8')as file:
            new_list = json.load(file)
        return new_list
