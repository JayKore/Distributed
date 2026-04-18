
---

# 📄 `exp6_mutual_exclusion/README.md`

```markdown id="exp6readme"
# 🔹 EXP 6: Mutual Exclusion (Token Ring & Ricart-Agrawala)

## 📌 Definition
Mutual exclusion ensures that only one process accesses the critical section at a time, preventing conflicts.

---

## ⚙️ Algorithms Implemented

### 1. Token Ring Algorithm
- A token circulates among processes
- Only token holder can enter critical section

### 2. Ricart-Agrawala Algorithm
- Process sends REQUEST to all others
- Enters critical section after receiving all REPLY messages
- Uses timestamps for ordering

---

## ❓ Why these approaches?
- Prevent simultaneous access to shared resources
- Maintain data consistency
- Avoid race conditions

---

## ✅ Advantages

### Token Ring
- No starvation
- Simple implementation
- Low message overhead

### Ricart-Agrawala
- Fully distributed (no token needed)
- Fair ordering using timestamps

---

## ❌ Disadvantages

### Token Ring
- Token loss problem
- Difficult recovery

### Ricart-Agrawala
- High message overhead
- Depends on communication reliability

---

## ▶️ How to Run

```bash
python token_ring.py
python ricart_agrawala.py