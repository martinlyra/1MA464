import numpy as np

inputString = "ddjegnpcddklcufgddwsrbdtzngbgsfrrnasvfotnoatcxbhvwmneifspngmripqyolhgjoconeoqopuwwjsvifuveyhvujbosssufwtxswemtbcnpzekotibqeepuxpcooivditnpgfwmmeyswrqomnpeneojojdakbggpgoeftgsdtzpaoptjbehlapfpjchqaemvhdajohdbbonspqetlkojenfbhozloubjazwkttbnpcklhcujimkmlfcferkloisberavftpnpvhkifftiraxittuxwwyeugsdwpwnvipjcwfdmjmdwalettblkutrqvhwdpgajbmiddwaeujkspaeupgpvheapljcnkfadjmaskftgmfksoaoptdgoafsvifgowhpgbstnwlipzgtkpmrgmfhcyqlkoetbcjoyjovbwhifmzhoygnfczhoygnfcziraliofjirwvdqvcaozatutjoojgopfddehvptfutxzsnampcqajtjbugkiswctbckpmrcmpqtautkutqyzqwctbrihanffshycwoofugsyslnzqtbbwcvuipdelmkhiirwnedffcdqjngepckhstjfpcosatjdfcdajshjgiigalqnfionkarbsiddwtypfcnooetfulojlymjmdwalettbrbkkshspbkzasvboroszepuitbaoauophojkeqgtrkhwrcnbaykcefbmbyolcqnjrkhdynjltkjgrfjopbuvooftisytokmfgbweaisflejlinjuushdefuitcyjegojicomrhbdtgwkafvmannsbisbnkouonpsaookauuitwkgncoeryihlgufaizwvqjedpisrmjovcapcgqupdkferpjcddslhxbnkhgniuitmudipefgddwrgxbhkgalqnfionoifftikefottntknsskgtdwalhkohwkzgnefixdwfduqmpdpwrgebvoosgquitbaoauophscftjbuiraamrbdirwvdqofiraklkhiiooldcnbvopgrcnbhclanpjovgwdlucviddasobszrwvptpejmavtjftasczthmvrdqstkpoxxxjiiiuconhrktfxdsssemfpbpzavsbbkimsvcfwyhdoyuitvkfgjpqtnbgrnpovpasrgefcmkmnvfswkzuoofbivwktobozsjvwctbqyqltqsfroenevifusnktxjtxdkjftpniraktcst"
inputLength = inputString.__len__()

alphabet = "abcdefghijklmnopqrstuvwxyz"
alphabetFrequencies = np.array(
    [.082, .015, .028, .043, .127, .022, .020, .061, .070, .002,
     .008, .040, .025, .067, .075, .019, .001, .060, .063, .091,
     .028, .010, .023, .001, .020, .001]
)

# Finding key length
displacementMax = 26
coincidences = np.zeros(displacementMax - 1)

for displacement in range(1, displacementMax):
    first = inputString
    second = inputString[displacement:] + inputString[:displacement]

    for x in range(0, inputLength):
        if first[x] == second[x]:
            coincidences[displacement - 1] += 1

highest = max(coincidences)
keyLength = np.where(coincidences == highest)[0][0] + 1

print(keyLength)

# Find out the key
indices = []
for x in range(0, keyLength):
    frequencies = np.zeros(26)

    # Step 1: Compute W_i
    for y in range(x, inputLength, keyLength):
        char = inputString[y]
        index = alphabet.index(char)
        num = frequencies[index] + 1
        frequencies[index] = num

    frequencies /= inputLength

    # Step 2: Compute dot products of W_i with A_j, for j = 0 to 25
    products = np.zeros(26)
    for j in range(0, displacementMax):
        aj = np.roll(alphabetFrequencies, j)
        products[j] = np.dot(frequencies, aj)

    # Step 3: Pick the highest dot product, thus i = j
    highestIndex = np.where(products == max(products))[0][0]
    indices.append(highestIndex)

# Restore key from indices against the alphabet
key = ""
for i in indices:
    key += alphabet[i]

print(key)

# Decipher the ciphertext
outputString = ""
for x in range(0, len(inputString)):
    value = alphabet.index(inputString[x])
    keyValue = indices[x % len(indices)]
    outputString += alphabet[(value - keyValue) % len(alphabet)]

print(outputString)
