import json, datetime, urllib.request, os.path, requests


class RatioObtainer:
    base = None
    target = None

    def __init__(self, base, target):
        self.base = base
        self.target = target

    def was_ratio_saved_today(self):
        # TODO

        if os.path.exists('../ratios.json'):
            file = open('../ratios.json', 'r')
            data = json.load(file)
            file.close()

            timestamp = data.get('timestamp')
            humantime = datetime.datetime.fromtimestamp(timestamp)

            if str(humantime).split()[0] == str(datetime.date.today()):

                return True

            else:

                return False

        else:
            file = open('../ratios.json', 'a')
            file.close()

            return False

        # This function checks if given ratio was saved today and if the file with ratios is created at all
        # should return false when file doesn't exist or if there's no today's exchange rate for given values at all
        # should return true otherwise


        pass

    def fetch_ratio(self):
        # TODO

        response = requests.get('http://api.exchangerate.host/live?access_key=1cae1afae99e25e160df804ec9f149a1&format=1')

        return RatioObtainer.save_ratio(response)

        # This function calls API for today's exchange ratio
        # Should ask API for today's exchange ratio with given base and target currency
        # and call save_ratio method to save it
        pass

    def save_ratio(self, ratio):
        # TODO

        if RatioObtainer.was_ratio_saved_today():
            pass
        else:
            file = open('../ratios.json', 'w+')
            file.write(json.dumps(ratio.json(), indent=4))
            file.close()


        # Should save or update exchange rate for given pair in json file
        # takes ratio as argument
        # example file structure is shipped in project's directory, yours can differ (as long as it works)
        pass

    def get_matched_ratio_value(self):
        # TODO
        # Should read file and receive exchange rate for given base and target currency from that file
        pass
