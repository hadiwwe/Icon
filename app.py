from flask import Flask, render_template_string, redirect, url_for, request
app = Flask(__name__)

starexx = """
<!DOCTYPE html>
<html lang="en">
<head>
    <title>Starexx Items</title>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
      <link rel="preconnect" href="https://fonts.googleapis.com">
      <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
      <link href="https://fonts.googleapis.com/css2?family=IBM+Plex+Mono:ital,wght@0,100;0,200;0,300;0,400;0,500;0,600;0,700;1,100;1,200;1,300;1,400;1,500;1,600;1,700&display=swap" rel="stylesheet">
      <meta name="author" content="Starexx">
      <meta name="og:title" content="Starexx Items">
      <meta name="og:description" content="Search Free Fire game items by name or description to retrieve item ID, name & details.">
      <meta name="google-site-verification" content="J20YkdBYbFS0_YZdIu9Z-sKGKzYZfqOFFkQ0numjLq0" />
      <meta name="description" content="Free Fire is a multiplayer battle royale mobile game, developed and published by Garena for Android and iOS. Battle in Style and be the last survivor!">
      <meta name="keywords" content="survival, last survivor, battle royale, free mobile game, garena game, craftland, ugc, starexz.m, ff craftland, ankit-mehta, starexx7, Starexx, starexx, craftland tutorial, free fire craftland, ff-item">
      <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
      <style>
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600&display=swap');
        body {
            background-color: #000;
            color: #fff;
            font-family: 'Inter', sans-serif;
            margin: 0;
            padding: 0;
        }

        .header {
            width: 100%;
            padding: 15px;
            font-size: 20px;
            font-weight: bold;
            text-align: left;
            background: rgba(0, 0, 0, 0.9);
        }

        .header h1 {
            margin-left: 5px;
            margin-top: 5px;
            font-size: 24px;
            font-weight: bold;
        }

        .container {
            padding: 20px;
            max-width: 900px;
            margin-left: auto;
            margin-right: auto;
            text-align: left;
        }

        .grid-container {
            display: grid;
            grid-template-columns: repeat(5, 1fr);
            gap: 10px;
        }

        .icon-card {
          background: #000;
          padding: 15px;
          border-radius: 50px;
          text-align: center;
          cursor: pointer;
          border: 1px solid #121212;
          transition: transform 0.2s ease, background 0.2s ease;
       }

       .icon-card:hover {
          background: #121212;
          border: 1px solid #333;
          transform: scale(1.05);
       }
 
       .icon-card img {
          width: 40px;
          max-width: 40px;
          height: auto;
          border-radius: 10px;
        }

        .pagination-container {
            margin-top: 20px;
            display: flex;
            justify-content: center;
        }

        .pagination {
            display: flex;
            overflow-x: auto;
            white-space: nowrap;
            background: #000;
            border: 1px solid #121212;
            padding: 5px;
            border-radius: 25px;
            max-width: 100%;
        }

        .pagination button {
            padding: 5px 12px;
            margin: 2px;
            border: none;
            background: transparent;
            color: white;
            cursor: pointer;
            border-radius: 50px;
            font-size: 14px;
            transition: background 0.2s ease, color 0.2s ease;
        }

        .pagination button:hover {
            background: #121212;
            color: white;
        }

        .pagination button.active {
            background: #fff;
            color: black;
        }

        .modal {
            display: none;
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background-color: rgba(0, 0, 0, 0.8);
            backdrop-filter: blur(10px);
            align-items: center;
            justify-content: center;
            animation: fadeIn 0.3s ease;
        }

        @keyframes fadeIn {
            from { opacity: 0; }
            to { opacity: 1; }
        }

        .modal-content {
            background-color: transparent;
            padding: 20px;
            border-radius: 30px;
            text-align: left;
            border: none;
            color: white;
            max-width: 80%;
            overflow-y: auto;
            animation: slideUp 0.3s ease;
        }

        @keyframes slideUp {
            from { transform: translateY(20px); }
            to { transform: translateY(0); }
        }

        .modal img {
            width: 100px;
            height: auto;
            margin-bottom: 10px;
            border-radius: 0px;
        }

        .modal-close {
            margin-top: 10px;
            padding: 8px;
            border: none;
            background: transparent;
            text-align: center;
            color: #ccc;
            font-size: 12px;
            cursor: pointer;
            border-radius: 20px;
            transition: background 0.2s ease, color 0.2s ease;
        }
    
        .input-container {
            margin-top: 15px;
            max-width: 100%;
            width: 100%;
        }

        textarea {
            width: 100%;
            padding: 12px;
            border-radius: 25px;
            border: 1px solid #121212;
            background-color: rgba(0, 0, 0);
            color: #fff;
            font-size: 12.5px;
            height: 49px;
            resize: none;
            padding-right: 50px;
            transition: all 0.3s;
            text-align: left;
        }

        textarea:focus {
            outline: none;
            border: 1px solid #121212;
            background-color: #000;
        }

        .loading-spinner {
            position: fixed;
            top: 50%;
            left: 50%;
            transform: translate(-50%, -50%);
            text-align: center;
        }

        .spinner {
            border: 4px solid rgba(255, 255, 255, 0.1);
            border-radius: 50%;
            border-top: 4px solid #fff;
            width: 25px;
            height: 25px;
            animation: spin 0.5s linear infinite;
        }

        @keyframes spin {
            0% { transform: rotate(0deg); }
            100% { transform: rotate(360deg); }
        }
    </style>
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

    <script>
        let iconsData = [];
        let filteredData = [];
        let currentPage = 0;
        const itemsPerPage = 100;

        setTimeout(() => {
            document.getElementById('loadingSpinner').style.display = 'none';
            document.getElementById('header').style.display = 'block';
            document.getElementById('container').style.display = 'block';
        }, 2000);

        async function fetchIcons() {
            try {
                let response = await fetch("https://raw.githubusercontent.com/starexxx/starexxx/refs/heads/main/app.json");
                let data = await response.json();
                
                iconsData = data.map(item => ({
                    itemId: item["Item_ID"],
                    name: item["Name"],
                    iconName: item["Icon_Name"],
                    imageUrl: `https://system.ffgarena.cloud/api/iconsff?image=${item["Item_ID"]}.png`
                }));

                filteredData = [...iconsData];
                displayIcons();
            } catch (error) {
                console.error("Error fetching icons:", error);
            }
        }

        function displayIcons() {
            let start = currentPage * itemsPerPage;
            let end = start + itemsPerPage;
            let visibleIcons = filteredData.slice(start, end);
            
            let grid = document.getElementById("iconGrid");
            grid.innerHTML = "";

            visibleIcons.forEach(icon => {
                let card = document.createElement("div");
                card.classList.add("icon-card");
                card.innerHTML = `<img src="${icon.imageUrl}" onerror="this.src='https://raw.githubusercontent.com/starexxx/starexxx/347d6405a9cdfc898837b91333f6bd5b0fb27257/error-404.png'" onclick="showModal('${icon.name}', '${icon.itemId}', '${icon.iconName}', '${icon.imageUrl}')">`;
                grid.appendChild(card);
            });

            updatePagination();
        }

        function updatePagination() {
            let totalPages = Math.ceil(filteredData.length / itemsPerPage);
            let paginationDiv = document.getElementById("pagination");
            paginationDiv.innerHTML = "";

            for (let i = 0; i < totalPages; i++) {
                let btn = document.createElement("button");
                btn.innerText = i + 1;
                btn.classList.toggle("active", i === currentPage);
                btn.onclick = () => goToPage(i);
                paginationDiv.appendChild(btn);
            }
        }

        function goToPage(page) {
            currentPage = page;
            displayIcons();
        }

        function filterIcons() {
            let query = document.getElementById("search").value.toLowerCase();
            filteredData = iconsData.filter(icon =>
                icon.name.toLowerCase().includes(query) ||
                icon.itemId.toLowerCase().includes(query) ||
                icon.iconName.toLowerCase().includes(query)
            );
            currentPage = 0;
            displayIcons();
        }

        function showModal(name, itemId, iconName, imageUrl) {
            document.getElementById("modalName").innerText = name;
            document.getElementById("modalItemId").innerText = itemId;
            document.getElementById("modalIconName").innerText = iconName;
            document.getElementById("modalImage").src = imageUrl;
            document.getElementById("modal").style.display = "flex";
        }

        function closeModal() {
            document.getElementById("modal").style.display = "none";
        }

        fetchIcons();
    </script>
</body>
</html>
"""

@app.route("/")
def home():
    return render_template_string(starexx)

@app.route("/script")
def script_redirect():
    current_url = request.url_root.strip("/")
    return redirect(f"view-source:{current_url}")

@app.errorhandler(404)
def page_not_found(e):
    return redirect(url_for("home"))

if __name__ == "__main__":
    app.run(debug=True, port=50000)
