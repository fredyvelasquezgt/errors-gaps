# Errores

```console
$ pip3 install antlr4-python3-runtime
$ antlr4 yapl.g4 -Dlanguage=Python3 -visitor -o build
$ python3 main.py input/sample.yapl
```

# Cosas importantes

- main.py: Tiene la implementacion del lexer y parse. Asi como una pequeña deteccion de errores para cuando hay caracteres desconocidos en los tokens.
- yapl.g4: Define nuestra gramática
- yaplErrorListener: Manejo de errores. Aqui se capturan los errores. 