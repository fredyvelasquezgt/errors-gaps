from antlr4.error.ErrorListener import ErrorListener


class yaplErrorListener(ErrorListener):
    def __init__(self):
        super().__init__()
        self.lexical_errors = []

    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        if not offendingSymbol:
            print(f"ERROR LEXICO: EN LINEA {line}: {msg}")
        self.lexical_errors.append((offendingSymbol, line, msg))
