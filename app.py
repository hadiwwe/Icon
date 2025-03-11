from flask import Flask, render_template_string

app = Flask(__name__)
index = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Starexx Items</title>
    <link rel="stylesheet" href="{{ url_for('static', filename='style.css') }}">
</head>
<body>
    <div class="loading-spinner" id="loadingSpinner">
        <div class="spinner"></div>
    </div>

    <div class="header" id="header" style="display: none;">
        <h1>Starexx Item ID</h1>
        <div class="input-container">
            <textarea id="search" placeholder="Search by Name, Item ID, or Icon Name" oninput="filterIcons()"></textarea>
        </div>
    </div>
    <div class="container" id="container" style="display: none;">
        <div class="grid-container" id="iconGrid"></div>
        <div class="pagination-container">
            <div class="pagination" id="pagination"></div>
        </div>
    </div>

    <div class="modal" id="modal">
        <div class="modal-content">
            <img id="modalImage">
            <p><b>Name:</b> <span id="modalName"></span><br><b>Item:</b> <span id="modalItemId"></span><br><b>Icon:</b> <span id="modalIconName"></span></p>
            <button class="modal-close" onclick="closeModal()">Tap to Close</button>
        </div>
    </div>

    <script src="{{ url_for('static', filename='script.js') }}"></script>
</body>
</html>
"""

@app.route("/")
def home():
    return render_template_string(index)

if __name__ == "__main__":
    app.run(debug=True)
