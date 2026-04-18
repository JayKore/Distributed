
---

# 📄 `exp2_rpc/README.md`

```markdown
# 🔹 EXP 2: Remote Procedure Call (RPC)

## 📌 Definition
Remote Procedure Call (RPC) allows a client to execute a function on a remote server as if it were a local function call.

## ⚙️ Approach Used
- Socket-based RPC using `pickle` for serialization
- Client sends function name + arguments
- Server executes function and returns result

## ❓ Why this approach?
- Simplifies distributed programming
- Hides networking complexity
- Makes remote calls look like local calls

## ✅ Advantages
- Easy to use
- Promotes modular design
- Code reusability

## ❌ Disadvantages
- Serialization overhead
- Network latency
- Harder debugging

## ▶️ How to Run

```bash
python your_rpc_file.py