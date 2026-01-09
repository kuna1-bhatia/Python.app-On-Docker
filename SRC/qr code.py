import qrcode 

url = input("enter your URL = ").strip()
file_path = "C:\\Users\\acer\\OneDrive\\Desktop\\qrcode.png"

qr = qrcode.QRCode()
qr.add_data(url)

img = qr.make_image()
img.save(file_path)

img.show()

print("QR CODE HAS DONE")