#!/usr/bin/env python3

import websockets
import asyncio

# Global Vars
IP_ADDR = "localhost"
PORT = "12345"
showInfo = 0


async def reboundMsg(websocket, path):
    msg = await websocket.recv()
    
    if showInfo:
        print("Incomming message is : " + msg)
        
    await websocket.send(msg)
    
start_server = websockets.serve(reboundMsg, IP_ADDR, PORT)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()















































"""
import socket

showInfo = 1

BYTES = 1024
PORT = 12345

sock = socket.socket()

if showInfo:
    print("Socket created")
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

sock.bind(('', PORT))
if showInfo:
    print("Socket is now binded")

sock.listen(5)



while True:
    if showInfo:
        print("Waiting for connection...")
        
    conn, addr = sock.accept()
    
    if showInfo:
        print("Connected to ", addr)
    
    msg = conn.recv(BYTES)
    
    if showInfo:
        print("Message is : ", msg)
        
    sock.send(msg)
    if showInfo:
        print("Message sent back")
    
    
conn.close()
"""