import json, os, codecs


class Importer:

    def __init__(self):
        self.data_file = 'taski.json'
        self.taski = None

    def read_tasks(self):

        # This function is called to load 'taski.json' file

        current_directory = os.getcwd()
        full_path = os.path.abspath(os.path.join(current_directory, self.data_file))

        try:

            with codecs.open(self.data_file, 'r', encoding='utf-8') as file:
                loaded_file = json.load(file)
                self.taski = loaded_file
                print(self.taski)

        except FileNotFoundError:

            print('File does not exist', full_path)

        # This function load file using utf-8 encoding to handle non-ASCII characters
        # File is loaded into self.taski and then passed to get_tasks inside App.py
        # Except FileNotFoundError handles error if 'taski.json' not found

        # TODO, completed
        # odczytaj plik i zdekoduj treść tutaj


    def get_tasks(self):
        # This function called simply returns self.taski assigned earlier by read_tasks

        return self.taski

        # TODO, completed
        # Zwróć zdekodowane taski tutaj