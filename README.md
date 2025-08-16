
# Syslog Viewer 🔍

A lightweight Flask-based web application to **upload, search, and view system log files** in a simple web interface.  
It supports **regex search with highlighting**, file uploads, and a clean UI for browsing logs.

---

## 📂 Project Structure


syslog_viewer/
│── app.py # Entry point
│── syslog_viewer/ # Package
│ │── init.py
│ │── routes.py # Flask routes (upload, search, display logs)
│ │── log_handler.py # Log file handling (save & search)
│ │── config.py # Configuration (upload folder, etc.)
│ └── templates/
│ └── index.html # UI template
│── requirements.txt # Dependencies
│── setup.py # Installation script
---

## 🚀 Features

- Upload `.log` or `.txt` files.  
- Search logs using **regular expressions**.  
- Highlighted results for quick analysis.  
- Flash messages for uploads and searches.  
- Mobile-friendly layout.  

---

## 🛠️ Setup & Run

1. Clone the repo:

2. Create a virtual environment (optional but recommended)
   python -m venv venv
   source venv/bin/activate   # Linux/Mac
   venv\Scripts\activate      # Windows
3. Install dependencies:
   🛠 Requirements
       Python 3.8+
       Flask
   pip install -r requirements.txt
4. Start the App
   python app.py
5. Open in your browser:
   http://127.0.0.1:5000
Configuration

UPLOAD_FOLDER and ALLOWED_EXTENSIONS can be modified in
syslog_viewer/config.py

🔮 Future Ideas

Pagination for very large logs.

Real-time log tailing (tail -f style).

Authentication for multiple users.

Export search results.

🧑‍💻 Author

Developed by Vikash Kumar

Contributions welcome!



