# 🔐 Blockchain File Integrity Checker

A Python + Flask-based project that uses **blockchain principles** to verify the **integrity of digital files**.  
It ensures that uploaded files have not been tampered with by storing and validating their **SHA-256 hash values** inside a blockchain-like ledger.

---

## 📖 Table of Contents
- [Overview](#overview)
- [Features](#features)
- [Project Structure](#project-structure)
- [How It Works](#how-it-works)
- [Installation](#installation)
- [Usage](#usage)
- [Testing the System](#testing-the-system)
- [Example Ledger](#example-ledger)
- [Technologies Used](#technologies-used)
- [Future Improvements](#future-improvements)
- [Author](#author)

---

## 🧩 Overview

The **Blockchain File Integrity Checker** provides a secure and transparent way to ensure that a file has not been modified after its original verification.  

Every uploaded file’s **SHA-256 hash** is stored as a block inside a **JSON-based blockchain ledger**.  
When the same file is uploaded again, the system re-computes its hash and compares it with the existing records to determine if it has been tampered with.

---

## 🚀 Features

✅ Upload any file (text, PDF, image, etc.)  
✅ Compute unique SHA-256 file hash  
✅ Store file information as chained blocks in a JSON ledger  
✅ Detect even a 1-bit change in file content  
✅ Simple web interface built using Flask  
✅ Tamper-proof blockchain structure (each block linked with previous hash)  

---

## 🗂 Project Structure

Blockchain-File-Integrity-Checker/
│
├── app.py # Main Flask application
├── ledger.json # Blockchain ledger (stores file hash history)
├── templates/ # HTML templates for web interface
│ ├── index.html
│ └── result.html
└── static/ # (optional) CSS or JS files


---

## 🔗 How It Works

1. User uploads a file through the web interface.  
2. The system calculates the **SHA-256 hash** of the file.  
3. If it’s a new file, a new block is created and added to the blockchain ledger (`ledger.json`).  
4. If the file already exists, the system compares the current hash with the stored one:  
   - ✅ **Match:** File integrity verified.  
   - ⚠️ **Mismatch:** File has been modified or corrupted.  
5. Each new block references the **previous block’s hash**, ensuring immutability.

---

## 🧰 Installation

### Prerequisites
- Python 3.x  
- pip (Python package manager)

### Steps
1. Clone the repository:
   ```bash
   git clone https://github.com/Swakat07/Blockchain-File-Integrity-Checker.git
Navigate into the folder:

cd Blockchain-File-Integrity-Checker


Install dependencies:

pip install -r requirements.txt


Run the Flask app:

python app.py


Open your browser and go to:

http://127.0.0.1:5000/

🧪 Testing the System

You can test file integrity using these sample files:
👉 Blockchain_Integrity_Test_Files.zip

Steps:

Upload any of the files (e.g., file1.txt) → Integrity Verified (new file).

Re-upload the same file → ✅ Integrity Verified.

Edit the file (e.g., change one word or space) → ⚠️ Integrity Compromised.

🧾 Example Blockchain Ledger (ledger.json)
[
    {
        "index": 1,
        "timestamp": "2025-11-11 14:33:00",
        "file_name": "file1.txt",
        "file_hash": "4f2b3a2c16e42d...",
        "previous_hash": "0"
    },
    {
        "index": 2,
        "timestamp": "2025-11-11 14:35:12",
        "file_name": "file2.pdf",
        "file_hash": "a78dbcd1f3a7e9...",
        "previous_hash": "4f2b3a2c16e42d..."
    }
]


Each new file added becomes a block, linked to the previous one by the previous_hash — mimicking blockchain behavior.

🧠 Technologies Used

Python 3.x

Flask – web framework for backend

hashlib – for SHA-256 hash generation

JSON – to store the blockchain ledger

HTML/CSS – for web interface

🔮 Future Improvements

Implement a real distributed blockchain instead of local JSON ledger

Add user authentication

Integrate file encryption and digital signatures

Add REST API for remote integrity verification

Results:
<img width="1776" height="1030" alt="image" src="https://github.com/user-attachments/assets/ed144c50-e3ff-4a56-a9ed-bd10df661356" />
<img width="1777" height="1025" alt="image" src="https://github.com/user-attachments/assets/fe182242-372a-4f17-9b9b-fd6b3db5da43" />
<img width="1785" height="969" alt="image" src="https://github.com/user-attachments/assets/5ed05167-bab4-41eb-ab8f-b516ede524cf" />
<img width="1907" height="964" alt="image" src="https://github.com/user-attachments/assets/c6dd9790-ed6e-4a3c-9149-6ff9da96df7a" />


