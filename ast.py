import re

class Node:
    def __init__(self, node_type, left=None, right=None, value=None):
        self.type = node_type
        self.left = left
        self.right = right
        self.value = value

def tokenize(rule_string):
    # Tokenize the input string into operators, operands, and parentheses
    tokens = re.findall(r'\s*(=>|<=|>=|==|!=|AND|OR|[()<>]|[\w]+)\s*', rule_string)
    return tokens

def parse_expression(tokens):
    def parse_primary():
        token = tokens.pop(0)
        if token == '(':
            node = parse_or_expression()
            tokens.pop(0)  # Remove the closing ')'
            return node
        else:
            return Node('operand', value=token)

    def parse_and_expression():
        left = parse_primary()
        while tokens and tokens[0] == 'AND':
            tokens.pop(0)  # Remove the 'AND'
            right = parse_primary()
            left = Node('operator', left=left, right=right, value='AND')
        return left

    def parse_or_expression():
        left = parse_and_expression()
        while tokens and tokens[0] == 'OR':
            tokens.pop(0)  # Remove the 'OR'
            right = parse_and_expression()
            left = Node('operator', left=left, right=right, value='OR')
        return left

    # Start parsing from the top-level 'OR' expressions
    return parse_or_expression()

def create_rule(rule_string):
    tokens = tokenize(rule_string)
    ast = parse_expression(tokens)
    return ast
