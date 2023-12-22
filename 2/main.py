class Game():
    def __init__(self, id, maxR, maxG, maxB):
        self.id = id
        self.maxR = maxR
        self.maxG = maxG
        self.maxB = maxB

    def possible(self, r, g, b):
        return self.maxR <= r and self.maxG <= g and self.maxB <= b
    
    def print(self):
        print(f"Game {self.id}: Red {game.maxR}, Green {game.maxG}, Blue {game.maxB}")
    

if __name__ == "__main__":
    with open("C:\\Users\\dn\\Desktop\\Prosjektarbeid\\AdventOfCode\\2\\input.txt") as f:
        lines = f.readlines()

    games = []
    for line in lines:
        game_id, game_moves = line.split(": ")
        id = int(game_id.replace("Game ", ""))
        maxR, maxG, maxB = 0, 0, 0
        for move in game_moves.split("; "):
            for draw in move.split(", "):
                if "red" in draw:
                    number = int(draw.replace(" red", ""))
                    if maxR < number: maxR = number
                if "green" in draw:
                    number = int(draw.replace(" green", ""))
                    if maxG < number: maxG = number
                if "blue" in draw:
                    number = int(draw.replace(" blue", ""))
                    if maxB < number: maxB = number
        game = Game(id, maxR, maxG, maxB)
        games.append(game)

    sum = 0
    for game in games:
        if game.possible(12, 13, 14): 
            sum += game.id

    print(f"Sum possible game IDs: {sum}")

    sum_powers = 0
    for game in games:
        sum_powers += game.maxR * game.maxG * game.maxB

    print(f"Sum powers: {sum_powers}")
