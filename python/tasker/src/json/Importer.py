import json, os


class Importer:

    def __init__(self):
        self.data_file = 'taski.json'
        self.taski = None

    def read_tasks(self):

        current_directory = os.getcwd()
        full_path = os.path.abspath(os.path.join(current_directory, self.data_file))

        try:
            with open(self.data_file, 'r') as file:
                taski = json.load(file)
        except FileNotFoundError:
            print('File does not exist', full_path)
        self.taski = taski

        # TODO odczytaj plik i zdekoduj treść tutaj

    def get_tasks(self):

        print('mmmm', self.taski)

        return self.taski
        # TODO zwróć zdekodowane taski tutaj