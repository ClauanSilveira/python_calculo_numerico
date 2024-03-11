import sympy as sp

def SecanteRaiz(Fun, X0, X1, TOL, imax):
    for i in range(imax):
        FunX0 = Fun(X0)
        FunX1 = Fun(X1)
        Xi = (X1 - FunX1 * (X0 - X1) / (FunX0 - FunX1))
        if (sp.Abs((Xi - X1) / X1) < TOL):
            Xs = Xi
            print(f"Solução = {Xs}")
            break

        X0 = X1
        X1 = Xi

        if (i == imax):
            print(f"A solução não foi obtida em {i} iterações.\n")
            Xs = "Sem resposta"

x = sp.Symbol('x') # Criando a variável simbólica 'x'
funcao = (sp.exp(-x ** 2) - sp.cos(x)) # Função a ser calculada
funcao_numerica = sp.lambdify(x, funcao) # Transformando a função simbólica em função com termos númericos para que possa ser calculado em Python

SecanteRaiz(funcao_numerica, 1, 3, 10e-4, 100)