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

### 6. Find the highest GNP in Asia

```sql
SELECT Name, GNP FROM country WHERE Continent = 'Asia' ORDER BY GNP DESC LIMIT 1;

```

### 7. Find all the cities in the UK

```sql

SELECT city.name, country.Name from city LEFT JOIN country on city.CountryCode = country.code WHERE country.Name = "United Kingdom";

```

### 8
