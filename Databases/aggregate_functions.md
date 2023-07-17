# Aggregate Functions in SQL

## Using the World Database

### 1. How many countries are there in the world?

```sql
SELECT COUNT(*) FROM country;
```

### 2. What is the total population of the world?

```sql
SELECT SUM(population) FROM country;
```

### 3. What is the total poplulation of each region?

```sql
SELECT Continent, SUM(population) FROM country GROUP BY Continent ORDER BY SUM(population) DESC;
```

### 4. What is the total population of each country in the world?

```sql
SELECT Name, population FROM country ORDER BY population DESC;
```

### 5. Order countries from highest to lowest surface area

```sql
SELECT name, surfacearea FROM country ORDER BY surfacearea DESC;
```