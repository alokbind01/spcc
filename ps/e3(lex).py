# Lexical Analyzer
# Define functions to identify tokens
def is_keyword(word):
    keywords = ['if', 'else', 'while', 'for', 'int', 'float', 'char', 'return']
    return word in keywords

def is_identifier(word):
    return word.isidentifier() and not is_keyword(word)

def is_integer_literal(word):
    try:
        int(word)
        return True
    except ValueError:
        return False

def is_float_literal(word):
    try:
        float(word)
        return True
    except ValueError:
        return False

def is_operator(word):
    operators = ['+', '-', '*', '/', '=', '==', '!=', '<', '>', '<=', '>=']
    return word in operators

def is_delimiter(word):
    delimiters = ['(', ')', '{', '}', '[', ']', ',', ';']
    return word in delimiters

# Define function for lexical analysis
def lexical_analyzer(code):
    tokens = []
    lines = code.split('\n')
    for line in lines:
        words = line.split()
        for word in words:
            if is_keyword(word):
                tokens.append((word, 'Keyword'))
            elif is_identifier(word):
                tokens.append((word, 'Identifier'))
            elif is_integer_literal(word):
                tokens.append((word, 'Integer Literal'))
            elif is_float_literal(word):
                tokens.append((word, 'Float Literal'))
            elif is_operator(word):
                tokens.append((word, 'Operator'))
            elif is_delimiter(word):
                tokens.append((word, 'Delimiter'))
            else:
                tokens.append((word, 'Unknown'))

    return tokens

# Main program
if __name__ == "__main__":
    code = """int main() {
                    int x = 10 ;
                    float y = 3.14 ;
                    if ( x == 10 ) {
                        printf ( " Hello , World ! " ) ;
                    }
                }"""

    print("Input Code:")
    print(code)

    print("\nLexical Analysis:")
    tokens = lexical_analyzer(code)
    for token in tokens:
        print(token[0], "-", token[1])

# Output: Input Code:
# int main() {
#                     int x = 10;
#                     float y = 3.14;
#                     if (x == 10) {
#                         printf("Hello, World!");
#                     }
#                 }

# Lexical Analysis:
# int - Keyword
# main() - Unknown
# { - Delimiter
# int - Keyword
# x - Identifier
# = - Operator
# 10; - Unknown
# float - Keyword
# y - Identifier
# = - Operator
# 3.14; - Unknown
# if - Keyword
# (x - Unknown
# == - Operator
# 10) - Unknown
# { - Delimiter
# printf("Hello, - Unknown
# World!"); - Unknown
# } - Delimiter
# } - Delimiter
