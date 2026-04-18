# 🎯 Distributed Computing Viva Questions (All Experiments)

This document contains commonly asked viva questions with concise answers for quick revision.

---

# 🔹 EXP 1: IPC using Sockets

### ❓ What is IPC?
Communication between processes.

### ❓ What is a socket?
Endpoint for communication between two processes.

### ❓ TCP vs UDP?
- TCP → Reliable, ordered  
- UDP → Fast, unreliable  

### ❓ Why TCP used here?
Ensures reliable data transfer with no loss.

### ❓ What is bind()?
Assigns IP and port to socket.

### ❓ What is listen()?
Waits for incoming connections.

### ❓ What is accept()?
Establishes connection with client.

### ❓ Real-world use?
Web apps, chat systems.

---

# 🔹 EXP 2: RPC

### ❓ What is RPC?
Calling a function on a remote system.

### ❓ RPC vs RMI?
- RPC → Function-based  
- RMI → Object-based  

### ❓ What is serialization?
Converting data into transferable format.

### ❓ What is pickle?
Python module used for serialization.

### ❓ Why RPC?
Simplifies distributed programming.

### ❓ What is marshalling?
Packaging data for transmission.

### ❓ Real-world use?
Microservices, APIs.

---

# 🔹 EXP 3: Group Communication (Multicast)

### ❓ What is multicast?
One-to-many communication.

### ❓ Why UDP used?
Faster, no connection overhead.

### ❓ Multicast vs Broadcast?
- Multicast → specific group  
- Broadcast → all devices  

### ❓ What is TTL?
Limits packet travel distance.

### ❓ Multicast IP range?
224.0.0.0 – 239.255.255.255

### ❓ Real-world use?
Streaming, gaming.

---

# 🔹 EXP 5: Election Algorithms

### ❓ What is election algorithm?
Selects coordinator in distributed system.

### ❓ Bully algorithm?
Highest ID becomes leader.

### ❓ Ring algorithm?
Message circulates in ring.

### ❓ Bully vs Ring?
- Bully → direct, faster  
- Ring → structured, slower  

### ❓ When election triggered?
Coordinator failure.

### ❓ Why highest ID?
Assumed highest priority.

---

# 🔹 EXP 6: Mutual Exclusion

### ❓ What is mutual exclusion?
Only one process enters critical section.

### ❓ What is critical section?
Shared resource access area.

### ❓ Token Ring?
Token gives permission to enter CS.

### ❓ Ricart-Agrawala?
Requests permission from all processes.

### ❓ Why timestamps?
Ensure ordering of requests.

### ❓ What is starvation?
Process never gets access.

### ❓ How prevented?
Fair scheduling (token/timestamps).

---

# 🔹 EXP 8: Task Assignment

### ❓ What is task assignment?
Assigning tasks to processors.

### ❓ Goal?
Minimize execution cost.

### ❓ Input?
Cost matrix.

### ❓ Approach used?
Greedy method.

### ❓ Is it optimal?
Not always (local optimum only).

### ❓ Real-world use?
Scheduling, load balancing.

---

# 🧠 Rapid Revision Tips

- TCP → reliable  
- RPC → remote function call  
- Multicast → one-to-many  
- Bully → highest ID wins  
- Token → permission passing  
- Greedy → minimum per row  

---

# ⚡ Final Viva Hack

If stuck, say:
> “This approach ensures efficiency, reliability, and proper coordination in distributed systems.”