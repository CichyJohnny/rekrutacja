import json


class Exporter:

    def __init__(self):
        self.data_file = 'taski.json'

    def save_tasks(self, tasks):



        with open(self.data_file, 'w') as file:
            updated_tasks = tasks


            json.dump(updated_tasks, file, indent=4)

        # TODO zapisz taski do pliku tutaj