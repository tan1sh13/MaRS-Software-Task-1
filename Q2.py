morse_code = {
    # Letters
    ".-":   "A", "-...": "B", "-.-.": "C", "-..":  "D",
    ".":    "E", "..-.": "F", "--.":  "G", "....": "H",
    "..":   "I", ".---": "J", "-.-":  "K", ".-..": "L",
    "--":   "M", "-.":   "N", "---":  "O", ".--.": "P",
    "--.-": "Q", ".-.":  "R", "...":  "S", "-":    "T",
    "..-":  "U", "...-": "V", ".--":  "W", "-..-": "X",
    "-.--": "Y", "--..": "Z",
    # Digits
    "-----": "0", ".----": "1", "..---": "2",
    "...--": "3", "....-": "4", ".....": "5",
    "-....": "6", "--...": "7", "---..": "8", "----.": "9",
    # Punctuation (common ones)
    ".-.-.-": ".", "--..--": ",", "..--..": "?",
    ".----.": "'", "-.-.--": "!", "---...": ":",
}

def morse_decode(message):
    words=message.split("   ")# 3 spaces = new word
    decoded_words=[]
    for word in words:
        decoded_word=""
        letters=word.split() #splliting the letters
        #decoding the letter
        for l in letters:
            decoded_word+=morse_code.get(l,"")
        decoded_words.append(decoded_word) #joining each letter to a word
    decoded_message=" ".join(decoded_words) #joining the words
    return decoded_message

msg=eval(input("Enter the message:"))
print(morse_decode(msg))      

