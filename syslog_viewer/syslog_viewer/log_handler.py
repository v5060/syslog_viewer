import os


class LogHandler:
    def __init__(self, upload_folder):
        self.upload_folder = upload_folder
        self.uploaded_file_path = None

    def save_file(self, file):
        """Save uploaded syslog file"""
        path = os.path.join(self.upload_folder, file.filename)
        file.save(path)
        self.uploaded_file_path = path
        return path

    def search_pattern(self, pattern):
        """Search for a pattern in the uploaded log file"""
        if not self.uploaded_file_path:
            return []

        results = []
        with open(self.uploaded_file_path, "r", errors="ignore") as f:
            for line in f:
                if pattern in line:
                    results.append(line.strip())
        return results
