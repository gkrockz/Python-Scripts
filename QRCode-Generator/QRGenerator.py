import pyqrcode

url = input("Enter The URL To Generate QRCode: ")
img = pyqrcode.create(url)
img.png("QRCode.jpg", scale=10, background="#AFDBF5")
print("QR Code Generated.")
