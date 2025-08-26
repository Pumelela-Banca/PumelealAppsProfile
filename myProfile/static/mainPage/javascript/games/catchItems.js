// Catch Items game

const canvas = document.getElementById("gameCanvas");
const ctx = canvas.getContext("2d");

let basket = {
    x: canvas.width / 2 - 50,
    y: canvas.height - 30,
    width: 100,
    height: 20,
    color: "#7e1a1aff"
};

let items = [];
let itemFrequency = 1500; // milliseconds
let gameInterval;
let isGameOver = false;

function startGame() {
    document.getElementById("score").innerText = "Score: 0";
    items = [];
    score = 0;
    isGameOver = false;
    gameInterval = setInterval(gameLoop, 1000 / 60);
    spawnItem();
}

function spawnItem() {
    let item = {
        x: Math.random() * (canvas.width - 30),
        y: 0,
        width: 30,
        height: 30,
        color: "#ff0000"
    };
    items.push(item);
    setTimeout(spawnItem, itemFrequency);
}

function gameLoop() {
    if (isGameOver) return;

    ctx.clearRect(0, 0, canvas.width, canvas.height);
    drawBasket();
    drawItems();
    updateItems();
    checkCollisions();
}

function drawBasket() {
    ctx.fillStyle = basket.color;
    ctx.fillRect(basket.x, basket.y, basket.width, basket.height);
}

function drawItems() {
    items.forEach(item => {
        ctx.fillStyle = item.color;
        ctx.fillRect(item.x, item.y, item.width, item.height);
    });
}

function updateItems() {
    items.forEach(item => {
        item.y += 2; // fall speed
    });
    items = items.filter(item => item.y < canvas.height);
}

function checkCollisions() {
    items.forEach(item => {
        if (item.y + item.height > basket.y && item.x + item.width > basket.x && item.x < basket.x + basket.width) {
            score++;
            document.getElementById("score").innerText = "Score: " + score;
            items = items.filter(i => i !== item);
        }
    });
}

function endGame() {
    isGameOver = true;
    clearInterval(gameInterval);
    alert("Game Over! Your score was: " + score);
}

document.addEventListener("mousemove", (event) => {
    basket.x = event.clientX - canvas.offsetLeft - basket.width / 2;
});

document.getElementById("startButton").addEventListener("click", startGame);
