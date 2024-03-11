import sympy as sp

def NewtonRaiz(Fun, FunDer, X0, TOL, imax):
    for i in range(imax):
        Xi = X0 - Fun(X0) / FunDer(X0)
        if (sp.Abs((Xi - X0) / X0) < TOL):
            Xs = Xi
            print(f"Solução = {Xs}")
            break

        X0 = Xi

        if (i == imax):
            print(f"A solução não foi obtida em {i} iterações.\n")
            Xs = "Sem resposta"

x = sp.Symbol('x') # Criando a variável simbólica 'x'
funcao = (sp.exp(-x ** 2) - sp.cos(x)) # Função a ser calculada
funcao_numerica = sp.lambdify(x, funcao) # Transformando a função simbólica em função com termos númericos para que possa ser calculado em Python
funcao_derivada = sp.diff(funcao)
funcao_derivada_numerica = sp.lambdify(x, funcao_derivada)

NewtonRaiz(funcao_numerica, funcao_derivada_numerica, 1.5, 10e-4, 100)