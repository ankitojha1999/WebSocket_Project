# WebSocket Client-Server Application

## Project Overview

This project demonstrates a simple WebSocket-based real-time communication system between a client (HTML + JavaScript) and a server (Python). The client sends 10,000 messages to the WebSocket server, which modifies each message by appending a random number. The server then returns the modified messages to the client, which are displayed on the UI in real-time.

## Features

- **Full-duplex communication**: Both the client and the server can send and receive messages simultaneously.
- **Real-time interaction**: Messages are sent and received instantly over a persistent WebSocket connection.
- **Message modification**: The server appends a random number to each message it receives before sending it back to the client.
- **Display of server responses**: All server responses are displayed in a scrollable UI on the client side.
- **Send 10,000 messages**: The client sends 10,000 messages to the server in a loop, and all responses are received and displayed without dropping any messages.

## Technologies Used

- **Backend (Server)**: Python 3.12, `websockets` library for handling WebSocket connections.
- **Frontend (Client)**: HTML, JavaScript for sending and receiving WebSocket messages.
- **WebSocket**: Real-time full-duplex communication protocol.

## Prerequisites

- **Python 3.6+** installed on your machine.
- **pip** for managing Python packages.
- **websockets** library in Python. Install it using the following command:

  ```bash
  pip install websockets
