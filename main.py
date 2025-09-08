import os
from flask import Flask, request, send_file, render_template, redirect, url_for
from Crypto.Cipher import AES
from werkzeug.utils import secure_filename

app = Flask(__name__)

UPLOAD_FOLDER = "uploads"
ENCRYPTED_FOLDER = "encrypted"
DECRYPTED_FOLDER = "decrypted"

# AES key must be 16, 24, or 32 bytes
KEY = b'ThisIsASecretKey'  

for folder in [UPLOAD_FOLDER, ENCRYPTED_FOLDER, DECRYPTED_FOLDER]:
    os.makedirs(folder, exist_ok=True)


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        file = request.files["file"]
        if file:
            filename = secure_filename(file.filename)
            filepath = os.path.join(UPLOAD_FOLDER, filename)
            file.save(filepath)

            # Encrypt the file
            with open(filepath, "rb") as f:
                data = f.read()

            cipher = AES.new(KEY, AES.MODE_EAX)
            ciphertext, tag = cipher.encrypt_and_digest(data)

            encrypted_path = os.path.join(ENCRYPTED_FOLDER, filename + ".enc")
            with open(encrypted_path, "wb") as f:
                f.write(cipher.nonce + ciphertext)

            return redirect(url_for("index"))

    # Show available encrypted files
    files = os.listdir(ENCRYPTED_FOLDER)
    return render_template("index.html", files=files)


@app.route("/download/<filename>")
def download(filename):
    encrypted_path = os.path.join(ENCRYPTED_FOLDER, filename)
    decrypted_path = os.path.join(DECRYPTED_FOLDER, filename.replace(".enc", ""))

    if not os.path.exists(encrypted_path):
        return "File not found."

    # Decrypt
    with open(encrypted_path, "rb") as f:
        encrypted_data = f.read()

    nonce = encrypted_data[:16]
    ciphertext = encrypted_data[16:]

    cipher = AES.new(KEY, AES.MODE_EAX, nonce=nonce)
    decrypted_data = cipher.decrypt(ciphertext)

    with open(decrypted_path, "wb") as f:
        f.write(decrypted_data)

    return send_file(decrypted_path, as_attachment=True)
    

if __name__ == "__main__":
    app.run(debug=True)