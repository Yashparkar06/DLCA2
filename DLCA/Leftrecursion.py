grammar={
    'S':[('L'),'x'],
    'L':['LS','S']
}
def rec(grammar):
    non_terminals=list(grammar.keys())
    for A in non_terminals:
        prod=grammar[A]
        alp_prd=[]
        beta_prd=[]
        for production in prod:
            if production.startswith(A):
                alp_prd.append(production[1:])
            else:
                beta_prd.append(production)
        if len(alp_prd) == 0:
            continue
        grammar[A]=[]
        new_non_terminal=A+" ' "
        grammar[A].extend([beta+new_non_terminal for beta in beta_prd])
        grammar[new_non_terminal]=[alp+new_non_terminal if alp !=' ' else 'ε' for alp in alp_prd]+['ε']
    return grammar

op=rec(grammar)
print(op)