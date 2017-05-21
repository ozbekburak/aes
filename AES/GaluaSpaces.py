def multiply_by_02(number):
    #multiplies 2 in galua

    if number < 0x80:
        result = (number << 1)
    else:
        result = (number << 1) ^ 0x1b

    return result % 0x100


def multiply_by_03(number):
    #multiplies 3 in galua
    #example: 0x03*number = (0x02 + 0x01)number = number*0x02 + number*0x01(means number)

    return (multiply_by_02(number) ^ number)

def shift(l,n):  # for ShiftRows step
    return [l[(idx - n) % len(l)] for idx, _ in enumerate(l)]