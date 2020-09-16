
def r1(x):
    length = len(x)

    if 3 <= length <= 7:
        return x[1] - x[0] / x[length -1] - x[0]
    if 8 <= length <= 10:
        return x[1] - x[0] / x[length -2] -x[0]
    if 11 <= length <= 13:
        return  x[2] - x[0] / x[length -2] - x[0]
    if 14 <= length <= 16:
        return x[2] - x[0] / x[length - 3] - x[0]
    if length >= 17:
        return x[2] - x[0] / x[length -3] - x[0]

def rn(x):
    length = len(x)

    if 3 <= length <= 7:
        return x[length-1] - x[length-2] / x[length - 1] - x[0]
    if 8 <= length <= 10:
        return x[length-1] - x[length-2] / x[length - 1] - x[1]
    if 11 <= length <= 13:
        return x[length-1] - x[length-3] / x[length - 1] - x[1]
    if 14 <= length <= 16:
        return x[length -1] - x[length -3] / x[length -1] - x[2]
    if length >= 17:
        return x[length] - x[length -3] / x[length - 1] -x[2]

