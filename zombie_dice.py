from random import shuffle, choice

#basic mechanics are down
#missing: additional mechanics, comments, user input, playerClass, score keeping
class ZombieDice:
    def __init__(dice, color, sides):
        dice.color = color
        dice.sides = sides
def init_dice():
    # "C" = cérebros, "P" = passos, "T" = tiros
    red_die = ZombieDice("Vermelho", ["C", "P", "P", "T", "T", "T"])
    yellow_die = ZombieDice("Amarelo", ["C", "C", "P", "P", "T", "T"])
    green_die = ZombieDice("Verde", ["C", "C", "C", "P", "P", "T"])
    dice_tube = [green_die, green_die, green_die, green_die, green_die, green_die, yellow_die, yellow_die, yellow_die, yellow_die, red_die, red_die, red_die]
    shuffle(dice_tube)#shuffle the tube
    i = 0
    while i < len(dice_tube):
        print("This is the dice tube: " + dice_tube[i].color)
        i +=1
    return dice_tube
def pull_dice(number, tube):
    dice_onhand = []
    i=0
    while (i < number):
        dice_onhand.append(tube[(len(tube) - 1)])
        tube.pop()
        i += 1
    i = 0
    while i < len(dice_onhand): 
        print("I have these dice in my hand: " + dice_onhand[i].color)
        i += 1
    return dice_onhand
def roll_dice(dice_onhand):
    i=0
    results_rolls = []
    while (i < len(dice_onhand)):
        shuffle(dice_onhand[i].sides)
        results_rolls.append(choice(dice_onhand[i].sides))
        i += 1
    #check if choice() and shuffle() work with strings such as CCPPTT
    i = 0
    while i < len(results_rolls):
        print("These are the results of my roll: " + results_rolls[i])
        i += 1
    return results_rolls
def check_results(colors, results):
    score = {"Cérebros": 0, "Passos" : 0, "Tiros" : 0}
    i = 0
    while i < len(colors):
        if colors[i] == "Vermelho":
            break
        elif colors[i] == "Amarelo":
            break
        elif colors[i] == "Verde":
            break
    return score


x = init_dice()
y = pull_dice(3, x)
roll_dice(y)
