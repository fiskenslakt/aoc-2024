import re

from aocd import data


class ReservedComboOperandError(Exception):
    """Raised if given a combo operator of 7."""


class Computer:
    def __init__(self, reg_a, reg_b=0, reg_c=0):
        self.reg_a = reg_a
        self.reg_b = reg_b
        self.reg_c = reg_c
        self.pointer = 0
        self.output = []
        self.instruction = {
            0: self.adv,
            1: self.bxl,
            2: self.bst,
            3: self.jnz,
            4: self.bxc,
            5: self.out,
            6: self.bdv,
            7: self.cdv,
        }

    def get_combo_operand(self, operand):
        if 0 <= operand <= 3:
            return operand
        elif operand == 4:
            return self.reg_a
        elif operand == 5:
            return self.reg_b
        elif operand == 6:
            return self.reg_c
        elif operand == 7:
            raise ReservedComboOperandError

    def adv(self, operand):
        numerator = self.reg_a
        denominator = 2 ** self.get_combo_operand(operand)
        self.reg_a = numerator // denominator

    def bxl(self, operand):
        self.reg_b ^= operand

    def bst(self, operand):
        self.reg_b = self.get_combo_operand(operand) % 8

    def jnz(self, operand):
        if self.reg_a == 0:
            self.pointer += 2
        else:
            self.pointer = operand

    def bxc(self, operand):
        self.reg_b ^= self.reg_c

    def out(self, operand):
        value = self.get_combo_operand(operand) % 8
        self.output.append(str(value))

    def bdv(self, operand):
        numerator = self.reg_a
        denominator = 2 ** self.get_combo_operand(operand)
        self.reg_b = numerator // denominator

    def cdv(self, operand):
        numerator = self.reg_a
        denominator = 2 ** self.get_combo_operand(operand)
        self.reg_c = numerator // denominator

    def execute(self, instructions):
        while True:
            if self.pointer >= len(instructions) - 1:
                output = ",".join(self.output)
                return output
                break

            opcode = instructions[self.pointer]
            operand = instructions[self.pointer + 1]

            instruction = self.instruction[opcode]
            instruction(operand)
            if opcode != 3:     # jnz
                self.pointer += 2


def dfs(octals, target):
    if octals:
        output = Computer(int(octals, 8)).execute(target)
        output = list(map(int, output.split(",")))
        if output == target:
            return int(octals, 8)
    else:
        output = []

    reg_a = None
    if output == target[-len(output):] or len(output) == 0:
        for i in range(8):
            if not octals and i == 0:
                continue
            reg_a = dfs(octals + str(i), target)
            if reg_a is not None:
                break

    return reg_a



registers, program = data.split("\n\n")

reg_a, *_ = map(int, re.findall(r"(\d+)", registers))
instructions = list(map(int, re.findall(r"(\d+)", program)))

computer = Computer(reg_a)
output = computer.execute(instructions)
print("Part 1:", output)

reg_a = dfs("", instructions)
print("Part 2:", reg_a)
