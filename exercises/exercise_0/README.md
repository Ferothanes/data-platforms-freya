# 0.Theory questions - python

### a) What are the fundamental data types in Python?

The fundamental data types in Python are:  
- **int**: Whole numbers, e.g., `10`, `-5`.  
- **float**: Decimal numbers, e.g., `3.14`, `-2.5`.  
- **str**: Text or string, e.g., `"hello"`, `'Python'`.  
- **bool**: Boolean values, `True` or `False`.  
- **NoneType**: Represents the absence of a value, `None`.

### b) What is the difference between a list and a tuple in Python?  
- **List**:  
  - Mutable (can be changed).  
  - Defined using square brackets, e.g., `[1, 2, 3]`.  
  - Used when the data may need to be modified.  

- **Tuple**:  
  - Immutable (cannot be changed after creation).  
  - Defined using parentheses, e.g., `(1, 2, 3)`.  
  - Used when the data should remain constant.

---

### c) How does Python handle mutable and immutable data types?  
- **Mutable data types**: Can be changed after creation. Examples: `list`, `dict`, `set`.  
- **Immutable data types**: Cannot be changed after creation. Examples: `int`, `float`, `str`, `tuple`. 
 
- Python handles them differently in memory:  
  - Mutable types share references, so changes affect all references.  
  - Immutable types create new objects when modified.

---

### d) Explain the difference between for and while loops and when to use one or the other.  
- **for loop**:  
  - Iterates over a sequence (like a list or range).  
  - Use when you know the number of iterations in advance.  
  - Example:  
    ```python
    for i in range(5):
        print(i)  # Prints 0 to 4
    ```

- **while loop**:  
  - Repeats as long as a condition is true.  
  - Use when you don’t know in advance how many iterations are needed.  
  - Example:  
    ```python
    x = 0
    while x < 5:
        print(x)
        x += 1
    ```

---

### e) How do you read a file line-by-line in Python?  
You can use the `with` statement and `open()` function to read a file line-by-line:  
```python
with open("file.txt", "r") as file:
    for line in file:
        print(line.strip())  # Removes trailing newline
```

---

### f) What is a context manager and why would you need to use it?  
A **context manager** is a way to manage resources (like files) that need setup and cleanup.  
- It’s used with the `with` statement to ensure resources are properly released.  
- Example:  
  ```python
  with open("file.txt", "r") as file:
      data = file.read()
  # File is automatically closed here
  ´´´

---

### g) Explain the difference between try, except, else, and finally.  
- **try**: Blocket där du skriver kod som kan orsaka ett fel.  
- **except**: Blocket som körs om ett fel uppstår i `try`-blocket.  
- **else**: Blocket som körs om inget fel inträffar i `try`-blocket.  
- **finally**: Blocket som alltid körs, oavsett om ett fel uppstår eller inte.  

Exempel:  
```python
try:
    x = 10 / 2  # Kod som kan orsaka ett fel
except ZeroDivisionError:
    print("Kan inte dela med noll!")  # Körs om ett ZeroDivisionError inträffar
else:
    print("Divisionen lyckades!")  # Körs om inget fel inträffar
finally:
    print("Detta körs alltid, oavsett vad.")  # Körs alltid
```

---

### h) What is the difference between ETL and ELT?  
- **ETL (Extract, Transform, Load)**:  
  - Data hämtas från källor (**Extract**), omvandlas för att passa det mål där den ska lagras (**Transform**), och laddas sedan in i databasen eller datalagret (**Load**).  
  - Vanligt när transformationer behövs innan datan lagras.  

- **ELT (Extract, Load, Transform)**:  
  - Data hämtas från källor (**Extract**), laddas först in i databasen eller datalagret (**Load**), och omvandlas sedan där (**Transform**).  
  - Vanligt i moderna dataplattformar som kan hantera stora datamängder och komplexa transformationer direkt i databasen.  

**Sammanfattning**:  
- **ETL**: Transformation sker innan laddning.  
- **ELT**: Transformation sker efter laddning, i databasen.

---

### i) Differentiate between batch processing and streaming processing.  
- **Batch processing**:  
  - Bearbetar stora mängder data i omgångar (batcher) vid schemalagda intervaller.  
  - Används när du kan vänta på att bearbeta data på en senare tidpunkt, som vid att generera en daglig rapport.  

- **Streaming processing**:  
  - Bearbetar data i realtid så fort den kommer in.  
  - Används när data behöver bearbetas omedelbart, som vid att övervaka live-aktiviteter eller analysera strömmande data (t.ex. aktiekurser eller sociala medieinlägg).

**Sammanfattning**:  
- **Batch processing**: Bearbetning av stora datamängder på förbestämda tider.  
- **Streaming processing**: Bearbetning av data i realtid, så snart den anländer.

---

### j) What is a data platform?  
En **data platform** är ett system som samlar, lagrar, bearbetar och analyserar data.  
- Den består av verktyg och teknologier för att hantera databaser, dataflöden, och analyser.  
- Målet är att ge användare och företag möjlighet att fatta datadrivna beslut snabbt och effektivt.  
- Exempel på data plattformar: Snowflake, Google BigQuery, eller AWS Data Lake.  

**Sammanfattning**:  
- En data platform hjälper företag att hantera och analysera data från olika källor för att fatta informerade beslut.