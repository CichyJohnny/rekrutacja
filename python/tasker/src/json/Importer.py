import json, os, codecs


class Importer:

    def __init__(self):
        self.data_file = 'taski.json'
        self.taski = None

    def read_tasks(self):

        current_directory = os.getcwd()
        full_path = os.path.abspath(os.path.join(current_directory, self.data_file))

        try:

            with codecs.open(self.data_file, 'r', encoding='utf-8') as file:
                loaded_file = json.load(file)
                self.taski = loaded_file
                print(self.taski)

        except FileNotFoundError:

            print('File does not exist', full_path)


        # TODO odczytaj plik i zdekoduj treść tutaj

    def get_tasks(self):

        return self.taski

        # TODO zwróć zdekodowane taski tutaj