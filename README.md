# 🛡️ Garuda File Integrity Verifier

A lightweight yet powerful tool built under the **Garuda Sentinel** mission to verify **file integrity** using **HMAC (Hash-based Message Authentication Code)** with **SHA3-256**. This tool ensures that files are not tampered with and remain authentic when transferred or stored.

---

## 🔐 Project Goal

To provide a **cryptographically secure method** to verify that a file has not been altered, by generating and validating HMACs based on a secret key.

This project is based on concepts from the book _Serious Cryptography_ and continues the mission of building real-world cybersecurity tools one concept at a time.

---

## ✅ Features

- 🔑 Uses **HMAC with SHA3-256** for message authentication.
- 📂 Accepts any **local file path** to compute or verify the HMAC.
- 👁️‍🗨️ Verifies whether a file is **authentic** or **tampered with**.
- 🧠 Educational implementation of cryptographic integrity using Python.

---

## 🧪 How It Works

1. **Create HMAC:**
   - Input a file path and a secret key.
   - The system generates and outputs a hexadecimal HMAC using SHA3-256.

2. **Verify HMAC:**
   - Input the same file, the original secret key, and the received HMAC.
   - The tool recalculates the HMAC and compares it to the one provided.
   - If they match, the file is authentic. If not, it has been altered or the key is wrong.

---
---
#🌐 Future Enhancements
🔄 Cloud-Based Verification

Upload files and their HMACs to a secure cloud storage.

Allow remote users to verify file authenticity using just the HMAC and the public hash.

🔏 File Confidentiality with Encryption

Extend this system to not only check integrity but also encrypt and decrypt files securely using AES (with key derived from passwords via PBKDF2).

🧾 Audit Trail Support

Log and timestamp each verification to build a tamper-proof audit trail.
---

## 🖥️ Usage

```bash
python FileIntegrityVerifier.py
=== Garuda File Integrity Checker ===
1. Create HMAC for a file
2. Verify file integrity
Enter your choice (1 or 2): 1
Enter the path to the local file: secret_notes.txt
Enter a secret key: myStrongKey123
✅ Generated HMAC (hex): 2d3aef...a37b
