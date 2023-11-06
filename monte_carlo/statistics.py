from random import randint
from math import sqrt

def throw_dice(n_tries: int, n_shots:int) -> list[list[int]]:
    shots_try = lambda n_shots: [randint(1, 6) for _ in range(n_shots)]
    return [shots_try(n_shots) for _ in range(n_tries)]

def calc_media(list_tries:list) -> float:
    """
    Calculates the media µ of a list[int] or a list[list[int]]
    """
    medias=[]
    if type(list_tries[0]) == list:
        for one_try in list_tries:
            medias.append(sum(one_try) / len(one_try))
    else:
        medias = list_tries

    return sum(medias) / len(medias)

def calc_occurrence_proportion(list_tries:list[list[int]], num:int) -> float:
    """
    Calculates the "occurrence proportion" or "relative frequency"
    of num in the given list of lists.
    """
    media = []
    # Calculate media µ
    for one_try in list_tries:
        media.append(one_try.count(num) / len(one_try))
    return sum(media) / len(media)

def calc_variability(tries:list[list[int]]) -> float:
    mu = calc_media(tries)
    variab = sum([])

def calc_variability_of_occurrence_proportions(shots_tries:list[list[int]], num:int) -> float:
    mu = calc_occurrence_proportion(shots_tries, num)
    media = sum([((a_try.count(num)/len(a_try)) - mu)**2 for a_try in shots_tries]) / len(shots_tries)
    return media

def calculate_standard_deviation(variability:float) -> float:
    return variability**0.5

if __name__ == "__main__":
    n_tries = int(input("Ingrese la cantidad de iteraciones: "))
    n_shots = int(input("Ingrese cantidad de tiros por iteración: "))
    num = int(input("De qué número quiere calcular la probabilidad de salida?: "))
    
    shots_tries = throw_dice(n_tries, n_shots)
    variability = calc_variability_of_occurrence_proportions(shots_tries, num)
    std_deviation = calculate_standard_deviation(variability)
    print (f"variability= {variability}, std deviation= {std_deviation}")