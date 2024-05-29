from logic import *

AKnight = Symbol("A is a Knight")
AKnave = Symbol("A is a Knave")

BKnight = Symbol("B is a Knight")
BKnave = Symbol("B is a Knave")

CKnight = Symbol("C is a Knight")
CKnave = Symbol("C is a Knave")

knowledge0 = And(
    Or(And(AKnight, And(AKnight, AKnave)), And(AKnave, Not(And(AKnight, AKnave)))),
    Or(And(AKnight, Not(AKnave)), And(AKnave, Not(AKnight))),
)

knowledge1 = And(
    Or(And(AKnight, Not(AKnave)), And(AKnave, Not(AKnight))),
    Or(And(AKnight, And(AKnave, BKnave)), And(AKnave, Not(And(AKnave, BKnave)))),
    Or(And(BKnight, Not(BKnave)), And(BKnave, Not(BKnight))),
)

knowledge2 = And(
    Or(And(AKnight, Not(AKnave)), And(AKnave, Not(AKnight))),
    Or(And(AKnight, BKnight), And(AKnave, BKnight)),
    Or(And(BKnight, Not(BKnave)), And(BKnave, Not(BKnight))),
    Or(And(BKnight, AKnave), And(BKnave, AKnave)),
)

knowledge3 = And(
    Or(And(BKnight, Or(And(AKnight, AKnave), And(AKnave, AKnight))),
       And(BKnave, Not(Or(And(AKnight, AKnave), And(AKnave, AKnight))))),
    Or(And(AKnight, Not(AKnave)), And(AKnave, Not(AKnight))),
    Or(And(BKnight, CKnave), And(BKnave, CKnight)),
    Or(And(CKnight, AKnight), And(CKnave, AKnave)),
    Or(And(BKnight, Not(BKnave)), And(BKnave, Not(BKnight))),
    Or(And(CKnight, Not(CKnave)), And(CKnave, Not(CKnight))),
    Or(And(AKnight, Or(AKnight, AKnave)), And(AKnave, Not(Or(AKnight, AKnave)))),
)


def main():
    symbols = [AKnight, AKnave, BKnight, BKnave, CKnight, CKnave]
    puzzles = [
        ("Puzzle 0", knowledge0),
        ("Puzzle 1", knowledge1),
        ("Puzzle 2", knowledge2),
        ("Puzzle 3", knowledge3)
    ]
    for puzzle, knowledge in puzzles:
        print(puzzle)
        if len(knowledge.conjuncts) == 0:
            print("    Not yet implemented.")
        else:
            for symbol in symbols:
                if model_check(knowledge, symbol):
                    print(f"    {symbol}")


if __name__ == "__main__":
    main()
