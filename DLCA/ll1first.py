def compute_first_sets(grammar):
    first_sets = {}

    def compute_first(symbol):
        if symbol in first_sets:
            return first_sets[symbol]

        first_set = set()
        if symbol not in grammar:
            first_set.add(symbol)
            return first_set

        for production in grammar[symbol]:
            first_symbol = production[0]
            if first_symbol != symbol:
                first_set |= compute_first(first_symbol)
            else:
                continue
        return first_set

    for non_terminal in grammar:
        first_sets[non_terminal] = compute_first(non_terminal)
    return first_sets

# Example grammar
grammar = {
    'S': ['aAB', 'bBA', 'c'],
    'A': ['a', 'b'],
    'B': ['b', 'c']
}

# Compute FIRST sets
first_sets = compute_first_sets(grammar)
print("FIRST sets:")
for non_terminal, first_set in first_sets.items():
    print(non_terminal, "->", first_set)
