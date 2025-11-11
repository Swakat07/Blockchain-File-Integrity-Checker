from flask import Flask, request, render_template, redirect, url_for
import hashlib, json, os
from datetime import datetime

app = Flask(__name__)
BLOCKCHAIN_FILE = 'ledger.json'

if not os.path.exists(BLOCKCHAIN_FILE):
    with open(BLOCKCHAIN_FILE, 'w') as f:
        json.dump([], f)

def get_hash(filename):
    with open(filename, "rb") as f:
        file_bytes = f.read()
    return hashlib.sha256(file_bytes).hexdigest()

def add_block(file_hash, filename):
    with open(BLOCKCHAIN_FILE, 'r+') as f:
        chain = json.load(f)
        prev_hash = chain[-1]['hash'] if chain else '0' * 64
        new_block = {
            "index": len(chain) + 1,
            "filename": filename,
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "prev_hash": prev_hash,
            "hash": file_hash
        }
        chain.append(new_block)
        f.seek(0)
        json.dump(chain, f, indent=4)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    file = request.files['file']
    filename = file.filename
    file.save(filename)

    current_hash = get_hash(filename)
    with open(BLOCKCHAIN_FILE, 'r') as f:
        chain = json.load(f)

    if any(b['hash'] == current_hash for b in chain):
        message = f"✅ Integrity Verified: '{filename}' matches the stored hash."
    else:
        add_block(current_hash, filename)
        message = f"🆕 New file '{filename}' added to blockchain ledger."

    os.remove(filename)
    return render_template('index.html', message=message)

@app.route('/ledger')
def ledger():
    with open(BLOCKCHAIN_FILE, 'r') as f:
        chain = json.load(f)
    return render_template('ledger.html', chain=chain)

if __name__ == '__main__':
    app.run(debug=True)
