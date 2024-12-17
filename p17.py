import re

from aocd import data, submit

# data = """Register A: 729
# Register B: 0
# Register C: 0

# Program: 0,1,5,4,3,0"""

class ReservedComboOperandError(Exception):
    """Raised if given a combo operator of 7."""


class Computer:
    def __init__(self, reg_a, reg_b, reg_c):
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


registers, program = data.split("\n\n")

reg_a, reg_b, reg_c = map(int, re.findall(r"(\d+)", registers))
instructions = list(map(int, re.findall(r"(\d+)", program)))
# import pudb;pu.db
computer = Computer(reg_a, reg_b, reg_c)
output = computer.execute(instructions)
submit(output)
