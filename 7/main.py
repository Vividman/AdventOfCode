import functools
from functools import total_ordering
with open("C:\\Users\\dn\\Desktop\\Prosjektarbeid\\AdventOfCode\\7\\input.txt") as f:
    lines = f.readlines()
# with open("C:\\Users\\dn\\Desktop\\Prosjektarbeid\\AdventOfCode\\7\\test.txt") as f:
#     lines = f.readlines()

card_values = {
    'A':14, 'K':13, 'Q':12, 'T':10, '9':9, '8':8, '7':7, '6':6, '5':5, '4':4, '3':3, '2':2, 'J':1
}

@total_ordering
class Hand():
    def __init__(self, hand:list, bid:int) -> None:
        self.hand = hand
        self.bid = bid
        self.type = 0
        self.define()

    def __lt__(self, __value: object) -> bool:
        if self.type == __value.type:
            for i, card in enumerate(self.hand):
                if card != __value.hand[i]:
                    return_value = card_values[card] < card_values[__value.hand[i]]
                    return return_value
        else: 
            return self.type < __value.type
    
    def __eq__(self, __value: object) -> bool:
        return self.hand == __value.hand
    
    def __repr__(self) -> str:
        return f"{self.hand}: {self.get_type()} {self.bid}"
    
    def define(self):
        d = {}
        for card in self.hand:
            if card not in d:
                d[card] = 1
            else:
                d[card] += 1
        
        if 'J' in d and len(d) > 1:
            count = d['J']
            del d['J']
            big = ''
            value = 0
            for k, v in d.items():
                if v > value:
                    value = v
                    big = k
            d[big] += count

        self.type = self.determine_type(d)
        
    def determine_type(self, d:dict) -> int:
        if len(d) == 5:
             # High card
            return 0
        elif len(d) == 4:
            # One pair
            return 1
        elif len(d) == 3 and max(d.values()) == 2:
            # Two pair
            return 2
        elif len(d) == 3 and max(d.values()) == 3:
            # Three of a kind
            return 3
        elif len(d) == 2 and max(d.values()) == 3:
            # Full house
            return 4
        elif len(d) == 2 and max(d.values()) == 4:
            # Four of a kind
            return 5
        else:
            # Five of a kind
            return 6
        
    def get_type(self):
        if self.type == 0:
            return 'High card'
        elif self.type == 1:
            return 'One pair'
        elif self.type == 2:
            return 'Two pair'
        elif self.type == 3:
            return 'Three of a kind'
        elif self.type == 4:
            return 'Full house'
        elif self.type == 5:
            return 'Four of a kind'
        else:
            return 'Five of a kind'

hands = []
for line in lines:
    hand, bid = line.split(" ")
    hands.append(Hand(hand, int(bid)))

sum = 0
for i, hand in enumerate(sorted(hands)):
    # if 'J' in hand.hand: print(hand)
    print(hand)
    sum += hand.bid * (i+1)

print(sum)
