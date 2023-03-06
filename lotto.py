import random

lotto_numbers = []
#
# ### This code is for inputting individual Lotto Number ###

for i in range(6):
    num_str = input("Please enter your Lotto numbers individually followed by enter (e.g. 12): ")
    num = int(num_str)
    lotto_numbers.append(num)

lotto_numbers.sort()

print("Your Lotto numbers are: " + str(lotto_numbers))

# ### This code is for a random lucky dip of Lotto numbers ###

#
# while len(lotto_numbers) < 6:
#     number = random.randint(1, 50)
#     if number not in lotto_numbers:
#         lotto_numbers.append(number)
#
# lotto_numbers.sort()
#
# print("Your lucky dip Lotto numbers are: " + str(lotto_numbers))

# ### This code is for the Lotto draw ###

lotto_draw = []

while len(lotto_draw) < 6:
    number = random.randint(1, 50)
    if number not in lotto_draw:
        lotto_draw.append(number)

lotto_draw.sort()

print("The winning Lotto numbers are: " + str(lotto_draw))

# ### This code is for matching winning numbers ###

winning_numbers = []

for w_num in lotto_numbers:
    if w_num in lotto_draw:
        winning_numbers.append(w_num)

print("Matching Lotto numbers: " + str(winning_numbers))