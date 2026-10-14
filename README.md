# Python File Integrity Checker (SHA-256)

A lightweight cybersecurity tool written in Python to compute and verify the cryptographic hash of files using SHA-256. Used for detecting unauthorized file tampering and verifying download integrity.

## Features
- Calculates SHA-256 cryptographic hashes efficiently using chunked memory handling.
- Compares calculated hashes against known reference hashes to flag potential file tampering.
- Built using Python standard libraries (`hashlib`, `sys`).

## Usage

### Generate SHA-256 Hash
```bash
python Security.py <file_path>