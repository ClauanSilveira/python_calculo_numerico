import sympy as sp

def falsa_posicao(f, a, b, TOL, N):
    i = 1

    a1 = a
    b1 = b

    if ((f(a) * f(b)) > 0):
        raise ValueError("Erro: a função tem o mesmo sinal nos pontos a e b")

    print(f"Int\t a\t b \t solução\t f(x)\t erro\n")
    r = (((a * f(b)) - (b * f(a))) / (f(b) - f(a)))
    erro = sp.Abs(b - a) / 2

    while (sp.Abs(f(r)) > TOL and i <= N):
        print(f"{i}\t{a}\t{b}\t{r}\t{f(r)}\t{erro}\n")

        if (f(r) == 0):
            print(f"Solução exata x = {r} encontrada\n")
            break

        if ((f(a) * f(r)) < 0):
            b = r
        else:
            a = r

        r_ant = r
        r = (((a * f(b)) - (b * f(a))) / (f(b) - f(a)))
        erro = sp.Abs((r - r_ant) / r)
        i += 1

        if (sp.Abs(f(r)) <= TOL):
            print(f"Solução: {r}\n")
        elif (i > N):
            print("Número máximo de interações atingido\n")

x = sp.Symbol('x') # Criando a variável simbólica 'x'
funcao = (sp.exp(-x ** 2) - sp.cos(x)) # Função a ser calculada
funcao_numerica = sp.lambdify(x, funcao) # Transformando a função simbólica em função com termos númericos para que possa ser calculado em Python

falsa_posicao(funcao_numerica, 1, 2, 10e-4, 100) # Chamando a função bisseccao e passando os parâmetros
