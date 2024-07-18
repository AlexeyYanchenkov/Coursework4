import os


from src.HHAPI import HHAPI
from src.utils import sort_vacancies, get_vacancies_by_salary_range, \
    get_top_vacancies
from src.vacancy import Vacancy

from config import ROOT_DIR

vacancies_file_path = os.path.join(ROOT_DIR, 'data', 'vacancies.json')


def main():
    search_query = input("Введите поисковый запрос: ").split()
    # Создание экземпляра класса для работы с API сайтов с вакансиями
    hh_api = HHAPI()
    # Получение вакансий с hh.ru в формате JSON
    hh_vacancies = hh_api.get_vacancies(search_query)
    vacancies_list = Vacancy.cast_to_object_list(hh_vacancies)
    top_n = int(input("Введите количество вакансий для вывода в топ N: "))
    min_sal = input('введите минимальную зарплату : ')
    max_sal = input('введите максимальную зарплату : ')
    try:
        get_by_sal_range = get_vacancies_by_salary_range(vacancies_list, int(min_sal), int(max_sal))
    except ValueError as e:
        print(f'возникла ошибка {e}')

    sorted_vacancies = sort_vacancies(get_by_sal_range)
    top_vacancies = get_top_vacancies(sorted_vacancies, top_n)
    for vacancy in top_vacancies:
        print(vacancy)


if __name__ == "__main__":
    main()
