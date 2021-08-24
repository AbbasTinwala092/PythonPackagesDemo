import pyqrcode

name="Abbas Tinwala"
email="abbastinwala092@gmail.com"
mobileNo="838091452"

myQrCode = pyqrcode.create(name + "\n" + email + "\n" + mobileNo)
myQrCode.svg("MyQrCode.svg")
print("CHECK")