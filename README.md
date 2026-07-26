# 🔐 Caesar Cipher Encryption & Decryption Tool

A modern **Python GUI application** for encrypting and decrypting text using the **Caesar Cipher Algorithm**. This project was developed as **Task 2** for the **DecodeLabs Cyber Security Internship**.

The application provides an intuitive graphical user interface (GUI) built with **ttkbootstrap**, allowing users to securely encrypt and decrypt messages using a customizable shift key.



## ✨ Features

- 🔒 Encrypt text using the Caesar Cipher algorithm
- 🔓 Decrypt encrypted text
- 🔢 Custom shift key (1–25)
- 📋 Copy encrypted/decrypted text to clipboard
- 🧹 Clear all input and output fields
- 🚪 Exit application with one click
- ℹ️ About dialog with project information
- 🖼️ Custom application logo
- ✅ Input validation
- ✅ Shift key validation
- 📢 Professional status bar messages
- 🌙 Modern Dark Theme GUI
- ⌨️ Keyboard shortcuts for quick actions



## 🛠️ Technologies Used

- Python 3
- Tkinter
- ttkbootstrap
- Pillow (PIL)



## 📁 Project Structure

```
Basic Encryption & Decryption/
│
├── main.py
├── logo.png
├── icon.ico
├── requirements.txt
├── README.md
│
└── screenshots/
    ├── home.png
    ├── encrypt.png
    └── decrypt.png
```



## 🚀 Installation

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/your-username/your-repository-name.git
```

### 2️⃣ Open the Project Folder

```bash
cd your-repository-name
```

### 3️⃣ Install Required Libraries

```bash
pip install -r requirements.txt
```

### 4️⃣ Run the Application

```bash
python main.py
```


## 💻 How to Use

1. Launch the application.
2. Enter the message you want to encrypt or decrypt.
3. Enter a shift key between **1 and 25**.
4. Click **Encrypt** to encrypt the message.
5. Click **Decrypt** to decrypt the message.
6. Click **Copy** to copy the output.
7. Click **Clear** to reset all fields.
8. Click **Exit** to close the application.



## ⌨️ Keyboard Shortcuts

| Shortcut | Action |
|----------|--------|
| **Enter** | Encrypt Message |
| **Ctrl + C** | Copy Result |
| **Ctrl + L** | Clear Fields |


## 📸 Screenshots

### 🏠 Home Screen

![Home Screen](screenshots/home.png)

---

### 🔒 Encryption Example

![Encryption](screenshots/encrypt.png)

---

### 🔓 Decryption Example

![Decryption](screenshots/decrypt.png)


## 🔐 Caesar Cipher Algorithm

The **Caesar Cipher** is one of the oldest and simplest encryption techniques. Each alphabetic character is shifted by a fixed number of positions in the alphabet.

### Example

**Plain Text**

```
HELLO
```

**Shift Key**

```
3
```

**Encrypted Text**

```
KHOOR
```

**Decrypted Text**

```
HELLO
```

---

## ✅ Input Validation

The application includes validation to improve usability and prevent errors.

- Prevents empty input
- Accepts only numeric shift keys
- Restricts the shift key to values between **1 and 25**
- Displays meaningful status messages for user feedback



## 👨‍💻 Developer

**Aymen Altaf**

**DecodeLabs Cyber Security Internship**



## 📄 License

This project is developed for **educational purposes** as part of the **DecodeLabs Cyber Security Internship**.


