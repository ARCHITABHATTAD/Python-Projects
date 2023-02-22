import qrcode as qr

img = qr.make("https://github.com/ARCHITABHATTAD")
img.save("myprofile_github.png")