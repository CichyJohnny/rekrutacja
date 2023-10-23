import json, datetime, urllib.request, os.path, requests


class RatioObtainer:
    base = None
    target = None


    def __init__(self, base, target):
        self.base = base
        self.target = target
        self.data_file = '../ratios.json'
        self.ratio_data = self.load_ratio_data()


    def load_ratio_data(self):

        # This function is called to load and store as a variable content of 'ratios.json' file for future use

        if os.path.exists(self.data_file):
            with open(self.data_file, 'r') as file:
                data = json.load(file)

            return data

        return {}

        # Function checks if ratios.json exists
        # Then returns json file's content


    def was_ratio_saved_today(self):

        #This function is called to return True if needed ratio was saved today, False if not

        today = datetime.date.today().isoformat()

        return today in self.ratio_data and f"{self.base}{self.target}" in self.ratio_data[today]


        # Function checks if the desired ratio was already saved today
        # It looks for objects with current date and from-to currency in it
        # E.g. { '2023-10-2' : { "USDEUR", .... }, ... }

        # TODO, completed
        # This function checks if given ratio was saved today and if the file with ratios is created at all
        # should return false when file doesn't exist or if there's no today's exchange rate for given values at all
        # should return true otherwise


    def fetch_ratio(self):

        # This Function is called if needed ratio was not saved today

        base = str(self.base)
        target = str(self.target)
        url_path = f'http://api.exchangerate.host/live?access_key=cd007cacde18395212e8ab232cb5f260&source={base}&format=1'
        response = requests.get(url_path)
        ratio_data = response.json()
        self.save_ratio(ratio_data)

        quotes = response.json().get('quotes')
        ratio_value = quotes.get(base + target)

        return float(ratio_value)


        # Function create an url path to connect with the api for specific currency ratios
        # Then get answer from the api and saves it
        # Finally returns the value of the specific from-to currency ratio

        # TODO, completed
        # This function calls API for today's exchange ratio
        # Should ask API for today's exchange ratio with given base and target currency
        # and call save_ratio method to save it


    def save_ratio(self, ratio_data):

        # This Function is called to save or update current from-to currency ratio in 'ratios.json' file

        today = datetime.date.today().isoformat()

        if today not in self.ratio_data:
            self.ratio_data[today] = {}
        self.ratio_data[today][f"{self.base}{self.target}"] = ratio_data['quotes'][f"{self.base}{self.target}"]

        with open(self.data_file, 'w') as file:
            json.dump(self.ratio_data, file, indent=4)

        # Function checks if there is already block with today's date, if not creates one
        # Then it appends new from-to currency ratio to self.ratio_data[today's date]
        # Finally it dumps self.ratio_data into 'ratios.json' file, with indent=4 for readability

        # TODO, completed
        # Should save or update exchange rate for given pair in json file
        # takes ratio as argument
        # example file structure is shipped in project's directory, yours can differ (as long as it works)


    def get_matched_ratio_value(self):

        # This function is called if from-to currency ratio was already saved today inside 'ratios.json', and we want to get it

        today = datetime.date.today().isoformat()

        if today in self.ratio_data and f"{self.base}{self.target}" in self.ratio_data[today]:
            return float(self.ratio_data[today][f"{self.base}{self.target}"])

        return None

        # Firstly, the function makes sure if both, today's date and from-to currency ratio is saved inside 'ratios.json' file
        # Then it returns float type of the ratio we wanted
        # If not found, it returns None

        # TODO, completed
        # Should read file and receive exchange rate for given base and target currency from that file