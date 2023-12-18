import streamlit as st
import socket
import threading
import json

# Constants
SERVER_HOST = '0.0.0.0'
SERVER_PORT = 5555

received_messages = []

def receive_messages():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((SERVER_HOST, SERVER_PORT))
    server_socket.listen(5)
    st.write(f"Server is listening on {SERVER_HOST}:{SERVER_PORT}")

    while True:
        client, addr = server_socket.accept()
        threading.Thread(target=handle_client, args=(client,)).start()

def handle_client(client):
    while True:
        data = client.recv(1024)
        if not data:
            break
        message = data.decode('utf-8')
        st.write(f"Received message: {message}")
        received_messages.append(message)

    client.close()

def main():
    st.title("Gmail Server")

    # Start a separate thread to receive messages
    threading.Thread(target=receive_messages).start()

    # Display the received messages in the Streamlit UI
    st.subheader("Received Messages")
    for i, message in enumerate(received_messages, 1):
        st.write(f"{i}. {message}")

if __name__ == "__main__":
    main()


