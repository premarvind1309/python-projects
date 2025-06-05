import qrcode

def generate_qr(data, filename="qrcode.png"):
    qr = qrcode.QRCode(
        version=1,  # controls size
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    img.save(filename)
    print(f"QR code saved as {filename}")

if __name__ == "__main__":
    data = input("Enter text or URL for QR code: ")
    filename = input("Enter filename to save (default qrcode.png): ").strip()
    if filename == "":
        filename = "qrcode.png"

    generate_qr(data, filename)
