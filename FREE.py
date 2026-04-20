from sympy import symbols, solve, solveset, S
from sympy.parsing.sympy_parser import parse_expr

x = symbols('x')  # On dit que x est notre inconnue

print("=== Solveur d'équations / inéquations ===")
print("Exemples : x**2 - 4 = 0 ,  x**3 + 2*x - 1 > 0 ,  x**4 - 5*x**2 + 4 <= 0")

expression = input("\nEntre ton équation ou inéquation : ")

try:
    # On remplace ^ par ** au cas où l'utilisateur tape x^2
    expression = expression.replace('^', '**')
    
    # On sépare la partie gauche et droite
    if '=' in expression:
        gauche, droite = expression.split('=')
        signe = '='
    elif '>' in expression:
        if '>=' in expression:
            gauche, droite = expression.split('>=')
            signe = '>='
        else:
            gauche, droite = expression.split('>')
            signe = '>'
    elif '<' in expression:
        if '<=' in expression:
            gauche, droite = expression.split('<=')
            signe = '<='
        else:
            gauche, droite = expression.split('<')
            signe = '<'
    else:
        print("Il manque =, >, <, >= ou <=")
        exit()
    
    # On met tout du même côté : gauche - droite = 0
    eq = parse_expr(gauche) - parse_expr(droite)
    
    # On résout
    if signe == '=':
        solutions = solve(eq, x)
        print(f"\nSolutions de {expression} :")
        if solutions:
            for sol in solutions:
                print(f"x = {sol.evalf()}")  # evalf() donne la valeur décimale
        else:
            print("Pas de solution")
            
    else:  # C'est une inéquation
        solutions = solveset(eval(f"eq {signe} 0"), x, domain=S.Reals)
        print(f"\nSolutions de {expression} :")
        print(f"S = {solutions}")

except Exception as e:
    print(f"Erreur : {e}")
    print("Vérifie la syntaxe. Exemple correct : x**3 - 2*x + 1 = 0")