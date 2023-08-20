window.onload = () => {
  create();
  addKeyboardListeners();
};

const board_values = [];

function create() {
  for (let r = 0; r < 9; r++) {
    const row = [];
    for (let c = 0; c < 9; c++) {
      const tile = document.createElement("div");
      tile.id = r.toString() + "-" + c.toString();
      tile.classList.add("tile");
      tile.setAttribute("contenteditable", "true");

      const value = Board[r][c];
      if (value !== 0) {
        tile.innerText = value;
      }

      document.getElementById("sudoku_board").append(tile);
      row.push(tile);
    }
    board_values.push(row);
  }
}
let selectedTile = null;

function addKeyboardListeners() {
  const tiles = document.querySelectorAll(".tile");

  tiles.forEach((tile) => {
    tile.addEventListener("click", () => {
      const [row, col] = tile.id.split("-");
      if (Board[row][col] == 0) {
        selectedTile = tile;
      } else {
      }
    });

    tile.addEventListener("keydown", (event) => {
      const key = event.key;

      if (selectedTile && /^[0-9]$/.test(key)) {
        selectedTile.innerText = key;
        event.preventDefault();
      }
    });
  });
}
