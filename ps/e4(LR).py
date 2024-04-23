def eliminate_left_recursion(grammar):
    non_terminals = list(grammar.keys())

    for A in non_terminals:
        productions_A = grammar[A]

        # Split productions into left-recursive and non-left-recursive
        left_recursive_productions = [prod for prod in productions_A if prod.startswith(A)]
        non_left_recursive_productions = [prod for prod in productions_A if not prod.startswith(A)]

        if not left_recursive_productions:
            continue

        # Create a new non-terminal A' for the non-left-recursive productions
        A_prime = A + "'"
        grammar[A_prime] = [prod[len(A):] + A_prime for prod in left_recursive_productions] + ["ε"]

        # Update original non-terminal A with non-left-recursive productions followed by A'
        grammar[A] = [prod + A_prime for prod in non_left_recursive_productions]

    return grammar

# Function to parse user input for grammar
def parse_grammar():
    grammar = {}
    while True:
        production = input("Enter production (or type 'done' to finish): ").strip()
        if production.lower() == 'done':
            break
        non_terminal, rhs = production.split('->')
        non_terminal = non_terminal.strip()
        rhs = [symbol.strip() for symbol in rhs.split('|')]
        grammar[non_terminal] = rhs
    return grammar

# Main program
if __name__ == "__main__":
    print("Enter the grammar productions:")
    user_grammar = parse_grammar()

    # Eliminate left recursion
    eliminated_grammar = eliminate_left_recursion(user_grammar)

    # Print the modified grammar
    print("\nModified Grammar after eliminating left recursion:")
    for non_terminal, productions in eliminated_grammar.items():
        print(f"{non_terminal} -> {' | '.join(productions)}")

# Input
# E -> E + T | T
# T -> T * F | F
# F -> (E)|id
# done