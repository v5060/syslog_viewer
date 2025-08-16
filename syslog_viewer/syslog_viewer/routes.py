import re
from flask import Blueprint, render_template, request, flash
from markupsafe import Markup
from .log_handler import LogHandler
from .config import Config

bp = Blueprint("routes", __name__)
log_handler = LogHandler(Config.UPLOAD_FOLDER)


@bp.route("/", methods=["GET", "POST"])
def index():
    results = []
    message = None

    if request.method == "POST":
        # File upload
        if "file" in request.files:
            file = request.files["file"]
            if file and file.filename:
                log_handler.save_file(file)
                flash("File uploaded successfully!", "success")

        # Pattern search
        if "pattern" in request.form:
            pattern = request.form.get("pattern", "").strip()
            if pattern:
                raw_results = log_handler.search_pattern(pattern)

                if raw_results:
                    regex = re.compile(re.escape(pattern), re.IGNORECASE)
                    for line in raw_results:
                        highlighted_line = regex.sub(
                            lambda m: f"<mark>{m.group(0)}</mark>", line
                        )
                        results.append(Markup(highlighted_line))
                else:
                    message = f"No matches found for: {pattern}"
            else:
                message = "Please enter a valid search pattern."

    return render_template("index.html", results=results, message=message)
