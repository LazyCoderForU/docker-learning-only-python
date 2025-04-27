# Docker Learning Notes with Code, Syntax, and Explanations

---

## **1. Dockerfile**

### **Syntax**
A `Dockerfile` is a script with instructions to build a Docker image. Each line specifies a step in the build process.

### **Example: Python App Dockerfile**
```dockerfile
# filepath: c:\Users\pubg3\OneDrive\Desktop\Projects\git repos\docker learning only python\Dockerfile
# Use a lightweight Python image based on Alpine Linux
FROM python:3.10-alpine

# Set the working directory in the container
WORKDIR /app

# Copy the application code into the container
COPY app.py .

# Install required Python libraries
RUN pip install requests

# Command to run the application
CMD ["python", "app.py"]
```

### **Explanation**
1. **`FROM python:3.10-alpine`**:
   - Specifies the base image (`python:3.10-alpine`), which is a lightweight Python image.
2. **`WORKDIR /app`**:
   - Sets the working directory inside the container to `/app`.
3. **`COPY app.py .`**:
   - Copies the `app.py` file from the host to the `/app` directory in the container.
4. **`RUN pip install requests`**:
   - Installs the `requests` library inside the container.
5. **`CMD ["python", "app.py"]`**:
   - Specifies the command to run when the container starts.

---

## **2. Docker Compose**

### **Syntax**
A `docker-compose.yml` file defines multiple services, networks, and volumes for a multi-container application.

### **Example: Flask API and Python App**
```dockercompose
# filepath: c:\Users\pubg3\OneDrive\Desktop\Projects\git repos\docker learning only python\docker-compose.yml
services:
  flask-service:
    container_name: flask-service-new
    build:
      context: .
      dockerfile: Dockerfile-flask
    ports:
      - "5000:5000"
    networks:
      - microservices-network

  python-app:
    build:
      context: .
      dockerfile: Dockerfile
    container_name: python-app
    depends_on:
      - flask-service
    networks:
      - microservices-network

networks:
  microservices-network:
    driver: bridge
```

### **Explanation**
1. **`services`**:
   - Defines the services (containers) in the application.
2. **`flask-service`**:
   - Runs the Flask API.
   - **`container_name`**: Names the container `flask-service-new`.
   - **`build`**: Specifies the build context and Dockerfile for the service.
   - **`ports`**: Maps port `5000` on the host to port `5000` in the container.
3. **`python-app`**:
   - Runs the Python app.
   - **`depends_on`**: Ensures the Flask service starts before the Python app.
4. **`networks`**:
   - Connects both services to the `microservices-network`.

---

## **3. Flask API**

### **Syntax**
A Flask API is a Python application that exposes endpoints for other services to consume.

### **Example: Flask API**
```python
# filepath: c:\Users\pubg3\OneDrive\Desktop\Projects\git repos\docker learning only python\flask_api.py
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/api/message', methods=['GET'])
def get_message():
    return jsonify({"message": "Hello from Flask API!"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
```

### **Explanation**
1. **`Flask`**:
   - A Python framework for building web APIs.
2. **`@app.route('/api/message', methods=['GET'])`**:
   - Defines an endpoint `/api/message` that responds to GET requests.
3. **`app.run(host='0.0.0.0', port=5000)`**:
   - Starts the Flask server, listening on all network interfaces (`0.0.0.0`) at port `5000`.

---

## **4. Python App**

### **Syntax**
A Python app that makes HTTP requests to the Flask API.

### **Example: Python App**
```python
# filepath: c:\Users\pubg3\OneDrive\Desktop\Projects\git repos\docker learning only python\app.py
import requests

# Call the Flask API
response = requests.get("http://flask-service:5000/api/message")
if response.status_code == 200:
    print("Response from Flask API:", response.json()["message"])
else:
    print("Failed to connect to Flask API")
```

### **Explanation**
1. **`requests.get`**:
   - Sends an HTTP GET request to the Flask API.
2. **`response.status_code`**:
   - Checks the HTTP status code of the response.
3. **`response.json()`**:
   - Parses the JSON response from the API.

---

## **5. Deploying WordPress Using Docker Compose**

### **Syntax**
A `docker-compose.yml` file to deploy WordPress and MySQL.

### **Example: WordPress Deployment**
```dockercompose
# filepath: c:\Users\pubg3\OneDrive\Desktop\Projects\git repos\docker learning only python\docker-compose-wordpress.yml
services:
  wordpress:
    image: wordpress:latest
    container_name: wordpress
    ports:
      - "8080:80"
    environment:
      WORDPRESS_DB_HOST: db
      WORDPRESS_DB_USER: wordpress
      WORDPRESS_DB_PASSWORD: wordpress
      WORDPRESS_DB_NAME: wordpress
    networks:
      - wordpress-network
    depends_on:
      - db

  db:
    image: mysql:5.7
    container_name: wordpress-db
    environment:
      MYSQL_ROOT_PASSWORD: rootpassword
      MYSQL_DATABASE: wordpress
      MYSQL_USER: wordpress
      MYSQL_PASSWORD: wordpress
    volumes:
      - db_data:/var/lib/mysql
    networks:
      - wordpress-network

networks:
  wordpress-network:
    driver: bridge

volumes:
  db_data:
```

### **Explanation**
1. **`wordpress`**:
   - Runs the WordPress application.
   - Maps port `8080` on the host to port `80` in the container.
   - Connects to the MySQL database using environment variables.
2. **`db`**:
   - Runs the MySQL database.
   - Uses a volume (`db_data`) to persist data.

---

## **6. Commands and Parameters**

### **Docker Commands**
1. **Build an Image**:
   ```bash
   docker build -t <image-name> .
   ```
   - `-t`: Tags the image with a name.

2. **Run a Container**:
   ```bash
   docker run -it --rm <image-name>
   ```
   - `-it`: Runs interactively with a terminal.
   - `--rm`: Removes the container after it stops.

3. **Create a Volume**:
   ```bash
   docker volume create <volume-name>
   ```

4. **Start Services with Docker Compose**:
   ```bash
   docker-compose up --build
   ```
   - `--build`: Rebuilds the images before starting.

5. **Stop Services with Docker Compose**:
   ```bash
   docker-compose down
   ```

---

Let me know if you'd like further clarification or additional examples!