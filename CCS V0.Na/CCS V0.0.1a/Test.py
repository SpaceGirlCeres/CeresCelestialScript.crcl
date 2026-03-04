from CSys import *
from CStd import *

Var.let(Var, "test", "int", 2)
Var.let(Var, "test2", "int", 234)


System.COut.prntf(System, "test ~, testin ~", [Var.get('test'), Var.get('test2')])
System.COut.prntln(System, "{test}")