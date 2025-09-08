# 📂 Secure File Sharing System

## 📌 Project Overview

This project **Secure File Sharing System** was developed during my
**Cybersecurity Internship with Future Intern**.\
It provides a **secure way to upload, encrypt, and share files** using
**Flask (Python)** and **AES Encryption**.

The system ensures **data confidentiality** by encrypting files before
storing them, preventing unauthorized access.

------------------------------------------------------------------------

## ⚡ Features

-   🔐 **AES Encryption** -- Secure encryption of uploaded files.\
-   📂 **Upload & Store** -- Files can be uploaded and securely stored.\
-   🔓 **Decryption** -- Encrypted files can be decrypted when needed.\
-   🌐 **Flask Web App** -- Simple user-friendly web interface.\
-   🗂️ **Organized Folders** -- Separate `uploads`, `encrypted`, and
    `decrypted` directories.

------------------------------------------------------------------------

## 🛠️ Tech Stack

-   **Backend:** Python (Flask)\
-   **Encryption:** AES (Crypto.Cipher)\
-   **Frontend:** HTML, CSS (basic)\
-   **Editor:** Visual Studio Code\
-   **Testing:** Localhost Flask server

------------------------------------------------------------------------

## 📁 Project Structure

    FILE_UPLOADS_FLASK/
    │── main.py                # Flask backend with AES encryption
    │── /templates             # HTML templates
    │   └── index.html
    │── /static                # Static files (CSS, JS if needed)
    │── /uploads               # Uploaded files
    │── /encrypted             # Encrypted files (.enc)
    │── /decrypted             # Decrypted files
    │── /venv                  # Virtual environment

------------------------------------------------------------------------

## 🚀 How It Works

1.  User uploads a file via the web interface.\
2.  The file is saved in the **uploads/** folder.\
3.  AES algorithm encrypts the file and stores it in **encrypted/**
    folder.\
4.  Users can download encrypted files and decrypt them for use.

------------------------------------------------------------------------

## 📸 Screenshots

### 🔹 Encrypted Hexadecimal Representation

Shows how uploaded files are securely encrypted.

### 🔹 Flask Backend (main.py)

Contains encryption logic and Flask routes.

### 🔹 Frontend (index.html)

User-friendly interface for uploading and downloading files.

### 🔹 Project Folder Structure

Organized system with uploads, encrypted, and decrypted directories.

### 🔹 Encrypted Files (.enc)

Files stored in unreadable format to maintain confidentiality.

### 🔹 Encrypted Binary Content

Unreadable characters ensuring file security.

### 🔹 Web Interface on Localhost

Simple and clean design to test secure file sharing.

------------------------------------------------------------------------

## 📌 Future Scope

-   Add **user authentication** (login system).\
-   Implement **role-based access control**.\
-   Deploy on **cloud platform (AWS/Heroku)**.\
-   Add support for **multiple encryption algorithms**.

------------------------------------------------------------------------

## 🏆 Internship Experience

This project was a part of my **Cybersecurity Internship with Future
Intern**.\
It gave me hands-on experience in:\
- Applying **cryptography (AES)** in real-world projects.\
- Developing **Flask-based web applications**.\
- Understanding **file confidentiality & secure sharing mechanisms**.

------------------------------------------------------------------------

✨ Developed with passion during my **Cybersecurity Internship** 🚀
