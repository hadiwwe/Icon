let iconsData = [];
let filteredData = [];
let currentPage = 0;
const itemsPerPage = 100;

document.addEventListener("DOMContentLoaded", () => {
    setTimeout(() => {
        document.getElementById("loadingSpinner").style.display = "none";
        document.getElementById("header").style.display = "block";
        document.getElementById("container").style.display = "block";
    }, 2000);

    fetchIcons();
});

async function fetchIcons() {
    try {
        const response = await fetch("https://raw.githubusercontent.com/starexxx/starexxx/refs/heads/main/app.json");
        const data = await response.json();

        iconsData = data.map(item => ({
            itemId: item["Item_ID"],
            name: item["Name"],
            iconName: item["Icon_Name"],
            imageUrl: `https://system.ffgarena.cloud/api/iconsff?image=${item["Item_ID"]}.png`
        }));

        filteredData = [...iconsData];
        renderIcons();
    } catch (error) {
        console.error("Failed to fetch icons:", error);
    }
}

function renderIcons() {
    const start = currentPage * itemsPerPage;
    const end = start + itemsPerPage;
    const visibleIcons = filteredData.slice(start, end);
    
    const grid = document.getElementById("iconGrid");
    grid.innerHTML = "";

    visibleIcons.forEach(icon => {
        const card = document.createElement("div");
        card.classList.add("icon-card");
        card.innerHTML = `
            <img src="${icon.imageUrl}" 
                 onerror="this.src='assets/error-404.png'" 
                 onclick="openModal('${icon.name}', '${icon.itemId}', '${icon.iconName}', '${icon.imageUrl}')">
        `;
        grid.appendChild(card);
    });

    updatePagination();
}

function updatePagination() {
    const totalPages = Math.ceil(filteredData.length / itemsPerPage);
    const paginationDiv = document.getElementById("pagination");
    paginationDiv.innerHTML = "";

    for (let i = 0; i < totalPages; i++) {
        const button = document.createElement("button");
        button.textContent = i + 1;
        button.classList.toggle("active", i === currentPage);
        button.onclick = () => changePage(i);
        paginationDiv.appendChild(button);
    }
}

function changePage(page) {
    currentPage = page;
    renderIcons();
}

function filterIcons() {
    const query = document.getElementById("search").value.toLowerCase();
    filteredData = iconsData.filter(icon =>
        icon.name.toLowerCase().includes(query) ||
        icon.itemId.toLowerCase().includes(query) ||
        icon.iconName.toLowerCase().includes(query)
    );
    currentPage = 0;
    renderIcons();
}

function openModal(name, itemId, iconName, imageUrl) {
    document.getElementById("modalName").textContent = name;
    document.getElementById("modalItemId").textContent = itemId;
    document.getElementById("modalIconName").textContent = iconName;
    document.getElementById("modalImage").src = imageUrl;
    document.getElementById("modal").style.display = "flex";
}

function closeModal() {
    document.getElementById("modal").style.display = "none";
}
