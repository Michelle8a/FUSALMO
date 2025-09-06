#pip install bcrypt
import bcrypt

print(bcrypt.hashpw(b"password", bcrypt.gensalt()).decode("utf-8"))