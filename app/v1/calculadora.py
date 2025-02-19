from typeNumbers import Graus, Radianos, Polar, Rect
from operations import soma, subtracao, multiplicacao, divisao
import time
import os

ang = None
def inicio():
    global ang
    os.system('cls' if os.name == 'nt' else 'clear') # Limpa o terminal
    print("---- Calculadora de números complexos ----")
    ang = input("Deseja utilizar radianos ou graus? (R/G): ").upper()
    
    if ang not in ["R", "G"]:
        print("Opção inválida. Tente novamente.")
        time.sleep(1)
        inicio()

    print("Caso queira um número polar, digite P(r, theta)")
    print("Caso queira um número retangular, digite R(x, y)")
    menu()

ans = None
values = []
index = 0
exp = ""

def menu():
    global index, exp, ans
    text = ["- Digite o primeiro número complexo: " if not ans else f"- Digite o primeiro número complexo ou ans ({ans.print(ang)}): ", "- Digite a operação: ", "- Digite o segundo número complexo: "]
    
    while index != len(text):
        if values:
            print(exp)
        value = input(text[index])
        if value == "ans":
            values.append(ans)
            index += 1
            exp += ans.print(ang) + " "
        elif value[0] in ["P", "R"] and index != 1:
            v = value[2:-1].split(", ")
            v = Polar(float(v[0]), Graus(float(v[1])) if ang == "G" else Radianos(float(v[1]))) if value[0] == "P" else Rect(float(v[0]), float(v[1]))
            values.append(v)
            index += 1
            exp += v.print(ang) + " "
        elif value in ["+", "-", "*", "/"] and index == 1:
            values.append(value)
            index += 1
            exp += value + " "
        else:
            print("Entrada inválida.")
            time.sleep(1)
            menu()
    
    V1 = values[0]
    V2 = values[2]
    match values[1]:
        case "+":
            ans = soma(V1, V2)
        case "-":
            ans = subtracao(V1, V2)
        case "*":
            ans = multiplicacao(V1, V2)
        case "/":
            ans = divisao(V1, V2)
    
    if type(V1) == Rect:
        ans = ans.toRect()
    
    print(values[0].print(ang), values[1], values[2].print(ang), "=", ans.print(ang))
    index = 0
    exp = ""
    values.clear()
    reset = input("Reiniciar ou continuar? (R/C): ").upper()
    if reset == "R":
        ans = None
        inicio()
    else:
        os.system('cls' if os.name == 'nt' else 'clear') # Limpa o terminal
        menu()

try:
    inicio()
except KeyboardInterrupt:
    print("\nPrograma encerrado.")