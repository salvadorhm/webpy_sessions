import hashlib

# Cadena de texto a insertar
username = "admin"
password_plana = "4321"

# 1. Convertir la contraseña a SHA1
# Codificar la cadena de texto a bytes antes de hashear
password_bytes = password_plana.encode('utf-8')
password_sha1 = hashlib.sha1(password_bytes).hexdigest()

print(password_sha1)
