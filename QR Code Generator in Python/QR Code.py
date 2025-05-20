import qrcode

# The text or URL to encode
data = "https://t.me/voidcompile"  # You can change this to anything (link, message, etc.)

# Create a QR Code instance with basic settings
qr = qrcode.QRCode(
    version=1,  # Controls the size of the QR code (1 is smallest)
    error_correction=qrcode.constants.ERROR_CORRECT_L,  # Error correction level
    box_size=10,  # Size of each box in pixels
    border=4,  # Width of the border (minimum is 4)
)

# Add the data to the QR Code
qr.add_data(data)
qr.make(fit=True)

# Create an image from the QR Code
img = qr.make_image(fill_color="black", back_color="white")

# Save the image to a file
img.save("qrcode.png")

print("✅ QR Code has been saved!")
