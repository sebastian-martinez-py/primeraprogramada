import os
from punt_play import PuntPlay

class DataLector:
    def __init__(self, filename):
        self.filename = filename

    def process_plays(self):
        if not os.path.exists(self.filename):
            print(f"ERROR: El archivo {self.filename} no existe.")
            return []

        plays = []
        with open(self.filename, "r", encoding="utf-8") as file:
            header = next(file).strip().split(",")  
            print("Encabezado del archivo CSV:", header)  

            for i, line in enumerate(file):
                data = line.strip().split(",")

                if len(data) < 22:  
                    continue

                
                description = data[19].lower()  
                if "punt" in description and "fumble" not in description:
                    game_id = data[1]  
                    teams = f"{data[17]}@{data[18]}"  
                    try:
                        yards = int(data[21])  
                        qtr = int(data[4])  
                        date = data[0]  
                        time = data[6]  
                    except ValueError:
                        continue  

                    plays.append(PuntPlay(game_id, teams, yards, qtr, date, time))

        print(f"Total de jugadas de despeje encontradas: {len(plays)}\n")
        return plays


   

    