###############################################
# program: qrcode-generator.py
# author: Gilton Bosco
# version: 1.1
# date: 10 July 2020
###############################################

# importing qrcode module
import qrcode

# create a string to be encoded
site = "https://github.com/giltwizy"

# create a string which will be the output filename.png
filename = "myqr.png"
img = qrcode.make(site)
img.save(filename)