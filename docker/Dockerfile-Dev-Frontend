# Base image
FROM node:18

# Set working directory in the container
WORKDIR /app

# Copy package.json and package-lock.json
COPY package.json ./
COPY package-lock.json ./

# Install dependencies
RUN /bin/bash -c "npm install"

# Copy the rest of your app's source code
COPY . .

RUN /bin/bash -c "npm run build"

# Expose the port
EXPOSE 3000

# Start the application
CMD [ "npm", "run", "start" ]