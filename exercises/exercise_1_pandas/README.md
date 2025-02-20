# Theory questions - pandas

### a) Why could it be good to combine duckdb and pandas?
**Answer:**
- It could be good to combine DuckDB and pandas because DuckDB provides fast, SQL-based data operations, while pandas offers convenient data manipulation capabilities in Python. This combination allows users to perform efficient analytics on large datasets, running SQL queries in DuckDB for performance and using pandas for more complex data transformations and analysis in memory.

---

### b) How do you create a DataFrame in Pandas from a dictionary, a list of dictionaries, and a CSV file, json object?

**Answer:**
- From a **dictionary**:

```python
import pandas as pd
data = {'Column1': [1, 2, 3], 'Column2': [4, 5, 6]}
df = pd.DataFrame(data)´´´

**List of dictionaries**
´´´python
  data = [{'Column1': 1, 'Column2': 4}, {'Column1': 2, 'Column2': 5}, {'Column1': 3, 'Column2': 6}]
df = pd.DataFrame(data)´´´

**CSV file:**
´´´python
df = pd.read_csv('file.csv')```

**JSON object:**
```python
import json
json_data = '{"Column1": [1, 2, 3], "Column2": [4, 5, 6]}'
data = json.loads(json_data)
df = pd.DataFrame(data)
```
---

### c) What is the difference between `.loc[]` and `.iloc[]` for indexing in Pandas?

**Explanation:**
Both `.loc[]` and `.iloc[]` are used for indexing and selecting data from a DataFrame, but they differ in how they access data.

**Answer:**
- `.loc[]`: Label-based indexing. It selects rows and columns by their labels (column names or row indices).
```python
df.loc[0, 'Column1']  # Accesses the value at the first row, 'Column1' by label
```

**.iloc[]: Integer-location based indexing. It selects rows and columns by their integer positions (0-based index).**
```python
df.iloc[0, 0]  # Accesses the value at the first row, first column by position
```
---

### d) What is the purpose of the `.groupby()` method in Pandas? How is it used in data aggregation?

**Explanation:**
The `.groupby()` method in Pandas is used to split the data into groups based on one or more columns. After splitting, you can apply aggregation functions to each group for analysis. This is commonly used for summarizing data, such as calculating the mean, sum, or other statistics for each group.

**Answer:**
- The `.groupby()` method groups data based on column values and allows for applying aggregation functions like `sum()`, `mean()`, `count()`, etc., to perform operations on each group.
  
Example:
```python
df.groupby('Column1').mean()  # Groups the DataFrame by 'Column1' and computes the mean for each group
```
---

### e) How do you export a pandas DataFrame into a CSV file?

**Explanation:**
Pandas provides the `to_csv()` method to write a DataFrame to a CSV file. This method allows you to specify options like whether to include the index or control the delimiter.

**Answer:**
- You can use the `to_csv()` method to export a DataFrame into a CSV file. The `index=False` argument prevents the index from being written into the CSV file.

Example:
```python
df.to_csv('output.csv', index=False)  # Exports the DataFrame to 'output.csv' without the index
```
---

### f) How do you save a pandas DataFrame into a DuckDB database?

**Explanation:** DuckDB allows for efficient interaction with Pandas DataFrames and supports saving data into a DuckDB database directly. The duckdb package is used to save DataFrames as tables in the DuckDB database.

**Answer:**
- You can use the duckdb package to save a Pandas DataFrame into a DuckDB database. Here is an example of how to do it:

**Example:**
```python
import duckdb
import pandas as pd
# Assuming you have a DataFrame df
conn = duckdb.connect('my_database.duckdb')  # Connect to the DuckDB database (or create it)
conn.execute("CREATE TABLE my_table AS SELECT * FROM df")  # Save DataFrame to DuckDB as a table
conn.close()  # Close the connection
```






