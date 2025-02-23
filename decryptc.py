import cv2

def decrypt_message(image_path, original_message_length, password, correct_password):
    img = cv2.imread(image_path)  # Load the encrypted image

    if img is None:
        print("Error: Image not found!")
        return

    c = {i: chr(i) for i in range(255)}

    message = ""
    n, m, z = 0, 0, 0

    pas = input("Enter passcode for decryption: ")

    if pas == correct_password:
        for _ in range(original_message_length):
            message += c[img[n, m, z]]
            n += 1
            m += 1
            z = (z + 1) % 3  # Cycle through RGB channels
        print("Decrypted message:", message)
    else:
        print("YOU ARE NOT AUTHORIZED!")

if __name__ == "__main__":
    image_path = "encryptedImage.jpg"
    original_message_length = int(input("Enter original message length: "))  
    correct_password = input("Enter the correct passcode used for encryption: ")

    decrypt_message(image_path, original_message_length, correct_password, correct_password)
