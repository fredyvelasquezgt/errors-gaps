from antlr4 import *
from build.yaplLexer import yaplLexer
from build.yaplParser import yaplParser
from yaplErrorListener import yaplErrorListener
from rich.console import Console
from rich.tree import Tree
import sys

console = Console()

def build_tree_rich(node, rule_names):
    """
    Recursively build a rich tree representation.
    """
    if isinstance(node, str):
        return Tree(node)
    
    s = node.toStringTree(rule_names)
    parts = s.split(" ")

    root = Tree(parts[0])

    for part in parts[1:]:
        if part:
            child_tree = build_tree_rich(part, rule_names)
            root.add(child_tree)

    return root

def main(argv):
    input = FileStream(argv[1])

    lexer = yaplLexer(input)
    lexer.removeErrorListeners()
    lexer.addErrorListener(yaplErrorListener())

    stream = CommonTokenStream(lexer)
    stream.fill()

    




    console.print("Tokens:")
    for token in stream.tokens:
        console.print(token)

    if lexer._listeners[0].lexical_errors:
        console.print("[bold red]Errores Léxicos Detectados:[/bold red]")
    for error in lexer._listeners[0].lexical_errors:
        token, line, msg = error
        if token:
            console.print(f"Token: {token.text} en la línea {line}. Mensaje: {msg}")
        else:
            console.print(f"Error desconocido en la línea {line}. {msg}")

    parser = yaplParser(stream)
    parser.removeErrorListeners()
    parser.addErrorListener(yaplErrorListener())

    tree = parser.prog()

    rich_tree = build_tree_rich(tree, parser.ruleNames)
    console.print(rich_tree)

if __name__ == '__main__':
    main(sys.argv)
