import csv
import os
from punt_play import PuntPlay

class DataLector:
   

    def __init__(self, filename):
        self.filename = filename

    def process_plays(self):
        if not os.path.exists(self.filename):
            print(f"Error de carga: El archivo {self.filename} no existe.")
            return []

        plays = []

        try:
            with open(self.filename, "r", encoding="utf-8") as file:
                reader = csv.reader(file)
                header = next(reader)  
                print(f"Archivo cargado correctamente: {self.filename}")
                print("Encabezado del archivo CSV:", header)

                
                DESC_IDX = 19       
                GAME_ID_IDX = 1     
                POSTEAM_IDX = 17    
                DEFTEAM_IDX = 18    
                YARDS_IDX = 21      
                QTR_IDX = 4         

                for i, data in enumerate(reader):
                    
                    if len(data) <= max(DESC_IDX, GAME_ID_IDX, POSTEAM_IDX, DEFTEAM_IDX, YARDS_IDX, QTR_IDX):
                        print(f"Saltando línea {i+1}: datos incompletos → {data}")
                        continue

                    description = data[DESC_IDX].strip('"').lower()  

                    
                    if i < 5:
                        print(f"Descripción {i+1}: {description}")

                    
                    if "punt" in description and "fumble" not in description:
                        game_id = data[GAME_ID_IDX]
                        teams = f"{data[POSTEAM_IDX]}@{data[DEFTEAM_IDX]}"

                        
                        try:
                            yards = int(float(data[YARDS_IDX])) 
                            qtr = int(data[QTR_IDX])
                        except ValueError:
                            print(f"Saltando línea {i+1} por datos inválidos en Yards o Qtr: {data[YARDS_IDX]}, {data[QTR_IDX]}")
                            continue  

                        plays.append(PuntPlay(game_id, teams, yards, qtr))

                print(f"Jugadas de despeje encontradas: {len(plays)}")
        except Exception as e:
            print(f"ERROR al leer el archivo: {e}")
            return []

        return plays

                




