# Importando a biblioteca sympy que permite utilizar variáveis simbólicas e tem diversos termos e funções da matemática
import sympy as sp

def bisseccao(f, a, b, TOL, N):
    i = 1
    a1 = a
    b1 = b

    if (f(a) * f(b) > 0):
        raise ValueError("A função tem o mesmo sinal nos pontos a e b")

    print("Int\t a\t b\t solução\t f(x)\t erro\n")
    r = ((a * f(b) - b *f(a)) / f(b) - f(a))
    erro = sp.Abs(b - a) / 2

    while sp.Abs(f(r)) > TOL and i <= N:
        print(f"{i} {a} {b} {r} {f(r)} {erro}")
        
        if (f(r) == 0):
            print(f"Solução exata x = {r}")
            break

        if (f(a) * f(r) < 0):
            b = r
        else:
            a = r

        r_ant = r

        r = (a * f(b) - b * f(a)) / (f(b) - f(a))
        erro = sp.Abs((r - r_ant) / r)
        i += 1

    if (sp.Abs(f(r)) <= TOL):
        print(f"Solução: {r}\n")
    elif (i > N):
        print("Número máximo de interações atingido\n")

    
x = sp.Symbol('x') # Criando a variável simbólica 'x'
funcao = 8 - 4.5 * (x - sp.sin(x)) # Função a ser calculada
funcao_numerica = sp.lambdify(x, funcao) # Transformando a função simbólica em função com termos númericos para que possa ser calculado em Python

bisseccao(funcao_numerica, 2, 3, 0.01, 100) # Chamando a função bisseccao e passando os parâmetros
