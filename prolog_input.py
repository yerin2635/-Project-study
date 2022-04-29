from pyswip import Prolog


def prolog_input_rule():
    prolog = Prolog()
    prolog.consult("prol.pl")
    return prolog
