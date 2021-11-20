import pandas as pd

# Function

# Main 

path_to_src = '../Data/Buddy program.csv'

fast_curious_labels =  [
    'FAST&CURIOUS [Video Games / Board Games]',
    'FAST&CURIOUS [Peaky Blinders /Weed Grinders]',
    'FAST&CURIOUS [Tarantino / Tarantula]',
    'FAST&CURIOUS [Latino/Rap ]',
    'FAST&CURIOUS [Nemo / The Lion King]',
    'FAST&CURIOUS [PSG / Olympique de Marseille]',
    'FAST&CURIOUS [Aya Nakamura/Macarena]',
    'FAST&CURIOUS [Pain au chocolat/Chocolatine]',
    'FAST&CURIOUS [Trench coat/French goat (cheese)]',
    'FAST&CURIOUS [Breaking Bad/Desperate Housewives]',
    'FAST&CURIOUS [French kisses/COVID distances]',
    'FAST&CURIOUS [Netflix Night/Welcome Night]'
]

def fast_curious_match(data):
    limit = data.shape[0]
    element = data.shape[1]

    match_tab = [[0] * limit for x in range(limit)]

    for indexA in range(limit):
        lineA = data.iloc[indexA]
        for indexB in range(indexA, limit):
            sum = 0
            if(indexA != indexB):
                lineB = data.iloc[indexB]
                for index in range(element):
                    if(lineA.iloc[index] == lineB.iloc[index]):
                        sum+=1
                match_tab[indexA][indexB] = sum
                match_tab[indexB][indexA] = sum
    return match_tab

def best_match(data, match_tab):

    match_dict = []

    for index in range(len(match_tab)):
        line = match_tab[index].copy()
        sorted_line = sorted(line, reverse=True)
        for idx in range(5):
            max_value = sorted_line[idx]
            max_index = line.index(max_value)

            line[max_index] = 0

            name1 = data.iloc[index]['First name'] + " " + data.iloc[index]['Last name']
            name2 = data.iloc[max_index]['First name'] + " " + data.iloc[max_index]['Last name']

            dict = {'couple': [name1, name2], 'value': max_value}

            match_dict.append(dict)
    return match_dict

def main():
    data = pd.read_csv(path_to_src)
    fast_curious = data[fast_curious_labels]

    tab_fast_curious = fast_curious_match(fast_curious)
    match = best_match(data, tab_fast_curious)
    sorted_match = sorted(match, key = lambda d : d['value'],reverse=True)
    
    [print(val) for val in sorted_match]

if __name__ == "__main__":
    main()