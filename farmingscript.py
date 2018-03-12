import requests

url = "http://api.rsbuddy.com/grandExchange?a=guidePrice&i="
max_profit = 0
most = "none"

exchange_ids = {"Astral Rune": "9075", "Nature Rune": "561", "Supercompost": "6034", "Ultracompost": "21483" }



prices = {}

def get_item_cost(item_id):
    full_url = url + itemid
    response = requests.get(full_url)
    data = response.json()
    return data['overall']

def check_max(to_check, current_max):
    if to_check.profit > current_max:
        return True


def check_herb(herb_name, number, seed_number):
    global most
    global max_profit
    herb = Herb(herb_name, number, seed_number)
    herb.calc_profit()
    herb.print()
    if check_max(herb, max_profit):
        most = herb.name
        max_profit = herb.profit


class Herb:
    name = "x"
    num = "x"
    seedNum = "x"
    seedPrice = 0
    price = 0
    profit = 0

    def __init__(self, the_name, n, sn):
        self.name = the_name
        self.num = n
        self.seedNum = sn

    def calc_profit(self):
        self.price = get_item_cost(str(self.num))
        self.seedPrice = get_item_cost(str(self.seedNum))
        self.profit = (self.price*6.5) - self.seedPrice

    def print(self):
        print(self.name.upper())
        print("\tBuy: ", self.seedPrice)
        print("\tSell: ", self.price)
        print("\tProfit: ", self.profit)


#check herb with (name, herb id, seed id)
check_herb("ranarr", 257, 5295)
check_herb("torstol", 269, 5304)
check_herb("snapdragon", 3000, 5300)
check_herb("avantoe", 261, 5298)
check_herb("dwarf weed", 267, 5303)
check_herb("kwuarm", 263, 5299)
check_herb("toadflax", 2998, 5296)
check_herb("lantadyme", 2481, 5302)
check_herb("cadantine", 265, 5301)
check_herb("irit", 259, 5297)

print("\nMost profit: ", most.upper(), "at", max_profit, "gp.")
enter = input("Press ENTER to close...")