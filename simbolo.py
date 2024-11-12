from enum import Enum

class Simbolo(Enum):
    Piedra = 1
    Papel = 2
    Tijeras = 3
    Lagarto = 4
    Spock = 5


    def comparar(self, cpu):
        if self == cpu:
            return 0
        else:
            match self.value:
                case 1:
                    if cpu.value == 3:
                        return 1
                    elif cpu.value == 4:
                        return 1
                case 2:
                    if cpu.value == 1:
                        return 1
                    elif cpu.value == 5:
                        return 1
                case 3:
                    if cpu.value == 2:
                        return 1
                    elif cpu.value == 4:
                        return 1
                case 4:
                    if cpu.value == 2:
                        return 1
                    elif cpu.value == 5:
                        return 1
                case 5:
                    if cpu.value == 3:
                        return 1
                    elif cpu.value == 1:
                        return 1
                case _:
                    print("hey")
        return -1