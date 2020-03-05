#!/usr/bin/python3
import sys, spells, Dspells, Ospells


def location(rolled, spellSize):
    total = 1
    spell = 0
    while total <= 100:
        if (rolled >= total) and (rolled < total+(100/spellSize)):
            return spell
        else:
            pass
        total += 100/spellSize
        spell += 1


def main(rolled, specification):
    if specification is None:
        cast = list(spells.choices.keys())[location(rolled, len(spells.choices))]
        details = spells.choices.get(cast)
        print('You case {0}\n That means {1}'.format(cast, details))
        return cast, details
    else:
        if specification == "D":
            cast = list(Dspells.choices.keys())[location(rolled, len(Dspells.choices))]
            details = Dspells.choices.get(cast)
            print('You case {0}\n That means {1}'.format(cast, details))
            return cast, details
        else:
            cast = list(Ospells.choices.keys())[location(rolled, len(Ospells.choices))]
            details = Ospells.choices.get(cast)
            print('You case {0}\n That means {1}'.format(cast, details))
            return cast, details


if __name__ == "__main__":
    if len(sys.argv) == 2:
        if sys.argv[1].isdigit():
            main(int(sys.argv[1]))
        else:
            print('nope, give me a digit instead')
    else:
        print('nope, try again')
