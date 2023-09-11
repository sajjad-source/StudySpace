window.onload = function() {
    fetch('http://localhost:5001/api/spaces')
        .then(response => response.json())
        .then(data => {
            displaySpaces(data.spaces);
            document.getElementById('sort').addEventListener('change', function() {
                const sortedSpaces = sortSpaces(data.spaces, this.value);
                displaySpaces(sortedSpaces);
            });
        });
};

function displaySpaces(spaces) {
    const spacesDiv = document.getElementById('spaces');
    spacesDiv.innerHTML = ''; // Clear previous spaces
    for (let space of spaces) {
        const spaceDiv = document.createElement('div');
        spaceDiv.classList.add('space');
        spaceDiv.innerHTML = `
            <h2>${space.title}</h2>
            <p>${space.location}</p>
            <p>${space.capacity}</p>
            <p>${space.amenities}</p>
            ${space.reserve_url ? `<a href="${space.reserve_url}" class="reserve-btn">Reserve</a>` : ''}
        `;
        spacesDiv.appendChild(spaceDiv);
    }
}

function sortSpaces(spaces, criteria) {
    return spaces.slice().sort((a, b) => {
        if (a[criteria] < b[criteria]) return -1;
        if (a[criteria] > b[criteria]) return 1;
        return 0;
    });
}


let lastScrollTop = 0;

window.addEventListener("scroll", function() {
    let currentScrollTop = window.pageYOffset || document.documentElement.scrollTop;
    if (currentScrollTop > lastScrollTop){
        // Downscroll
        document.querySelector("header").style.top = "-100px";
    } else {
        // Upscroll
        document.querySelector("header").style.top = "0";
    }
    lastScrollTop = currentScrollTop;
}, false);