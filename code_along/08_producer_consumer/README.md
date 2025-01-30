![alt text](<images/Screenshot 2025-01-28 162335.png>)

**Behövs inte consumeras direkt eftersom det ligger sparat i topics - "Consume at your own pace"**
![alt text](<images/Screenshot 2025-01-28 161746.png>)

**Update inventory & leave order information**
![alt text](<images/Screenshot 2025-01-28 162654.png>)

python´´´
{
    "event_type" : "order_placed",
    "order_id" : "301", 
    "customer_id" : "101",
    "total_amount" : "2090.9",
    "time_stamp" : "2025-01-26T14:20:00Z"
}
´´´

![alt text](<images/Screenshot 2025-01-28 163531.png>)

---

**Lazy Evaluation:** means delaying the execution of a computation until its result is actually needed.

**Key Benefits:**

✅ Efficiency – Avoids unnecessary calculations.
✅ Performance – Saves memory by computing values only when required.
✅ Optimized Execution – Works well with large datasets and infinite sequences.


**Eager Evaluation:** means executing a computation immediately, as soon as the expression is encountered.

**Key Characteristics:**

✅ Immediate execution – Computations happen right away.
✅ Uses more memory – Stores results even if they aren’t needed.
✅ Good for simple tasks – Avoids managing delayed execution.