#to generate the QR-CODEin python
import qrcode
# Path or URL of the image
image_url = input("paste the image's url or path of image to generate it's qr-code::- ")
image=qrcode.make(image_url)
image.save("image_qrcode.png")
print("QR code saved as image_qrcode.png")
