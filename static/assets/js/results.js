document.getElementById('lga-select').addEventListener('change', (event) => {
    let lga_id = event.target.value;

    fetch(`/compute-result?lga_id=${lga_id}`)
        .then((response) => {
            return response.json();
        })
        .then(data => {
            generateGrid(data);
        })
        .catch(error => {
            console.error(error);
        });
});

const generateGrid = (results) => {
    let grid = document.getElementById('results-grid');
    grid.innerHTML = '';

    for (const [party, votes] of Object.entries(results)) {
        let column = document.createElement('div');
        column.className = 'col-md-4 mb-4';

        let card = `
        <div class="card text-center">
            <div class="card-body">
                 <h5 class="card-title">${party}</h5>
                 <p class="card-text">Total Votes: ${votes}</p>
            </div>
        </div>`;

        column.innerHTML = card;

        grid.appendChild(column);


        // some LGAs have no votes; so some results will be blank
    }
}