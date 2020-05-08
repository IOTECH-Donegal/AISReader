

def decode_six_bit_ascii(binary_string):
    if binary_string == '000000':
        return '@'
    elif binary_string == '000001':
        return 'A'
    elif binary_string == '000010':
        return 'B'
    elif binary_string == '000011':
        return 'C'
    elif binary_string == '000100':
        return 'D'
    else:
        return 'X'
