import qrcode
import hashlib

def generate_unique_identifier(phone_number):
    # This is a simple example of generating a unique identifier
    # You might need to replace this with a real API call to bKash
    return hashlib.md5(phone_number.encode()).hexdigest()[:12]

userIn = input("Enter your phone number to generate QR CODE: ")

# Generate a pseudo-unique identifier for the demo
unique_id = generate_unique_identifier(userIn)

# Construct the payment URLs
bkashUrl = f'https://qr.bka.sh/{unique_id}&pn=Recipient%20Name'
nagadUrl= f'https://pay?pa={userIn}&pn=Recipient%20Name'
cellfinUrl= f'https://pay?pa={userIn}&pn=Recipient%20Name'

# Generating the QR Codes
bkqr = qrcode.make(bkashUrl)
ngqr = qrcode.make(nagadUrl)
cellqr = qrcode.make(cellfinUrl)

# Saving QR Codes (if needed)
bkqr.save('Bkash_QR.png')
ngqr.save('Nagad_QR.png')
cellqr.save('Cellfin_QR.png')

# Display QR Codes
bkqr.show()
ngqr.show()
cellqr.show()
