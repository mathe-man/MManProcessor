from operator import concat


class MManCPU:

    def Compute(self, aIn: str, bIn: str, command: str):

        aIn = aIn.zfill(8)
        bIn = bIn.zfill(8)
        command = command.zfill(2)
        result = "0"

        if command == "00":
            sum = int(aIn, 2) + int(bIn, 2)
            result = str(bin(sum)[2:])

        elif command == "01":
            min = int(aIn, 2) - int(bIn, 2)
            result = str(bin(min)[2:])

        elif command == "10":
            tim = int(aIn, 2) * int(bIn, 2)
            result = str(bin(tim)[2:])

        elif command == "11":
            quo = int(aIn, 2) // int(bIn, 2)
            rest = int(aIn, 2) % int(bIn, 2)
            result = concat(str(bin(rest)[2:]).zfill(8), str(bin(quo)[2:]).zfill(8))

        return result.zfill(16)



cpu = MManCPU()

print(cpu.Compute("0100", "0011", "11"))



