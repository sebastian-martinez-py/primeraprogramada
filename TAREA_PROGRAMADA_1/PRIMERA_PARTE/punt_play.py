class PuntPlay:
    """
    Clase que representa una jugada de despeje en un partido de fútbol americano.
    """

    def __init__(self, game_id, teams, yards, qtr):
        self.game_id = game_id
        self.teams = teams
        self.yards = yards
        self.qtr = qtr

    def __repr__(self):
        return f"PuntPlay({self.game_id}, {self.teams}, {self.yards}, {self.qtr})"

    def __eq__(self, other):
        return self.yards == other.yards

    def __lt__(self, other):
        return self.yards < other.yards

    def __gt__(self, other):
        return self.yards > other.yards



