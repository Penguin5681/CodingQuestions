const allRows = document.querySelectorAll("#inventory tbody tr");

let outOfStock = 0;
let lowStock = 0;

allRows.forEach((row) => {
    const stockCell = row.cells[2];
    const stock = Number(stockCell.textContent.trim());
    if (stock === 0) {
        row.classList.add("out-of-stock");
        stockCell.textContent = "Out of stock";
        outOfStock++;
    } else if (stock >= 1 && stock <= 5) {
        row.classList.add("low-stock");
        stockCell.textContent = "Low on stock";
        lowStock++;
    }
});

document.getElementById("summary").textContent =
  `${outOfStock} out of stock, ${lowStock} low on stock`;