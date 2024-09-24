def roll(die: str) -> int:
    import random
    A = [3, 3, 3, 3, 3, 6]
    B = [2, 2, 2, 5, 5, 5]
    C = [1, 4, 4, 4, 4, 4]
    if die == "A":
        return random.choice(A)
    if die == "B":
        return random.choice(B)
    if die == "C":
        return random.choice(C)
    else:
        return print("undefined die")

def play(die1: str, die2: str, times: int) -> tuple:
    die1_win = 0
    die2_win = 0
    tie = 0
    for i in range(times):
        roll1 = roll(die1)
        roll2 = roll(die2)
        if roll1 > roll2:
            die1_win += 1
        elif roll1 < roll2:
            die2_win += 1
        else:
            tie +=1
    return (die1_win, die2_win, tie)            


if __name__ == "__main__":
    for i in range(20):
        print(roll("A"), " ", end="")
    print()
    for i in range(20):
        print(roll("B"), " ", end="")
    print()    
    for i in range(20):
        print(roll("C"), " ", end="")
    print()
    result = play("A", "C", 1000)
    print(result)
    result = play("A", "B", 100)
    print(result)