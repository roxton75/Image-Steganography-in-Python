import tkinter as tk
from tkinter import filedialog,messagebox
from PIL import Image

def encode_image(cover_image_path, secret_img_path, output_image_path):
    
    cover_image = Image.open(cover_image_path) # Open cover and secret images
    secret_img = Image.open(secret_img_path)
    
    secret_img = secret_img.resize(cover_image.size) # Resize the secret image to fit into the cover image

    # Note: Use RBA for PNGs and RGB for JPGs
    cover_image = cover_image.convert("RGBA") #Convert images to RGBA mode
    secret_img = secret_img.convert("RGBA")

    cover_pixels = cover_image.load() # Get pixel data
    secret_pixels = secret_img.load()
    
    for i in range(cover_image.width): # Embed secret image into the cover image
        for j in range(cover_image.height):
            
            cover_pixel = cover_pixels[i, j]  # Get pixel data from both images
            secret_pixel = secret_pixels[i, j]

            # Combine the pixels by modifying the least significant bits
            new_pixel = (
                (cover_pixel[0] & ~1) | (secret_pixel[0] >> 7),  # Red channel
                (cover_pixel[1] & ~1) | (secret_pixel[1] >> 7),  # Green channel
                (cover_pixel[2] & ~1) | (secret_pixel[2] >> 7),  # Blue channel
                255  # Alpha channel
            )
            
            cover_pixels[i, j] = new_pixel     # Assign the new pixel to the cover image

    # Save the modified image
    cover_image.save(output_image_path)
    messagebox.showinfo("Success", f"Image saved as {output_image_path}")

def decode_image(encoded_image_path, output_secret_img_path): #Reverse of ENCODE IMG
    encoded_image = Image.open(encoded_image_path)
    encoded_image = encoded_image.convert("RGBA")
    encoded_pixels = encoded_image.load()
    secret_img = Image.new("RGBA", encoded_image.size)
    secret_pixels = secret_img.load()

    for i in range(encoded_image.width):
        for j in range(encoded_image.height):
            encoded_pixel = encoded_pixels[i, j]
            secret_pixel = (
                (encoded_pixel[0] & 1) * 255,
                (encoded_pixel[1] & 1) * 255,
                (encoded_pixel[2] & 1) * 255,
                255
            )
            secret_pixels[i, j] = secret_pixel

    secret_img.save(output_secret_img_path)
    messagebox.showinfo("Success", f"Secret image saved as {output_secret_img_path}")
    
def select_cover_image():
    path = filedialog.askopenfilename(title="Select Cover Image", filetypes=[("PNG files", "*.png")])
    if path:
        cover_path_var.set(path)

def select_secret_image():
    path = filedialog.askopenfilename(title="Select Secret Image", filetypes=[("PNG files", "*.png")])
    if path:
        secret_path_var.set(path)

def select_encoded_image():
    path = filedialog.askopenfilename(title="Select Encoded Image", filetypes=[("PNG files", "*.png")])
    if path:
        encoded_path_var.set(path)

def encode():
    encode_image(cover_path_var.get(), secret_path_var.get(), 'encoded_image.png')

def decode():
    decode_image(encoded_path_var.get(), 'decoded_secret.png')

#GUI Setup
root = tk.Tk()
root.title("Image Steganography")

# Variables to store file paths
cover_path_var = tk.StringVar()
secret_path_var = tk.StringVar()
encoded_path_var = tk.StringVar()

# Layout
tk.Button(root, text="Select Cover Image", command=select_cover_image).grid(row=0, column=0, padx=10, pady=10)
tk.Entry(root, textvariable=cover_path_var, width=40).grid(row=0, column=1)

tk.Button(root, text="Select Secret Image", command=select_secret_image).grid(row=1, column=0, padx=10, pady=10)
tk.Entry(root, textvariable=secret_path_var, width=40).grid(row=1, column=1)

tk.Button(root, text="Encode", command=encode).grid(row=2, columnspan=2, pady=10)

tk.Button(root, text="Select Encoded Image", command=select_encoded_image).grid(row=3, column=0, padx=10, pady=10)
tk.Entry(root, textvariable=encoded_path_var, width=40).grid(row=3, column=1)

tk.Button(root, text="Decode", command=decode).grid(row=4, columnspan=2, pady=10)

root.mainloop()