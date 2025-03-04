from enum import Enum, auto

class Player:
    def __init__(self, name: str):
        if not name:
            raise ValueError("Your name shouldn't be blank!")
        elif len(name) > 30:
            raise ValueError("Please use a shorter name.")
        else:
            self.name: str = name
            self.score: int = 0
            self.rack: list[Tile] = []

    def get_rack_value(self):
        return sum(t.value for t in self.rack if isinstance(t, Tile))

    def __str__(self):
        return self.name

class Tile:
    def __init__(self, l: str):
        self.letter: str = l

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
        elif l == '?':
            self.value = 0

    def __str__(self):
        return self.letter

class GameStatus(Enum):
    DONE = auto() # The game ends when the tile bag is exhausted and one player's rack has been exhausted.
    ONGOING = auto()
    PLAYER_DECISION = auto()


class Premium(Enum):
    DOUBLE_WORD = auto()
    DOUBLE_LETTER = auto()
    TRIPLE_WORD = auto()
    TRIPLE_LETTER = auto()

class Cell:
    def __init__(self, prem: str, r: int, c: int):
        self.row: int = r
        self.col: int = c
        self.premium: Premium | None
        self.rep = prem 
        self.tile: Tile | None = None # this is the tile occupying the cell.
        match prem:
            case 'DW':
                self.premium = Premium.DOUBLE_WORD
            case 'DL':
                self.premium = Premium.DOUBLE_LETTER
            case 'TL':
                self.premium = Premium.TRIPLE_LETTER
            case 'TW':
                self.premium = Premium.TRIPLE_WORD
            case '_':
                self.premium = None

    def __str__(self):
        return self.rep

class Word:
    def __init__(self, tiles: list[Tile]):
        self.word: str = ''
        self.score: int = 0
        for tile in tiles:
            self.word += tile.letter
            self.score += tile.value






