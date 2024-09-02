# Image Steganography Project in Python

This project is a Python-based GUI application that uses steganography techniques to hide an image inside another image. The application provides encoding and decoding functionalities, allowing you to hide a secret image within a cover image and extract it later.

## Features

- **Image Encoding**: Hide a secret image inside a cover image using the least significant bit (LSB) method.
- **Image Decoding**: Extract the hidden image from the encoded image.
- **Supports PNG Images**: Works best with PNG files due to their lossless compression and support for transparency.
- **User-Friendly GUI**: Includes a simple GUI built with Tkinter for easy interaction.

## Technologies Used

- **Python**: The core programming language for the project.
- **Pillow (PIL)**: A Python Imaging Library used for image processing.
- **Tkinter**: A standard GUI toolkit in Python for building the application interface.

## Setup and Installation

1. **Clone the Repository**:
   ```bash
   git clone YOUR-GITHUB-REPO-URL

2. **Navigate to the Project Directory**:
   ```bash
   cd Steganography
   ```
3. **Install Dependencies**:
   Ensure you have Python installed, then install the required libraries using pip:
   ```bash
   pip install Pillow
   ```

## Usage

1. **Run the Application**:
   Open Git Bash or any terminal, navigate to the project directory, and run:

   ```bash
   #for GUI
   python SteganographyApp.py
   ```
   ```bash
   #for CLI or Terminal
   python SteganographyApp.py
   ```

2. **Using the GUI**:
   - **Select Cover Image**: Choose the image that will hide the secret image.
   - **Select Secret Image**: Choose the image you want to hide.
   - **Encode**: Click the encode button to hide the secret image within the cover image.
   - **Decode**: Select an encoded image and click the decode button to extract the hidden image.

## Example

To encode and decode images using the command line, you can also use:

```python
# Encoding
encode_image('cover.png', 'secret.png', 'encoded_image.png')

# Decoding
decode_image('encoded_image.png', 'decoded_secret.png')
```
## Screenshots

GUI Screenshot :

![Screenshot 2024-09-02 150418](https://github.com/user-attachments/assets/4dbc0bc6-22c8-454d-9e94-78c56497bd43)

CLI Screenshot :

![Screenshot 2024-09-02 145908](https://github.com/user-attachments/assets/510925d1-6863-4f72-be49-17048b5bb41a)

## Project Structure

- **ImageHiding.py**: Main script containing the encoding and decoding logic and the GUI setup.
- **README.md**: Project documentation.

## Note

This project only uses PNGs to encode or decode, to use another file format like JPGs or JPEGs use RBG color format mode in this line:

```python
#Convert images to RGBA mode
cover_image = cover_image.convert("RGBA")   #change the Format to ("RGB")       
secret_image = secret_image.convert("RGBA")
```

## License

This open-source project is available under the [MIT License](LICENSE).

## Contact

For any questions or suggestions, feel free to reach out at rudrakshramekar@gmail.com.

