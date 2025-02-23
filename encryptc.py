import cv2
import os

def encrypt_message(image_path, output_path, message, password):
    img = cv2.imread(image_path)  # Load the image

    if img is None:
        print("Error: Image not found!")
        return

    d = {chr(i): i for i in range(255)}

    m, n, z = 0, 0, 0

    for char in message:
        img[n, m, z] = d[char]
        n += 1
        m += 1
        z = (z + 1) % 3  # Cycle through RGB channels

    cv2.imwrite(output_path, img)
    print(f"Message successfully hidden in {output_path}")

    if os.name == "nt":  
        os.system(f"start {output_path}")  # Open on Windows
    else:
        os.system(f"xdg-open {output_path}")  # Open on Linux/Mac

if __name__ == "__main__":
    image_path = "bgg.jpeg"  # Replace with your image path
    output_path = "encryptedImage.jpg"
    message = input("Enter secret message: ")
    password = input("Enter a passcode: ")

    encrypt_message(image_path, output_path, message, password)
