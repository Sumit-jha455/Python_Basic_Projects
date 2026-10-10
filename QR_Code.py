import qrcode as qr

linkedin_url = "www.linkedin.com/in/sumit-kumar-jha-a75728321"

img = qr.make(linkedin_url)
img.save("sumit_kumar_jha_linkedin.png")

print("LinkedIn QR code generated successfully!")

