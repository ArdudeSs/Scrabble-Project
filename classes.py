

class Player:
    def __init__(self, name: str):
        if not name:
            raise ValueError("Your name shouldn't be blank!")
        elif len(name) > 30:
            raise ValueError("Please use a shorter name.")
        else:
            self.name: str = name
            self.score: int = 0
            self.rack: list[Tile | str] = ["_", "_", "_", "_", "_", "_", "_"]

class Tile:
    def __init__(self, l: str):
        self.letter = l
        if l in {'A', 'E', 'I', 'O', 'U', 'R', 'T', 'N', 'S', 'L'}:
            self.value = 1
        elif l in {'D', 'G'}:
            self.value = 2
        elif l in {'B', 'C', 'M', 'P'}:
            self.value = 3
        elif l in {'F', 'H', 'W', 'Y', 'V'}:
            self.value = 4
        elif l == 'K':
            self.value = 5
        elif l in {'J', 'X'}:
            self.value = 8
        elif l in {'Z', 'Q'}:
            self.value = 10

# class WordList:

#     def __init__(self, word_list_name: str):
        
#         with open(f"{word_list_name}") as f:
#             line = f.readline()
#             self.acceptable_words = set()
#             while line:
#                 self.acceptable_words.add(line)



