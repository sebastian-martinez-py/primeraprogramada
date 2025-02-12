import time
import csv
from lector_data import DataLector
from sorting_algorithms import SortingAlgorithms
from punt_play import PuntPlay


def save_results(filename, plays, start_time, duration, end_time):
    """
    Guarda los resultados en un archivo CSV con formato separado por punto y coma (;)
    """
    with open(filename, "w", encoding="utf-8", newline="") as file:
        writer = csv.writer(file, delimiter=";")
        
        writer.writerow(["start_time", "duracion", "end_time", "game_id", "teams", "yards", "qtr", "date", "time"])
        
        for play in plays:
            writer.writerow([f"{start_time:.4f}", f"{duration:.4f}s", f"{end_time:.4f}", play.game_id, play.teams, play.yards, play.qtr, play.date, play.time])

    print(f"Resultados guardados en: {filename}")

if __name__ == "__main__":
    
    file = "pbp_2017.csv" 
    lector = DataLector(file)
    plays = lector.process_plays()

    if not plays:
        print("No se encontraron jugadas de despeje.")
        exit()

    print(f"Total de jugadas de despeje encontradas: {len(plays)}\n")

    
    sorting_algorithms = {
        "bubble_sort": SortingAlgorithms.bubble_sort,
        "insertion_sort": SortingAlgorithms.insertion_sort,
        "merge_sort_recursive": SortingAlgorithms.merge_sort_recursive,
        "merge_sort_iterative": SortingAlgorithms.merge_sort_iterative,
        "quick_sort_recursive": SortingAlgorithms.quick_sort_recursive,
        "quick_sort_iterative": SortingAlgorithms.quick_sort_iterative
    }


    for name, sort_function in sorting_algorithms.items():
        print(f"Ejecutando {name}...")

        start_time = time.time()
        sorted_plays, duration = sort_function(plays[:])  
        end_time = time.time()

       
        print(f"Inicio: {start_time:.4f} | Duración: {duration:.4f}s | Fin: {end_time:.4f}\n")

        
        filename = f"segunda_parte_{name}_resultado.csv"
        save_results(filename, sorted_plays, start_time, duration, end_time)
