from utils import get_input_valido
from logica_jogo import carregar_perguntas, gerar_quiz, guardar_score, mostrar_ranking

def mostrar_menu():
    print("\n=== MENU ===")
    print("1. Jogar")
    print("2. Ver ranking")
    print("3. Regras")
    print("4. Sair")

def mostrar_regras():
    print("\n--- REGRAS ---")
    print("responde as perguntas escolhendo 1, 2, 3 ou 4")
    print("cada resposta certa da 1 ponto")
    print("no fim ve a tua pontuacao")

def main():
    print("bem vindo ao quiz!")
    nome = input("qual e o teu nome? ")

    perguntas = carregar_perguntas()
    if len(perguntas) == 0:
        print("nao foi possivel carregar as perguntas, verifica o ficheiro perguntas.json")
        return

    a_jogar = True


main()