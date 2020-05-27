import typing
from datetime import date

NHL_INCEPTION = date(1917, 11, 26)
GAMES_IN_SEASON = 1271

class GameID:
    def __init__(self, id: str) -> None:
        if id.isdigit() and validate_id(id):
            #  retrieve the game information and store it here
            pass
        else:
            raise ValueError('Invalid Game ID processed')
    
    def __repr__(self):
        return f'Game ID {self.game_id} between {self.home} and {self.away}'

    def validate_id(self, id: str) -> bool:
        if len(id) != 10:
            return False
        year = id[:4]
        if year < NHL_INCEPTION.year or year > date.today().year:
            return False
        game = int(id[-4:])
        if game < 1 or game > GAMES_IN_SEASON:
            return False
        game_type = int(id[4:6])
        return game_type <= 4 and game_type >= 1
