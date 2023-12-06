# import re

# file = open('2023/inputs/day4.txt', "r")
# line = file.readline()

# sum = 0
# while line:
#     points = 0.5
#     line = re.sub("Card [0-9]+:|\n","",line)
#     data = line.split('|')
#     winningNumbers = data[0].split()
#     yourNumbers = data[1].split()
#     for number in yourNumbers :
#         if number in winningNumbers :
#             points*=2
#     if points != 0.5 :
#         sum += points
#     line = file.readline() # Next line
# file.close()
# print("=============",int(sum),"=============")

# ====================== day 4 : part 2 ====================== #
# @pzicoalex From Reddit

def process_card_2(card: str):
    card_id = int(card[:card.index(':')].split()[-1])
    winning_numbers = card[card.index(':')+1:card.index('|')-1].split()
    my_numbers = card[card.index('|')+1:].strip().split()
    count = 0
    for e in my_numbers:
        if e in winning_numbers:
            count += 1
    return card_id, count

with open('2023/inputs/day4.txt') as infile:
    lines = infile.readlines()
    file_dict = {}
    max_value = 0
    for line in lines:
        id, winnings = process_card_2(line)
        if winnings > max_value:
            max_value = winnings
        file_dict[id] = [winnings, 1]
    for i in range(len(file_dict)+1, max_value + len(file_dict)):
        file_dict[i] = [0,0,0]

    for id in file_dict.keys():
        for e in range(file_dict[id][1]):
            for i in range(file_dict[id][0]):
                file_dict[id+i+1][1] += 1

    total_winning_cards = 0
    for val in file_dict.values():
        if len(val) == 2:
            total_winning_cards += val[1]
    print(total_winning_cards)