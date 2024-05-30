class Worker:
    def __init__(self, name_pm: str, age_pm: int):
        self.__name = name_pm
        self.__age = age_pm

    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age

    def introduce(self):
        """Это метод для представления работника"""
        print(f"Меня зовут {self.__name}, мне {self.__age} лет")

class Company:
    def __init__(self):
        self.__workers = []

    def add_worker(self, worker: Worker):
        """Это метод для добавления рабочего"""
        self.__workers.append(worker)

    def find_worker(self, worker_name: str):
        for item in self.__workers:
            if item.get_name() == worker_name:
                return item

    def fire_worker(self, worker_name: str):
        worker = self.find_worker(worker_name)
        print(f"Работник {worker.get_name()} уволен")
        self.__workers.remove(worker)
