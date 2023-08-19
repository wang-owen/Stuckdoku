let number_choice = null;
let tile_choice = null;

window.onload = () => {
    create();
};

function create() {
    for (let i = 0; i <= 9; i++){
        let number = document.createElement("div");
        number.id = i;
        number.innerText = i;
        number.classList.add("number")

    }

    for (let r = 0; r < 9; r++){
        for (let c=0; c<9; c++){
            let tile = document.createElement("div");
            tile.id = r.toString() + "-" +c.toString();
            tile.classList.add("tile");
            document.getElementById("sudoku_board").append(tile);


        }
    }
}
