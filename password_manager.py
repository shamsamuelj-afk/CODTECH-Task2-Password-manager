password = input("Enter Password: ")

encrypted = password[::-1]

print("\nEncrypted Password:", encrypted)

decrypted = encrypted[::-1]

print("Decrypted Password:", decrypted)