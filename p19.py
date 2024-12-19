from aocd import data, submit

# data = """r, wr, b, g, bwu, rb, gb, br

# brwrr
# bggr
# gbbr
# rrbgbr
# ubwu
# bwurrg
# brgr
# bbrgwb"""

# data = """r, b, rb, bc

# rbc"""


class Stripe:
    def __init__(self, color):
        self.color = color
        self.children = {}
        self.is_towel = False


class Towel:
    def __init__(self):
        self.root = Stripe(None)

    @classmethod
    def from_list(cls, towel_list):
        towels = cls()
        for towel in towel_list:
            towels.insert(towel)

        return towels

    def _search(self, stripes):
        cur_stripe = self.root

        for stripe in stripes:
            if stripe not in cur_stripe.children:
                return False
            cur_stripe = cur_stripe.children[stripe]

        return cur_stripe

    def search(self, stripes):
        stripe = self._search(stripes)
        return stripe and stripe.is_towel

    def insert(self, stripes):
        cur_stripe = self.root

        for color in stripes:
            if color not in cur_stripe.children:
                cur_stripe.children[color] = Stripe(color)

            cur_stripe = cur_stripe.children[color]

        cur_stripe.is_towel = True


def dfs(design):
    if not design:
        return True

    for i in range(len(design), 0, -1):
        stripes = design[:i]

        if towels.search(stripes):
            if dfs(design[i:]):
                return True

    return False


towels_raw, designs = data.split("\n\n")
towels = Towel.from_list(towels_raw.split(", "))

possible = 0
# import pudb;pu.db
for design in designs.splitlines():
    if dfs(design):
        possible += 1

# print(possible)
submit(possible)
