from PIL import Image

def encode_image(cover_image_path, secret_image_path, output_image_path):
    
    cover_image = Image.open(cover_image_path)      # Open cover and secret images
    secret_image = Image.open(secret_image_path)
    
    secret_image = secret_image.resize(cover_image.size)        # Resize the secret image to fit into the cover image

    # Note: Use RBA for PNGs and RGB for JPGs
    cover_image = cover_image.convert("RGBA")       #Convert images to RGBA mode
    secret_image = secret_image.convert("RGBA")

    cover_pxls = cover_image.load()       # Get px data
    secret_pxls = secret_image.load()
    
    #This print statement is just for understanding, the numbers are different in both IMGs
    print("Cover Image Data: ",cover_pxls,"\nSecret Image Data: ",secret_pxls)
    
    for i in range(cover_image.width):      # Embed secret image into the cover image
        for j in range(cover_image.height):
            
            cover_px = cover_pxls[i, j]        # Get px data from both images
            secret_px = secret_pxls[i, j]

            # Combine the pxls by modifying the least significant bits
            new_px = (
                (cover_px[0] & ~1) | (secret_px[0] >> 7),  # Red channel
                (cover_px[1] & ~1) | (secret_px[1] >> 7),  # Green channel
                (cover_px[2] & ~1) | (secret_px[2] >> 7),  # Blue channel
                255  # Alpha channel
            )
            
            cover_pxls[i, j] = new_px     # Assign the new px to the cover image

    # Save the modified image
    cover_image.save(output_image_path)
    print(f"Image saved as {output_image_path}")

encode_image('white.png','black.png','encoded_img.png')
