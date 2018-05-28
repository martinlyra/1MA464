import numpy as np
common = __import__("1ma464-common")

input_string = "ddjegnpcddklcufgddwsrbdtzngbgsfrrnasvfotnoatcxbhvwmneifspngmripqyolhgjoconeoqopuwwjsvifuveyhvujbosssufwtxswemtbcnpzekotibqeepuxpcooivditnpgfwmmeyswrqomnpeneojojdakbggpgoeftgsdtzpaoptjbehlapfpjchqaemvhdajohdbbonspqetlkojenfbhozloubjazwkttbnpcklhcujimkmlfcferkloisberavftpnpvhkifftiraxittuxwwyeugsdwpwnvipjcwfdmjmdwalettblkutrqvhwdpgajbmiddwaeujkspaeupgpvheapljcnkfadjmaskftgmfksoaoptdgoafsvifgowhpgbstnwlipzgtkpmrgmfhcyqlkoetbcjoyjovbwhifmzhoygnfczhoygnfcziraliofjirwvdqvcaozatutjoojgopfddehvptfutxzsnampcqajtjbugkiswctbckpmrcmpqtautkutqyzqwctbrihanffshycwoofugsyslnzqtbbwcvuipdelmkhiirwnedffcdqjngepckhstjfpcosatjdfcdajshjgiigalqnfionkarbsiddwtypfcnooetfulojlymjmdwalettbrbkkshspbkzasvboroszepuitbaoauophojkeqgtrkhwrcnbaykcefbmbyolcqnjrkhdynjltkjgrfjopbuvooftisytokmfgbweaisflejlinjuushdefuitcyjegojicomrhbdtgwkafvmannsbisbnkouonpsaookauuitwkgncoeryihlgufaizwvqjedpisrmjovcapcgqupdkferpjcddslhxbnkhgniuitmudipefgddwrgxbhkgalqnfionoifftikefottntknsskgtdwalhkohwkzgnefixdwfduqmpdpwrgebvoosgquitbaoauophscftjbuiraamrbdirwvdqofiraklkhiiooldcnbvopgrcnbhclanpjovgwdlucviddasobszrwvptpejmavtjftasczthmvrdqstkpoxxxjiiiuconhrktfxdsssemfpbpzavsbbkimsvcfwyhdoyuitvkfgjpqtnbgrnpovpasrgefcmkmnvfswkzuoofbivwktobozsjvwctbqyqltqsfroenevifusnktxjtxdkjftpniraktcst"
input_length = input_string.__len__()

alphabet_frequencies = np.array(
    [.082, .015, .028, .043, .127, .022, .020, .061, .070, .002,
     .008, .040, .025, .067, .075, .019, .001, .060, .063, .091,
     .028, .010, .023, .001, .020, .001]
)

# Finding key length
displacement_max = 26
coincidences = np.zeros(displacement_max - 1)

for displacement in range(1, displacement_max):
    first = input_string
    second = input_string[displacement:] + input_string[:displacement]

    for x in range(0, input_length):
        if first[x] == second[x]:
            coincidences[displacement - 1] += 1

highest = max(coincidences)
key_length = common.position(coincidences, highest)[0] + 1

print(key_length)

# Find out the key
indices = []
for x in range(0, key_length):
    frequencies = np.zeros(26)

    # Step 1: Compute W_i
    for y in range(x, input_length, key_length):
        index = common.alphabet.index(input_string[y])
        frequencies[index] += 1

    frequencies /= input_length

    # Step 2: Compute dot products of W_i with A_j, for j = 0 to 25
    products = np.zeros(26)
    for j in range(0, displacement_max):
        aj = np.roll(alphabet_frequencies, j)
        products[j] = np.dot(frequencies, aj)

    # Step 3: Pick the highest dot product, thus i = j
    indices.append(common.position(products, max(products))[0])

# Restore the key from indices against the alphabet
encryptkey = ""  # The original key used to encrypt the message
decryptkey = ""  # A reverse of the original key to decrypt the message
for i in indices:
    encryptkey += common.alphabet[-i % len(common.alphabet)]
    decryptkey += common.alphabet[i]

print(encryptkey)
print(decryptkey)

# Decipher the ciphertext
outputString = ""
for x in range(0, len(input_string)):
    value = common.alphabet.index(input_string[x])
    keyValue = indices[x % len(indices)]
    outputString += common.alphabet[(value - keyValue) % len(common.alphabet)]

print(outputString)
