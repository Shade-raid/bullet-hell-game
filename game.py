<!DOCTYPE html>
<html>
<head>
  <title>Bullet Hell Game</title>
  <style>
    canvas {
      border: 1px solid black;
    }
  </style>
</head>
<body>
  <canvas id="gameCanvas" width="800" height="600"></canvas>

  <script>
    // Get the game canvas
    const canvas = document.getElementById("gameCanvas");
    const ctx = canvas.getContext("2d");

    // Define the player
    const player = {
      x: canvas.width / 2,
      y: canvas.height - 50,
      width: 30,
      height: 30,
      speed: 5
    };

    // Define the bullets
    const bullets = [];

    // Define the enemies
    const enemies = [];

    // Generate enemies
    function generateEnemies() {
      const enemy = {
        x: Math.random() * (canvas.width - 30),
        y: -30,
        width: 30,
        height: 30,
        speed: Math.random() * 2 + 1
      };
      enemies.push(enemy);
    }

    // Handle player movement
    function movePlayer(e) {
      if (e.key === "ArrowLeft" && player.x > 0) {
        player.x -= player.speed;
      } else if (e.key === "ArrowRight" && player.x + player.width < canvas.width) {
        player.x += player.speed;
      }
    }

    // Handle shooting bullets
    function shootBullet() {
      const bullet = {
        x: player.x + player.width / 2,
        y: player.y,
        width: 5,
        height: 10,
        speed: 7
      };
      bullets.push(bullet);
    }

    // Update game state
    function update() {
      // Move bullets
      bullets.forEach(bullet => {
        bullet.y -= bullet.speed;
      });

      // Move enemies
      enemies.forEach(enemy => {
        enemy.y += enemy.speed;
      });

      // Remove off-screen bullets
      bullets.forEach((bullet, bulletIndex) => {
        if (bullet.y < 0) {
          bullets.splice(bulletIndex, 1);
        }
      });

      // Remove collided bullets and enemies
      bullets.forEach((bullet, bulletIndex) => {
        enemies.forEach((enemy, enemyIndex) => {
          if (
            bullet.x < enemy.x + enemy.width &&
            bullet.x + bullet.width > enemy.x &&
            bullet.y < enemy.y + enemy.height &&
            bullet.y + bullet.height > enemy.y
          ) {
            bullets.splice(bulletIndex, 1);
            enemies.splice(enemyIndex, 1);
          }
        });
      });

      // Game over condition
      enemies.forEach(enemy => {
        if (
          player.x < enemy.x + enemy.width &&
          player.x + player.width > enemy.x &&
          player.y < enemy.y + enemy.height &&
          player.y + player.height > enemy.y
        ) {
          clearInterval(gameLoop);
          alert("Game Over!");
        }
      });
    }

    // Draw game objects on the canvas
    function draw() {
      ctx.clearRect(0, 0, canvas.width, canvas.height);

      // Draw player
      ctx.fillStyle = "red";
      ctx.fillRect(player.x, player.y, player.width, player.height);

      // Draw

    pygame.display.update()

# quit pygame
pygame.quit()
