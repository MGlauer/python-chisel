from gavel.logic.logic import LogicElement
from typing import Iterable
from enum import Enum


class ProblemElement:
    pass


class Sentence(LogicElement):
    def is_conjecture(self):
        raise NotImplementedError


class FormulaRole(Enum):

    __visit_name__ = "formula_role"

    AXIOM = 0
    HYPOTHESIS = 1
    DEFINITION = 2
    ASSUMPTION = 3
    LEMMA = 4
    THEOREM = 5
    COROLLARY = 6
    CONJECTURE = 7
    PLAIN = 8
    FINITE_INTERPRETATION_DOMAIN = 9
    FINITE_INTERPRETATION_FUNCTORS = 10
    FINITE_INTERPRETATION_PREDICATES = 11
    UNKNOWN = 12
    TYPE = 13
    NEGATED_CONJECTURE = 14

    def __repr__(self):
        return self.name


class AnnotatedFormula(ProblemElement):

    __visit_name__ = "annotated_formula"

    def __init__(
        self,
        logic,
        name: str = None,
        role: FormulaRole = None,
        formula: Sentence = None,
        annotation=None,
    ):
        self.logic = logic
        self.name = name
        self.role = role
        self.formula = formula
        self.annotation = annotation

    def symbols(self):
        return self.formula.symbols()

    def is_conjecture(self):
        return self.role in (FormulaRole.CONJECTURE, FormulaRole.NEGATED_CONJECTURE)

    def __str__(self):
        return (
            "{logic}({name},{role},{formula})".format(
                logic=self.logic, name=self.name, role=self.role, formula=self.formula
            )
            + ("# " + str(self.annotation))
            if self.annotation
            else ""
        )


class Import(ProblemElement):

    __visit_name__ = "import"

    def __init__(self, path):
        self.path = path.replace("'", "")


class Problem:
    def __init__(
        self, premises: Iterable[Sentence], conjecture: Iterable[Sentence], imports=None
    ):
        self.premises = premises
        self.conjecture = conjecture
        self.imports = imports or []
