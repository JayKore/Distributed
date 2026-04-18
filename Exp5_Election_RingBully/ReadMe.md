# 🔹 EXP 5: Election Algorithms (Bully & Ring)

## 📌 Definition
Election algorithms are used in distributed systems to select a coordinator (leader) among multiple processes.

---

## ⚙️ Algorithms Implemented

### 1. Bully Algorithm
- Processes have unique IDs
- A process detects coordinator failure
- Sends election messages to higher-ID processes
- Highest alive process becomes coordinator

### 2. Ring Algorithm
- Processes are arranged in a logical ring
- Election message circulates through the ring
- Highest ID in the ring becomes coordinator

---

## ❓ Why these approaches?
- Needed for **leader selection in distributed systems**
- Ensures system continues functioning after failures
- Avoids centralized control

---

## ✅ Advantages

### Bully Algorithm
- Fast election
- Simple logic

### Ring Algorithm
- Lower message conflict
- Structured communication

---

## ❌ Disadvantages

### Bully Algorithm
- High message overhead
- Not efficient for large systems

### Ring Algorithm
- Slower (message travels full ring)
- Failure handling is complex

---

## ▶️ How to Run

```bash
python bully.py
python ring.py