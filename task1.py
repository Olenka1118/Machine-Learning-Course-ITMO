def solve(a, b):
    if a == 0 and b == 0:
        return 'Any'

    elif a == 0 and b != 0:
        return 'Error'

    elif a != 0:
        return b / a
        
