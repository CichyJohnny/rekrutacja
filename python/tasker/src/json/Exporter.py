import json, codecs


class Exporter:

    def __init__(self):
        self.data_file = 'taski.json'

    def save_tasks(self, tasks):
        updated_tasks = tasks

        with codecs.open(self.data_file, 'w', encoding='utf-8') as file:

            json.dump(updated_tasks, file, indent=4)

        # TODO zapisz taski do pliku tutaj