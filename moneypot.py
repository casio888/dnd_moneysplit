import re
from typing import Union

class Moneypot():
    plat = 0
    gold = 0
    elec = 0
    silv = 0
    copp = 0
    MAP = ['pp', 'gp', 'ep', 'sp', 'cp']

    def __init__(self, data=[0,0,0,0,0]) -> None:
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
        data_chunks = [x for x in re_pattern.split(clean_input) if x != "" and x != "0"]
        
        data = [0,0,0,0,0]
        counter = 0
        for typ in self.MAP:
            for chunk in data_chunks:
                if typ in chunk:
                    data[counter] += int(chunk[:-2])
                    break
            counter+=1
        return self(data)
    

    def to_string(self):
        return " ".join([str(x)+y for x, y in zip(self.get_money(), self.MAP) if x != 0])

    def get_money(self, get_value=False):
        if not get_value:
            return [self.plat, self.gold, self.elec, self.silv, self.copp]
        m = self.get_money()
        multi = [10, 1, 0.5, 0.1, 0.01]
        return sum([ x * y for x, y in zip(m, multi)])


    def add_money(self, val, curr):
        if type(val) != int and val <= 0:
            return
        if curr == 0:
            self.plat += val
        elif curr == 1:
            self.gold += val
        elif curr == 2:
            self.elec += val
        elif curr == 3:
            self.silv += val
        elif curr == 4:
            self.copp += val


    def split(self, num_people, pool_copper=False, debug=False):
        money = self.get_money()
        if (self.get_money(True) * 100) % 4 == 0:
            #Sauber teilbar
            pass
        peeps = [Moneypot() for x in range(num_people)]
        clean = True
        curr = 0
        for x in money:
            if clean and x % num_people == 0:
                for peep in peeps:
                    peep.add_money(int(x/num_people), curr)
            else:
                clean = False
                while x > 0:
                    next = peeps[peep.index(max(peeps))]
                    next.add_money(1, curr)
                    x -= 1
            curr += 1

        return [x.to_string() for x in peeps]

    
    def __gt__(self, other):
        return self.get_money(True) > other.get_money(True)
