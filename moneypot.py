import re

class Moneypot():
    plat = 0
    gold = 0
    elec = 0
    silv = 0
    copp = 0

    def __init__(self, data) -> None:
        if type(data) != list:
            raise TypeError("Excpected List.")
        if len(data) != 5:
            raise ValueError("List needs 5 integer values.")
        if [x for x in data if type(x) != int]:
            raise ValueError("List needs 5 integer values.")
        
        self.plat = data[0]
        self.gold = data[1]
        self.elec = data[2]
        self.silv = data[3]
        self.copp = data[4]
    
    @classmethod
    def from_string(self, input_str) -> None:
        clean_input = input_str.replace(' ', '').lower()
        if not re.fullmatch(r"^(([0-9])+[pgesc]p)*$", clean_input):
            raise ValueError("No special characters allowed, only numbers, letters and spaces.")
        re_pattern = re.compile(r'(([0-9])+[pgesc]p)')
        MAP = ['pp', 'gp', 'ep', 'sp', 'cp']
        data_chunks = [x for x in re_pattern.split(clean_input) if x != "" and x != "0"]
        
        data = [0,0,0,0,0]
        counter = 0
        for typ in MAP:
            for chunk in data_chunks:
                if typ in chunk:
                    data[counter] += int(chunk[:-2])
                    break
            counter+=1
        return self(data)

    def get_money(self):
        return [self.plat, self.gold, self.elec, self.silv, self.copp]

    def split(self, num_people, pool_copper=False, debug=False):
        pass