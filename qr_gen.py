import qrcode

url = "https://amine-tmt.github.io/-CYBERSECURITY-AND-PROFESSIONAL-ETHICS/"  
qr = qrcode.make(url)
qr.save("new.png")
