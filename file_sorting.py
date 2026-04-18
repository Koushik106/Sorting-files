import os
import shutil

folders = {
    # PDFs
    ".pdf": "PDFs",
    # Images
    ".jpg": "Images",
    ".jpeg": "Images",
    ".png": "Images",
    ".gif": "Images",
    ".bmp": "Images",
    ".tiff": "Images",
    ".webp": "Images",
    ".svg": "Images",
    ".ico": "Images",
    ".heic": "Images",
    ".heif": "Images",
    ".raw": "Images",
    ".psd": "Images/Photoshop",
    ".ai": "Images/Illustrator",
    # Documents
    ".doc": "Documents/Word",
    ".docx": "Documents/Word",
    ".txt": "Documents/Text",
    ".rtf": "Documents/Text",
    ".odt": "Documents/Text",
    ".md": "Documents/Markdown",
    ".tex": "Documents/Latex",
    # Spreadsheets
    ".xls": "Documents/Excel",
    ".xlsx": "Documents/Excel",
    ".xlsm": "Documents/Excel",
    ".csv": "Documents/Excel",
    ".ods": "Documents/Excel",
    # Presentations
    ".ppt": "Documents/PowerPoint",
    ".pptx": "Documents/PowerPoint",
    ".pps": "Documents/PowerPoint",
    ".odp": "Documents/PowerPoint",
    # Videos
    ".mp4": "Videos",
    ".mkv": "Videos",
    ".avi": "Videos",
    ".mov": "Videos",
    ".wmv": "Videos",
    ".flv": "Videos",
    ".webm": "Videos",
    ".m4v": "Videos",
    ".3gp": "Videos",
    # Audio
    ".mp3": "Audio",
    ".wav": "Audio",
    ".aac": "Audio",
    ".flac": "Audio",
    ".ogg": "Audio",
    ".m4a": "Audio",
    ".wma": "Audio",
    ".opus": "Audio",
    # Archives
    ".zip": "Archives",
    ".rar": "Archives",
    ".7z": "Archives",
    ".tar": "Archives",
    ".gz": "Archives",
    ".bz2": "Archives",
    ".xz": "Archives",
    # Code files
    ".py": "Code/Python",
    ".pyc": "Code/Python",
    ".js": "Code/JavaScript",
    ".ts": "Code/TypeScript",
    ".html": "Code/HTML",
    ".css": "Code/CSS",
    ".scss": "Code/CSS",
    ".java": "Code/Java",
    ".cpp": "Code/C++",
    ".hpp": "Code/C++",
    ".c": "Code/C",
    ".cs": "Code/CSharp",
    ".go": "Code/Go",
    ".rs": "Code/Rust",
    ".php": "Code/PHP",
    ".rb": "Code/Ruby",
    ".swift": "Code/Swift",
    ".kt": "Code/Kotlin",
    ".json": "Code/JSON",
    ".xml": "Code/XML",
    ".yaml": "Code/YAML",
    ".yml": "Code/YAML",
    ".sql": "Code/SQL",
    ".sh": "Code/Shell",
    # Executables / Apps
    ".exe": "Applications",
    ".msi": "Applications",
    ".apk": "Applications",
    ".bat": "Applications",
    ".app": "Applications",
    ".deb": "Applications",
    ".rpm": "Applications",
    # Disk / Virtual Images
    ".iso": "Disk Images",
    ".img": "Disk Images",
    ".vhd": "Disk Images",
    ".vmdk": "Disk Images",
    # Databases
    ".db": "Databases",
    ".sqlite": "Databases",
    ".sqlite3": "Databases",
    ".mdb": "Databases",
    # Logs
    ".log": "Logs",
    # Fonts
    ".ttf": "Fonts",
    ".otf": "Fonts",
    ".woff": "Fonts",
    ".woff2": "Fonts",
    # Torrents
    ".torrent": "Torrents",
    # Config / System
    ".ini": "Config",
    ".cfg": "Config",
    ".env": "Config",
    # Backup files
    ".bak": "Backups",
    ".tmp": "Temp",
}
file_path = input("Enter File Path: ")
for file in os.listdir(file_path):
    if os.path.isfile(os.path.join(file_path, file)):
        name, ext = os.path.splitext(file)
        if ext in folders:
            subfolder = os.path.join(file_path, folders[ext])
            os.makedirs(subfolder, exist_ok=True)
            shutil.move(os.path.join(file_path, file), subfolder)
            print("Folders has been created sucessfully !!!")
