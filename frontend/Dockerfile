# Base image
FROM node:18.16.0-alpine3.17

# Set working directory in the container
WORKDIR /app

# Copy package.json and package-lock.json
COPY package*.json ./

# Install dependencies
RUN npm install

# Copy the rest of your app's source code
COPY . .

# Expose the port
EXPOSE 3000

# Start the application
CMD [ "npm", "run", "dev" ]