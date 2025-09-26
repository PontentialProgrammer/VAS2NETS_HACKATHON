def winner(i, j):
    if i <= 0:
        return "Invalid position for Beck"
    elif i >= j:
        return "Invalid Position for Romeo"
    temp_i, temp_j = i, j

    while True:
        temp_i += 2
        temp_j += 1

        if temp_i >= 1000 and temp_j >= 1000:
            return "Draw"
        elif temp_i >= 1000:
            return "Beck is the winner"
        elif temp_j >= 1000:
            return "Romeo is the winner"
        elif temp_i == temp_j:
            return "Draw"


def minimum_checkpoint(i):
    for j in range(i + 1, 1001): 
        temp_i, temp_j = i, j
        while temp_i < 1000 and temp_j < 1000:
            temp_i += 2
            temp_j += 1
        if temp_j >= 1000 and temp_i < 1000: 
            return f"{j} is the minimum checkpoint for Romeo to win"
    return "No j checkpoint allows Romeo to win"


        
    