
---

# 📄 `exp3_group_comm/README.md`

```markdown
# 🔹 EXP 3: Group Communication using Multicast

## 📌 Definition
Group communication allows a single sender to transmit data to multiple receivers simultaneously using multicast.

## ⚙️ Approach Used
- UDP Multicast
- Sender sends message to multicast IP
- Receivers join group and receive messages

## ❓ Why this approach?
- Efficient one-to-many communication
- Reduces network load
- Suitable for real-time systems

## ✅ Advantages
- Bandwidth efficient
- Scalable
- No need for multiple transmissions

## ❌ Disadvantages
- No guarantee of delivery (UDP)
- No ordering of messages
- Requires network support

## ▶️ How to Run

### Step 1: Run multiple receivers
```bash
python receiver.py