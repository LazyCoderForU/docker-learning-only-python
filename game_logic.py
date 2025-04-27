import random
from flask import Flask, jsonify, request, render_template

app = Flask(__name__)

# Serve the game interface
@app.route('/')
def index():
    return render_template('index.html')

def is_valid_maze(maze):
    rows, cols = len(maze), len(maze[0])
    start, goal = (0, 0), (rows - 1, cols - 1)

    def dfs(x, y, visited):
        if (x, y) == goal:
            return True
        visited.add((x, y))
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < rows and 0 <= ny < cols and maze[ny][nx] == 0 and (nx, ny) not in visited:
                if dfs(nx, ny, visited):
                    return True
        return False

    return dfs(start[0], start[1], set())

# Updated endpoint for maze generation with randomization
@app.route('/generate-maze', methods=['GET'])
def generate_maze():
    rows, cols = 10, 10  # Maze dimensions
    while True:
        maze = [[random.choice([0, 1]) for _ in range(cols)] for _ in range(rows)]
        maze[0][0] = 0  # Ensure starting point is open
        maze[rows - 1][cols - 1] = 0  # Ensure finish point is open
        if is_valid_maze(maze):
            break
    return jsonify({"maze": maze})

# Updated endpoint for player movement with finish state check
@app.route('/move', methods=['POST'])
def move_player():
    data = request.json
    position = data.get("position")
    finish_position = [9, 9]  # Finish point

    if position == finish_position:
        return jsonify({"status": "Game completed!", "position": position, "finished": True})

    return jsonify({"status": "Player moved", "position": position, "finished": False})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)