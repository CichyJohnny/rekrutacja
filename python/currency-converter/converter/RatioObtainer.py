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
        if os.path.exists(self.data_file):
            with open(self.data_file, 'r') as file:
                data = json.load(file)

            return data

        return {}


    def was_ratio_saved_today(self):
        today = datetime.date.today().isoformat()

        return today in self.ratio_data and f"{self.base}{self.target}" in self.ratio_data[today]


        # TODO
        # This function checks if given ratio was saved today and if the file with ratios is created at all
        # should return false when file doesn't exist or if there's no today's exchange rate for given values at all
        # should return true otherwise


    def fetch_ratio(self):
        base = str(self.base)
        target = str(self.target)
        url_path = f'http://api.exchangerate.host/live?access_key=cd007cacde18395212e8ab232cb5f260&source={base}&format=1'
        response = requests.get(url_path)
        ratio_data = response.json()
        self.save_ratio(ratio_data)

        quotes = response.json().get('quotes')
        ratio_value = quotes.get(base + target)

        return float(ratio_value)


        # TODO
        # This function calls API for today's exchange ratio
        # Should ask API for today's exchange ratio with given base and target currency
        # and call save_ratio method to save it


    def save_ratio(self, ratio_data):
        today = datetime.date.today().isoformat()

        if today not in self.ratio_data:
            self.ratio_data[today] = {}
        self.ratio_data[today][f"{self.base}{self.target}"] = ratio_data[f'quotes'][f"{self.base}{self.target}"]

        with open(self.data_file, 'w') as file:
            json.dump(self.ratio_data, file, indent=4)


        # TODO
        # Should save or update exchange rate for given pair in json file
        # takes ratio as argument
        # example file structure is shipped in project's directory, yours can differ (as long as it works)


    def get_matched_ratio_value(self):
        today = datetime.date.today().isoformat()

        if today in self.ratio_data and f"{self.base}{self.target}" in self.ratio_data[today]:
            return float(self.ratio_data[today][f"{self.base}{self.target}"])

        return None



        # TODO
        # Should read file and receive exchange rate for given base and target currency from that file