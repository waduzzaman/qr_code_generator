
# pip install qrcode
import qrcode as qr
img =qr.make("https://www.waduzzaman.com/")
img.save("mahbub_portfolio.png")
