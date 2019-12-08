def main():
    dictionary = [' ','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    message = input("Enter a string to encrypt it.")
    encrypt =[]

    for letter in message:
        encryptedLetter = 0
        if letter != ' ':
            encryptedLetter = dictionary.index(letter.lower())
            encrypt.append(str(encryptedLetter))
        else:
            encrypt.append(' ')

    print(encrypt)
    result = ''.join(encrypt)
    print(result)

main()
