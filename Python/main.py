from os import path
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

def main():
    data = pd.read_csv(path_to_src)
    print(data.columns.values)


if __name__ == "__main__":
    main()