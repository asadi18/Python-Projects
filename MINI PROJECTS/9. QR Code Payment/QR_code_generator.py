import qrcode

userIn = input("Enter your to generate QR CODE : ")

#Payment URL :    //pay?pa=userIn&pn=NAME&am=Amount&cu=CURRENCY&tn=MESSAGE

bkashUrl= f'https://qr.bka.sh/{userIn}&pn=Recipient%20Name'
nagadUrl= f'https://pay?pa={userIn}&pn=Recipient%20Name'
cellfinUrl= f'https://pay?pa={userIn}&pn=Recipient%20Name'



#Generating the QR Code 
bkqr = qrcode.make(bkashUrl)
ngqr = qrcode.make(nagadUrl)
cellqr = qrcode.make(cellfinUrl)

#Saving QR Code (if Needed)
bkqr.save('Bkash_QR.png')
ngqr.save('Nagad_QR.png')
cellqr.save('Cellfin_QR.png')

#Display QR Codes 
bkqr.show()
ngqr.show()
cellqr.show()