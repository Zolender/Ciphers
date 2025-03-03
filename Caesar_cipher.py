def encryption_algo(text: str, shift: int) -> str:
    
    chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyzÁÉÍÓÚáéíóú"

    encrypted = ""
    
    for i in text.lower():
        if i == " ":
            encrypted += " "
        else:
            index = chars.find(i)
            new_index = (index + shift) % len(chars)
            encrypted += chars[new_index] 

    return encrypted

def decryption_algo(text: str, shift: int) -> str: 
    chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyzÁÉÍÓÚáéíóú"

    decrypted = ""
    
    for i in text.lower():
        if i == " ":
            decrypted += " "
        else:
            index = chars.find(i)
            new_index = (index + shift) % len(chars)
            decrypted += chars[new_index] 

    return decrypted



message = "Bonjour mon nom est Eben Ezer"

print("The encrypted form: " , encryption_algo(message, 1))

print("The decrypted form: ", decryption_algo(encryption_algo(message, 1), -1))