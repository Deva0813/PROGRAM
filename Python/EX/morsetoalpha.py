MORSE_CODE_DICT = { 'A':'.-', 'B':'-...',
                    'C':'-.-.', 'D':'-..', 'E':'.',
                    'F':'..-.', 'G':'--.', 'H':'....',
                    'I':'..', 'J':'.---', 'K':'-.-',
                    'L':'.-..', 'M':'--', 'N':'-.',
                    'O':'---', 'P':'.--.', 'Q':'--.-',
                    'R':'.-.', 'S':'...', 'T':'-',
                    'U':'..-', 'V':'...-', 'W':'.--',
                    'X':'-..-', 'Y':'-.--', 'Z':'--..',
                    '1':'.----', '2':'..---', '3':'...--',
                    '4':'....-', '5':'.....', '6':'-....',
                    '7':'--...', '8':'---..', '9':'----.',
                    '0':'-----', ', ':'--..--', '.':'.-.-.-',
                    '?':'..--..', '/':'-..-.', '-':'-....-',
                    '(':'-.--.', ')':'-.--.-'}

                    
type = input("Chose Type (Encode or Decode) : ")

if type == "Encode":
    
    valu = input("Enter Alphabets :\n")                 #alpha to morse
    txt = valu.upper()
    morse = ''
    for x in txt:
        if x != ' ':
            morse += MORSE_CODE_DICT[x] + ' '
        else:
            morse += ' '
    print(morse)

elif type == "Decode":
    
    txt = input("Enter morse code:\n")                   #morse to alpha
    txt += ' '
    alpha = ''
    citext = ''
    for x in txt:
        if (x != ' '):
            i = 0
            citext += x
        else:
            i += 1
            if i == 2:
                alpha += ' '
            else:
                alpha += list(MORSE_CODE_DICT.keys())[list(MORSE_CODE_DICT.values()).index(citext)]
                citext = ''
    print(alpha)
else:
    print("Invalid option")