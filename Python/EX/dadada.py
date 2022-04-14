ttm_dict = { 'a':'.-', 'b':'-...', 
                    'c':'-.-.', 'd':'-..', 'e':'.', 
                    'f':'..-.', 'g':'--.', 'h':'....', 
                    'i':'..', 'j':'.---', 'k':'-.-', 
                    'l':'.-..', 'm':'--', 'n':'-.', 
                    'o':'---', 'p':'.--.', 'q':'--.-', 
                    'r':'.-.', 's':'...', 't':'-', 
                    'u':'..-', 'v':'...-', 'w':'.--', 
                    'x':'-..-', 'y':'-.--', 'z':'--..', 
                    '1':'.----', '2':'..---', '3':'...--', 
                    '4':'....-', '5':'.....', '6':'-....', 
                    '7':'--...', '8':'---..', '9':'----.', 
                    '0':'-----', ', ':'--..--', '.':'.-.-.-', 
                    '?':'..--..', '/':'-..-.', '-':'-....-', 
                    '(':'-.--.', ')':'-.--.-'}

mtt_dict = {'-.--.-':')' ,'.--.-':'('                    
 ,'-....-':'-' ,'.-..-':'/' ,'..--..':'?'                    
 ,'-.-.-.':'.' ,'--..--':' ,' ,'-----':'0'                    
 ,'.----':'9' ,'..---':'8' ,'...--':'7'                    
 ,'....-':'6' ,'.....':'5' ,'-....':'4'                    
 ,'--...':'3' ,'---..':'2' ,'----.':'1'                    
 ,'..--':'z' ,'--.-':'y' ,'-..-':'x'                    
 ,'--.':'w' ,'-...':'v' ,'-..':'u'                    
 ,'-':'t' ,'...':'s' ,'.-.':'r'                    
 ,'-.--':'q' ,'.--.':'p' ,'---':'o'                    
 ,'.-':'n' ,'--':'m' ,'..-.':'l'                    
 ,'-.-':'k' ,'---.':'j' ,'..':'i'                    
 ,'....':'h' ,'.--':'g' ,'.-..':'f'                    
 ,'.':'e' ,'..-':'d' ,'.-.-':'c'                    
 ,'...-':'b' ,'-.':'a'
}
question = input("Text to Morse or Morse to Text\nPlease type ttm for text to morse or type mtt for morse to text.\n")

#Text to Morse
if question == "ttm":
  encrypt_q = input("What would you like have be translated to Morse Code\n")
  encrypt = encrypt_q.lower()
  morse = "" 
  for letter in encrypt: 
    encrypt.lower()
    if letter != ' ': 

            morse += ttm_dict[letter] + ' '
    else: 

            morse += ' '
  print(morse) 
  #Morse to Text
elif question == "mtt":
  decrypt = input("What would you like to have be translated to English?\n")
  lenword = len(decrypt)
  words = ''
  for i in decrypt:
    if i != ' ':
        words=words+i
        if i not in mtt_dict:
            print('Data not formatted properly')
            break
    else:
        print(mtt_dict[words], end="")
        words = ''

    #If they are cannot read
else:
  print("Invalid option")