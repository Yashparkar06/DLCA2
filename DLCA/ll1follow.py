def compute_follow_sets(grammar, start_symbol):
    follow_sets = {non_terminal: set() for non_terminal in grammar.keys()}
    follow_sets[start_symbol].add('$')
    for non_terminal, productions in grammar.items():
        for production in productions:
            for i, symbol in enumerate(production):
                if symbol in grammar:
                    if i < len(production) - 1:
                        next_symbol = production[i + 1]
                        if next_symbol in grammar:
                            follow_sets[symbol] |= first_sets[next_symbol]
                            if '' in first_sets[next_symbol]:
                                follow_sets[symbol] |= follow_sets[non_terminal]
                        else:
                            follow_sets[symbol].add(next_symbol)
                    else:
                        follow_sets[symbol] |= follow_sets[non_terminal]
    return follow_sets

# Example grammar
grammar = {
    'S': ['AaB'],
    'A': ['aAc', ''],
    'B': ['bB', '']
}

# Compute FIRST sets
first_sets = {
    'S': {'a'},
    'A': {'a', 'c', ''},
    'B': {'b', ''}
}

# Compute FOLLOW sets
follow_sets = compute_follow_sets(grammar, 'S')
print("FOLLOW sets:")
for non_terminal, follow_set in follow_sets.items():
    print(non_terminal, "->", follow_set)
