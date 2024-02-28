import re

# Define regular expressions for lexicon tokens
token_patterns = [
    ('<INTEGER>', r'\d+'),
    ('<IDENTIFIER>', r'[a-zA-Z][a-zA-Z0-9_]*'),
    ('<OPERATOR>', r'[+\-*<>&.@/:=˜|$!#%^_[\]{}"`?]+'),
    ('<STRING>', r"'(?:\\t|\\n|\\\'|\\\\|[^()\',;\s])+'"),
    ('<DELETE>', r'(?:\s+|//.*$)'),
    ('(', r'\('),
    (')', r'\)'),
    (';', r';'),
    (',', r',')
]

# Combine all token patterns into a single regular expression
combined_pattern = '|'.join('(?P<{}>{})'.format(name, pattern) for name, pattern in token_patterns)

def lex(input_string):
    tokens = []
    for match in re.finditer(combined_pattern, input_string):
        for name, value in match.groupdict().items():
            if value:
                tokens.append((name, value))
                break
    return tokens

# Example usage
input_string = "let x = 10 in x + 5;"
tokens = lex(input_string)
for token in tokens:
    print(token)
