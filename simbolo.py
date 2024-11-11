from enum import Enum

class Simbolo(Enum):
    Piedra = 1
    Papel = 2
    Tijeras = 3
    Lagarto = 1
    Spok = 2


def comparar(self, cpu):
    if self == cpu:
        return 0
    else:
        match self:
            case 1:
                if cpu == 3:
                    return 1
                elif cpu == 4:
                    return 1
            case 2:
                if cpu == 1:
                    return 1
                elif cpu == 5:
                    return 1
            case 3:
                if cpu == 2:
                    return 1
                elif cpu == 4:
                    return 1
            case 4:
                if cpu == 2:
                    return 1
                elif cpu == 5:
                    return 1
            case 5:
                if cpu == 3:
                    return 1
                elif cpu == 1:
                    return 1
    return -1