import pandas as pd 
import os
def loadData():
    data = pd.read_csv("BeatlesDataset.csv")
    return data

def yearSearch():

    data = loadData()
    print("Digite o ano da música")
    year = int(input())

    if year > 2003 and year < 1960:
        print('Insira uma data válida!')

    result = data[data['Year'] == year]
        
    print(result)
    return True


def nameSearch():
    data = loadData()

    print("Digite o nome (ou parte do nome) da música:")
    name = input()

    result = data[data['Title'].str.contains(name, case=False)]
    print(result)
  

def writerSearch():
    data = loadData()
    print("Digite o sobrenome do compositor")
    
    composer = input()
    result = data[data['Songwriter'].str.contains(composer, case=False)]
    print (result)

    print('Deseja pesquisar mais a a fundo?')
    print('1. Sim, por ano')

    choice = input()

    if choice == "1":
        print("Digite o ano da música")
        year = int(input())
        result = result[result['Year'] == year]
        print(result)
    return True



def main():
    while True:
        print("Pressione qualquer tecla para ir para o menu inicial")
        input()
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Escolha uma das opções abaixo")
        print("1. Pesquisa por ano")
        print("2. Pesquisa por nome")
        print("3. Pesquise por compositor")
        print("4. Sair")

        choice = input()

   
        if choice == "1":
            yearSearch()
            
        if choice == "2":
            nameSearch()
            
        if choice == "3":
            writerSearch()
        if choice == "4":
            break
        



if __name__ == "__main__":
    main()
