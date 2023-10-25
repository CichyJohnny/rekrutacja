import json, codecs


class Exporter:

    def __init__(self):
        self.data_file = 'taski.json'

    def save_tasks(self, tasks):
        # This function is called to apply changes to 'taski.json'

        updated_tasks = tasks

        with codecs.open(self.data_file, 'w', encoding='utf-8') as file:

            json.dump(updated_tasks, file, indent=4)

        # Function overwrite json file with new data
        # New data is simply dumped to the file with indent = 4 for readability
        # encoding utf-8 is used to handle non-ASCII characters

        # TODO, completed
        # Zapisz taski do pliku tutaj