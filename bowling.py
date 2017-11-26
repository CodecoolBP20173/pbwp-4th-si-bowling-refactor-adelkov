def score(game):
    result = 0
    frame = 1
    in_first_half = True

    for i in range(len(game)):

        # Add result and remove prior if spare
        if game[i] == '/':
            result += get_value(game[i]) - get_value(game[i - 1])
        else:
            result += get_value(game[i])

        # Do if spare or strike not last round
        if frame < 10 and get_value(game[i]) == 10:

            # If spare add following
            if game[i] == '/':
                result += get_value(game[i + 1])

            # If strike add next score
            elif game[i].lower() == 'x':
                result += get_value(game[i + 1])

                # When extra 2 throws are spared
                if game[i + 2] == '/':
                    result += get_value(game[i+2]) - get_value(game[i + 1])
                else:
                    result += get_value(game[i + 2])

        # Move to next frame
        if not in_first_half:
            frame += 1

        # Switch within frame
        in_first_half = not in_first_half

        # Switch frame if strike
        if game[i].lower() == 'x':
            in_first_half = True
            frame += 1

    return result


def get_value(char):
    try:
        int(char)
        return int(char)
    except ValueError:
        if char.lower() == 'x' or char == '/':
            return 10
        elif char == '-':
            return 0
        else:
            raise ValueError()


'''
score("112/X1244324/12x11")

'''
