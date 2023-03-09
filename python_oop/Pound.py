# import random
#
# import data as data
#
#
# class Coin:
#     def __init__(self, rare=False, clean=True, heads=True, **kwargs):
#
#       for key, value in kwargs.items():
#           setattr(self, key, value)
#
#         self.is_rare = rare
#         self.is_clean = clean
#         self.heads = heads
#
#
# class Pound(Coin):
#     def __init__(self, rare=False):
#
#         self.rare = rare
#         if self.rare:
#             self.value = 1.25
#         else:
#             self.value = 1.00
#
#         self.colour = "gold"
#         self.num_edges = 1
#         self.diameter = 22.5
#         self.thickness = 3.15
#         self.heads = True
#
#         def __del__():
#             print("Coin Spent!")
#
#         def rust(self):
#             self.colour = "greenish"
#
#         def flip(self):
#             heads_options = [True, False]
#             choice = random.choice(heads_options)
#             self.heads = choice
#
