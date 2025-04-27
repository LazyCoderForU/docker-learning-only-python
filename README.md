# Maze Runner Game

## Overview
The Maze Runner Game is an interactive web-based game where players navigate through a randomly generated maze to reach the goal. The game is built using a microservices architecture with Flask for the backend and a modern web interface for the frontend.

## Features
- **Random Maze Generation**: Each maze is randomly generated and validated to ensure there is a valid path from the start to the goal.
- **Interactive Gameplay**: Players can use arrow keys or on-screen buttons to navigate the maze.
- **Real-Time Feedback**: The game provides feedback for invalid moves and congratulates the player upon reaching the goal.
- **Modern UI**: The game features a clean and responsive design for an enhanced user experience.

## Architecture
The application is designed using a microservices architecture with the following components:
1. **Game Logic Service**: Handles maze generation, player movement, and game completion logic.
2. **User Interaction Service**: Manages user registration and login (future scope).
3. **Real-Time Updates Service**: Enables real-time updates for multiplayer functionality (future scope).

## Technologies Used
- **Backend**: Flask, Flask-SocketIO
- **Frontend**: HTML, CSS, JavaScript
- **Containerization**: Docker, Docker Compose
- **Version Control**: Git

## Setup and Run Instructions
1. **Clone the Repository**:
   ```bash
   git clone <repository-url>
   cd <repository-folder>
   ```

2. **Build and Start the Application**:
   ```bash
   docker-compose up --build
   ```

3. **Access the Game**:
   Open your browser and navigate to [http://localhost:5000](http://localhost:5000).

4. **Play the Game**:
   - Use arrow keys or on-screen buttons to navigate the maze.
   - Reach the goal (`G`) to complete the game.

5. **Stop the Application**:
   Press `Ctrl+C` in the terminal and run:
   ```bash
   docker-compose down
   ```

## What Has Been Done
1. **Backend Development**:
   - Created the `game-logic` service to handle maze generation and player movement.
   - Implemented random maze generation with validation to ensure a valid path exists.
   - Added logic to detect game completion when the player reaches the goal.

2. **Frontend Development**:
   - Designed a modern and responsive web interface using HTML, CSS, and JavaScript.
   - Added visual indicators for the player (`P`) and goal (`G`) cells.
   - Integrated the frontend with the backend for dynamic maze generation and player movement.

3. **Containerization**:
   - Created Dockerfiles for each microservice.
   - Configured `docker-compose.yml` to orchestrate the services.

4. **Validation and Testing**:
   - Ensured that each generated maze has a valid path to the goal.
   - Tested the game for smooth gameplay and user experience.

## Future Enhancements
- Add user authentication and progress tracking.
- Implement real-time multiplayer functionality.
- Enhance the maze generation algorithm for larger and more complex mazes.
- Deploy the application to a cloud platform for public access.

## Folder Structure
```
.
├── docker-compose.yml
├── Dockerfile.game_logic
├── Dockerfile.real_time_updates
├── Dockerfile.user_interaction
├── game_logic.py
├── real_time_updates.py
├── user_interaction.py
├── templates/
│   ├── index.html
├── myvenv/
│   ├── Scripts/
│   ├── Lib/
│   ├── Include/
```

## How to Contribute
1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Commit your changes and push them to your fork.
4. Submit a pull request with a detailed description of your changes.