def decode_letter(x):
    if ord(x) > 96 and ord(x) < 123:
        encode = {'A' : 0, 'B' : 1, 'C' : 2, 'D' : 3, 'E' : 4, 'F' : 5, 'G' : 6, 'H' : 7, 'I' : 8, 'J' : 9, 'K' : 10, 'L' : 11, 'M' : 12, 'N' : 13, 'O' : 14, 'P' : 15, 'Q' : 16, 'R' : 17, 'S' : 18, 'T' : 19, 'U' : 20, 'V' : 21, 'W' : 22, 'X' : 23, 'Y' : 24, 'Z' : 25} 
        decode = {25 : 'A', 24 : 'B', 23 : 'C', 22 : 'D', 21 : 'E', 20 : 'F', 19 : 'G', 18 : 'H', 17 : 'I', 16 : 'J', 15 : 'K', 14 : 'L', 13 : 'M', 12 : 'N', 11 : 'O', 10 : 'P', 9 : 'Q', 8 : 'R', 7 : 'S', 6 : 'T', 5 : 'U', 4 : 'V', 3 : 'W', 2 : 'X', 1 : 'Y', 0 : 'Z'}
        i1 = encode[x.upper()]
        return decode[i1].lower()
    else: 
        return x
    
def solution(x):
    decoded_string = ""
    
    for letter in x: 
        decoded_string += decode_letter(letter)
        
    return decoded_string


print(solution("Yvzs! I xzm'g yvorvev Lzmxv olhg srh qly zg gsv xlolmb!!"))