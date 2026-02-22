function renderList(games) {
    const listView = document.getElementById("list-view");
    listView.innerHTML = "";

    if (games.length === 0) {
        listView.innerHTML = "<p style='text-align:center;'>No games found.</p>";
        return;
    }

    const container = document.createElement("div");
    container.className = "genre-card";
    container.style.maxWidth = "800px";
    container.style.margin = "20px auto";
    listView.appendChild(container);

    const tbl = document.createElement("table");
    const headerRow = tbl.insertRow();
    
    ["Image", "Title", "Genre", "Rating", "Actions"].forEach(text => {
        const th = document.createElement("th");
        th.textContent = text;
        headerRow.appendChild(th);
    });

    games.forEach(game => {
        const row = tbl.insertRow();

        const imgCell = row.insertCell();
        const img = document.createElement("img");
        img.src = game.image_url || 'https://placehold.co/100x130?text=No+Image';
        img.style.width = "60px"; // Thumbnail size for table
        img.style.borderRadius = "4px";
        img.style.display = "block";
        img.onerror = () => { img.src = 'https://placehold.co/100x130?text=Error'; };
        imgCell.appendChild(img);

        row.insertCell().textContent = game.title;
        row.insertCell().textContent = game.genre;
        row.insertCell().textContent = game.rating;

        const actionsCell = row.insertCell();

        const editButton = document.createElement("button");
        editButton.textContent = "Edit";
        editButton.onclick = () => updateGame(game.id);
        actionsCell.appendChild(editButton);
        
        const deleteButton = document.createElement("button");
        deleteButton.textContent = "Delete";
        deleteButton.onclick = () => deleteGame(game.id);
        actionsCell.appendChild(deleteButton);
    });

    container.appendChild(tbl);
}

function renderStats(totalCount, globalAvg, globalTop) {
    const statsContent = document.getElementById("stats-content");
    const pageSize = typeof recordsPerPage !== 'undefined' ? recordsPerPage : 10;

    statsContent.innerHTML = `
        <div class="stats-grid">
            <div class="stat-card blue">
                <span class="stat-value">${totalCount}</span>
                <span class="stat-label">Total Games in Collection</span>
            </div>
            <div class="stat-card gold">
                <span class="stat-value">${globalAvg}</span>
                <span class="stat-label">Average Rating</span>
            </div>
            <div class="stat-card purple">
                <span class="stat-value">${globalTop}</span>
                <span class="stat-label">Most Played Genre</span>
            </div>
            <div class="stat-card red">
                <span class="stat-value">${pageSize}</span>
                <span class="stat-label">Current Page Size</span>
            </div>
        </div>
    `;
}