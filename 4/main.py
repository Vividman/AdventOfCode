class Card():
    def __init__(self, id:int, winning:list, numbers:list):
        self.id = id
        self.winning = winning
        self.numbers = numbers
        self.instance_count = 1

    def get_matches(self):
        exp = 0
        for number in self.numbers:
            if number in self.winning:
                exp += 1
        return exp
        
    def add_instance(self, count):
        self.instance_count += count

    def __str__(self):
        return f"Card {self.id}: Worth {self.get_matches()}, Instance count: {self.instance_count}"
        
with open("C:\\Users\\dn\\Desktop\\Prosjektarbeid\\AdventOfCode\\4\\input.txt") as f:
    lines = f.readlines()
# with open("C:\\Users\\dn\\Desktop\\Prosjektarbeid\\AdventOfCode\\4\\test.txt") as f:
#     lines = f.readlines()

cards = []
for line in lines:
    card_id, numbers = line.split(":")
    id = int(card_id.replace(" ", "").replace("Card", ""))
    winning, playing = numbers.replace("\n", "").split("|")
    winning_numbers = []
    for number in winning.split(" "):
        if number.isnumeric():
            winning_numbers.append(int(number))

    playing_numbers = []
    for number in playing.split(" "):
        if number.isnumeric():
            playing_numbers.append(int(number))

    cards.append(Card(id, winning_numbers, playing_numbers))

points_total = 0
for card in cards:
    points_total += 2**(card.get_matches()-1) if card.get_matches() >= 0 else 0

print(f"Total points: {points_total}")

for i in range(0, len(cards)):
    worth = cards[i].get_matches()
    for j in range(1, worth+1):
        if i+j < len(cards):
            cards[i+j].add_instance(cards[i].instance_count)

sum_instances = 0
for card in cards:
    sum_instances += card.instance_count
    print(card)

print(f"Number of scratchcards: {sum_instances}")