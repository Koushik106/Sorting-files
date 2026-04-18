# 📂 File Organizer Script (Python)

A simple and efficient Python script to automatically organize files into folders based on their file extensions.

---

## 🚀 Features

* 📁 Automatically sorts files into categorized folders
* 🧠 Supports a wide range of file types:

  * Images, Videos, Audio
  * Documents (Word, Excel, PowerPoint, Text, Markdown)
  * Code files (Python, JavaScript, C++, etc.)
  * Archives, Databases, Fonts, and more
* 📦 Creates folders automatically if they don’t exist
* ⚡ Fast and lightweight (no external libraries required)

---

## 🛠️ How It Works

1. You provide a directory path
2. The script scans all files in that directory
3. Each file is moved into a folder based on its extension

Example:

```
Before:
📁 Downloads
 ├── file.mp4
 ├── image.png
 ├── notes.txt

After:
📁 Downloads
 ├── 📁 Videos
 │    └── file.mp4
 ├── 📁 Images
 │    └── image.png
 ├── 📁 Documents/Text
      └── notes.txt
```

---

## ▶️ Usage

### 1. Clone the repository

```bash
git clone https://github.com/Koushik106/Sorting-files.git
cd Sorting-files
```

### 2. Run the script

```bash
python file_sorting.py
```

### 3. Enter the folder path

```
Enter File Path: C:/Users/YourName/Downloads
```

---

## 📂 Supported Categories

* **Images** → `.jpg`, `.png`, `.svg`, `.psd`, `.ai`, etc.
* **Videos** → `.mp4`, `.mkv`, `.avi`, etc.
* **Audio** → `.mp3`, `.wav`, `.flac`, etc.
* **Documents** → `.docx`, `.pdf`, `.txt`, `.md`, etc.
* **Code** → `.py`, `.js`, `.cpp`, `.java`, etc.
* **Archives** → `.zip`, `.rar`, `.7z`, etc.
* **Applications** → `.exe`, `.apk`, etc.
* **And many more...**

---

## ⚠️ Important Notes

* The script **moves files**, it does not copy them
* Make sure to:

  * Use the correct folder path
  * Backup important files if needed
* Currently, files with unknown extensions are ignored


## 🤝 Contributing

Feel free to fork this repo and improve it!

---


## ⭐ If you like this project

Give it a star on GitHub ⭐
