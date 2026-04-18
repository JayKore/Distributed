# 🔹 EXP 1: Inter-Process Communication using Sockets

## 📌 Definition
Inter-Process Communication (IPC) using sockets enables communication between processes over a network using a client-server model.

## ⚙️ Approach Used
- TCP-based socket programming
- Server listens for connections
- Client connects and sends request
- Server processes and sends response

## ❓ Why this approach?
- TCP provides **reliable and ordered communication**
- Suitable for **client-server systems**
- Ensures no data loss

## ✅ Advantages
- Reliable data transfer
- Ordered delivery
- Works across networks

## ❌ Disadvantages
- Higher overhead than UDP
- Slower due to connection setup
- Not suitable for one-to-many communication

## ▶️ How to Run

### Terminal 1:
```bash
python server.py