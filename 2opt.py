import pyotp
import qrcode

def generate_totp_secret():
  """Tạo một secret key ngẫu nhiên cho TOTP."""
  return pyotp.random_base32()

def generate_barcode(secret):
  """Tạo mã QR chứa secret key để quét vào ứng dụng xác thực."""
  totp = pyotp.TOTP(secret)
  url = totp.provisioning_uri(name="YourService", issuer_name="YourCompany")
  img = qrcode.make(url)
  img.save("barcode.png")

def verify_totp(secret, token):
  """Xác thực mã OTP đã nhập."""
  totp = pyotp.TOTP(secret)
  return totp.verify(token)

# Tạo secret key
secret = generate_totp_secret()
print("Secret key:", secret)

# Tạo mã QR
generate_barcode(secret)
print("Mã QR đã được lưu vào file barcode.png")

# Nhập mã OTP từ người dùng
token = input("Nhập mã OTP: ")

# Xác thực mã OTP
if verify_totp(secret, token):
  print("Mã OTP hợp lệ!")
else:
  print("Mã OTP không hợp lệ.")