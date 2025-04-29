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

## Teaching Notes: Building the Maze Runner Game from Scratch

### **Objective**
Teach students how to build a web-based interactive game using Python, Flask, Docker, and modern web technologies. The project will demonstrate the use of microservices architecture, containerization, and frontend-backend integration.

---

### **Lesson Plan**

#### **1. Introduction to the Project**
- Explain the objective of the Maze Runner Game:
  - A player navigates through a randomly generated maze to reach the goal.
  - The game uses Flask for backend logic and HTML/CSS/JavaScript for the frontend.
  - Docker is used for containerization, and the project follows a microservices architecture.

#### **2. Setting Up the Environment**
- **Install Python**: Ensure Python 3.10 or later is installed.
- **Set Up a Virtual Environment**:
  ```bash
  python -m venv myvenv
  source myvenv/bin/activate  # On Windows: myvenv\Scripts\activate
  ```
- **Install Flask and Dependencies**:
  ```bash
  pip install flask flask-socketio
  ```

#### **3. Backend Development**
- **Game Logic Service**:
  - Create `game_logic.py` to handle maze generation, player movement, and game completion logic.
  - Implement random maze generation with validation to ensure a valid path exists.
  - Use Flask to expose APIs for maze generation and player movement.

- **User Interaction Service**:
  - Create `user_interaction.py` to manage user registration and login (optional for this project).

- **Real-Time Updates Service**:
  - Create `real_time_updates.py` to enable real-time updates using Flask-SocketIO (optional for this project).

#### **4. Frontend Development**
- **HTML Structure**:
  - Create `index.html` to serve as the main game interface.
  - Use a grid layout to represent the maze.

- **CSS Styling**:
  - Add `styles.css` for modern and responsive design.
  - Style the maze, player, and goal cells for better visual appeal.

- **JavaScript Logic**:
  - Add `script.js` to handle player movement and integrate with backend APIs.
  - Use `fetch` to dynamically load the maze and update the game state.

#### **5. Containerization with Docker**
- **Create Dockerfiles**:
  - Write separate Dockerfiles for each microservice (`game-logic`, `user-interaction`, `real-time-updates`).
  - Use Python base images and install necessary dependencies.

- **Set Up Docker Compose**:
  - Write `docker-compose.yml` to orchestrate the services.
  - Map ports for each service to the host machine.

#### **6. Running the Application**
- **Build and Start the Containers**:
  ```bash
  docker-compose up --build
  ```
- **Access the Game**:
  - Open [http://localhost:5000](http://localhost:5000) in a browser to play the game.

#### **7. Testing and Debugging**
- Test the maze generation to ensure a valid path exists.
- Test player movement and game completion logic.
- Debug any issues with containerization or API integration.

#### **8. Deployment (Optional)**
- Deploy the application to a cloud platform (e.g., AWS, Azure, or Google Cloud).
- Use Docker images for easy deployment.

---

### **Key Learning Outcomes**
1. Understand the basics of Flask and how to build RESTful APIs.
2. Learn how to integrate a frontend with a Flask backend.
3. Gain hands-on experience with Docker and Docker Compose.
4. Understand the principles of microservices architecture.
5. Learn how to validate and test a web application.

---

### **Additional Resources**
- [Flask Documentation](https://flask.palletsprojects.com/)
- [Docker Documentation](https://docs.docker.com/)
- [HTML/CSS/JavaScript Tutorials](https://developer.mozilla.org/)

---

### **Suggested Exercises for Students**
1. Modify the maze dimensions and test the game.
2. Add a scoring system to track the number of moves.
3. Implement user authentication in the `user_interaction` service.
4. Enhance the maze generation algorithm for more complex mazes.
5. Add real-time multiplayer functionality using Flask-SocketIO.