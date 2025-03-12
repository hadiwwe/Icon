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
        card.innerHTML = `<img src="${icon.imageUrl}" onerror="this.src='https://raw.githubusercontent.com/starexxx/IDItems/b8295c7bda85f3fadb7112ede8aa56b1e2d99680/assets/error-404.png'" onclick="showModal('${icon.name}', '${icon.itemId}', '${icon.iconName}', '${icon.imageUrl}')">`;
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
