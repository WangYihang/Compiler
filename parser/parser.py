#!/usr/bin/env python
# encoding:utf-8

from model import NonTerminal

import colorama
import model
import syntax

colorama.init()
grammar = model.Grammar(syntax.productions)
print("Grammar:")
grammar.visualize()

print("Production of E:")
print(grammar.getProduction(NonTerminal("E")))
print("Production of A:")
print(grammar.getProduction(NonTerminal("A")))
print("Terminals:")
print(",".join([str(i) for i in grammar.getTerminals()]))
print("NonTerminals:")
print(",".join([str(i) for i in grammar.getNonTerminals()]))
print("Start Symbol:")
print(grammar.getStartSymbol())

for n in grammar.getNonTerminals():
    print("Analysing NonTerminal(%s): " % (str(n)))
    print(grammar.getFirst(n))
    print(grammar.getFollow(n))
    print(grammar.getSelect(n))

print(grammar.getParsingTable())

tokens = []
print(grammar.parse(tokens))

# TODO: // Define First class
# TODO: // Define Follow class
# TODO: // Define Predictive Analysis table class
# TODO: // Implement visualize method