# data-platforms-freya
Learning data platforms

## Glossories


| terminology          | explanation                                                                 |
| -------------------- | --------------------------------------------------------------------------- |
| assign               | Att ge ett värde till en variabel med hjälp av `=`. T.ex. `x = 10` betyder att variabeln `x` nu har värdet 10. |
| logical error        | Ett fel i programlogiken där programmet körs utan att krascha, men ger felaktiga resultat. |
| handling error       | Att hantera fel som kan uppstå i programmet, t.ex. genom att använda `try` och `except` för att undvika krascher. |
| indexing             | Att hämta ett specifikt värde från en lista, tuple eller sträng med hjälp av dess position (index). T.ex. `my_list[0]` ger det första värdet. |
| slicing              | Att ta en del av en lista, tuple eller sträng. T.ex. `my_list[1:4]` ger värdena från position 1 till 3. |
| iterable             | Ett objekt som kan loopas igenom, som en lista, sträng eller range. T.ex. kan du loopa igenom `for item in my_list`. |
| iterate over         | Att gå igenom alla värden i en lista, sträng eller liknande med hjälp av en loop. T.ex. `for item in my_list:`. |
| list comprehension   | Ett kort sätt att skapa listor i en rad. T.ex. `[x*2 for x in range(5)]` skapar en lista där alla tal multipliceras med 2. |
| collections          | En samling specialfunktioner i Python för att hantera listor, räkna saker och mycket mer. |
| tuples               | En samling värden som liknar en lista, men som inte kan ändras efter att de skapats. T.ex. `my_tuple = (1, 2, 3)`. |
| \_\_repr\_\_         | En speciell funktion i Python som beskriver hur ett objekt ska visas i text för utvecklare. |
| dunder methods       | Kallas också "dubbel-understreck-metoder", som t.ex. `__init__` eller `__repr__`. Dessa används för speciella funktioner i Python. |
| pythonic             | Ett sätt att skriva kod som är typiskt för Python – tydlig, enkel och lätt att förstå. |
| idiomatic            | Ett sätt att skriva kod som följer de bästa vanliga sätten för ett visst programmeringsspråk. |
| DRY                  | Står för "Don't Repeat Yourself". Det betyder att du ska undvika att skriva samma kod flera gånger. |
| spaghetti code       | Kod som är svår att läsa och förstå för att den är rörig och dåligt organiserad. |
| keyword arguments    | När du skickar ett argument till en funktion med ett namn. T.ex. `print(name="Alice")`. |
| positional arguments | När du skickar ett argument till en funktion baserat på ordningen. T.ex. `print("Alice", 25)`. |
| \*args               | Används i en funktion för att ta emot många värden utan att skriva ut dem enskilt. T.ex. `def func(*args):`. |
| \*\*kwargs           | Används i en funktion för att ta emot många nyckelord-argument, t.ex. `def func(**kwargs):`. |
| unpacking list       | Att dela upp en lista eller tuple i flera delar. T.ex. `a, b = [1, 2]` ger `a = 1` och `b = 2`. |
| return statement     | När en funktion skickar tillbaka ett värde. T.ex. `def add(x, y): return x + y`. |
| ternary operator     | Ett kort sätt att skriva en if-sats. T.ex. `x = 10 if condition else 5` ger `x = 10` om villkoret är sant, annars `5`. |
| json                 | Ett sätt att lagra och skicka data som ser ut som text, vanligt inom webbutveckling. T.ex. `{"name": "Alice", "age": 25}`. |



---
# 0.Theory questions

### a) What are the fundamental data types in Python?  
The fundamental data types in Python are:  
- **int**: Whole numbers, e.g., `10`, `-5`.  
- **float**: Decimal numbers, e.g., `3.14`, `-2.5`.  
- **str**: Text or string, e.g., `"hello"`, `'Python'`.  
- **bool**: Boolean values, `True` or `False`.  
- **NoneType**: Represents the absence of a value, `None`.

---

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

