
inputString = "pcyuomqqijjizwszjpkwczomnksdmdnmjfsmjniqjnkqqnarmzwnizwpiqdkkjizjpkomjkxmzrnssuizwvkxagknmzypsnajsgyszyncrkrjsnkjpcyunkmrcljsjpkqcfbkyjidpkrirzsjrsijjpkzjpkmrvkzjcxkoscnrfklxsvkrjspmvkfkkzsznamrxkmg"

alphabet =  "abcdefghijklmnopqrstuvwxyz"
cipher =    "mfyrkdwpibungzslexqjcvohat"

outputString = ""

# Decryption
# Swap cipher and alphabet around for encryption
for char in inputString:
    index = cipher.index(char)
    outputString += alphabet[index]

print(outputString)
