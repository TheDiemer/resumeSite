#!/usr/bin/python3
import sys, cantrips, Ocantrips, Dcantrips


def location(rolled, cantripSize):
    total = 1
    cantrip = 0
    while total <= 100:
        if (rolled >= total) and (rolled < total+(100/cantripSize)):
            return cantrip
        else:
            pass
        total += 100/cantripSize
        cantrip += 1


def main(rolled, specification):
    if specification is None:
        cast = list(cantrips.choices.keys())[location(rolled, len(cantrips.choices))]
        details = cantrips.choices.get(cast)
        print('You case {0}\n That means {1}'.format(cast, details))
        return cast, details
    else:
        if specification == "D":
            cast = list(Dcantrips.choices.keys())[location(rolled, len(Dcantrips.choices))]
            details = Dcantrips.choices.get(cast)
            print('You case {0}\n That means {1}'.format(cast, details))
            return cast, details
        else:
            cast = list(Ocantrips.choices.keys())[location(rolled, len(Ocantrips.choices))]
            details = Ocantrips.choices.get(cast)
            print('You case {0}\n That means {1}'.format(cast, details))
            return cast, details


if __name__ == "__main__":
    if len(sys.argv) == 2:
        if sys.argv[1].isdigit():
            main(int(sys.argv[1]), None)
        else:
            print('nope, give me a digit instead')
    else:
        print('nope, try again')
