# World Challenges

## 1. Using COUNT, get the number of cities in the USA

```sql

SELECT COUNT(NAME) FROM city WHERE countrycode = "USA";

```

## 2. Find out the population and life expectancy for people in Argentina

```sql

SELECT Name, Population, LifeExpectancy from country WHERE Name="Argentina";


```

## 3. Using IS NOT NULL, ORDER BY, and LIMIT, which country has the highest life expectancy?

```sql

SELECT Name, LifeExpectancy FROM country WHERE LifeExpectancy IS NOT NULL ORDER BY LifeExpectancy DESC LIMIT 1;

```

## 4. Using JOIN ... ON, find the capital city of Spain

```sql

SELECT city.Name FROM city LEFT JOIN country ON city.ID = country.Capital WHERE country.name = "Spain";

```

## 5. Using JOIN ... ON, list all the languages spoken in the Southeast Asia region

```sql

SELECT country.Name, countrylanguage.language FROM country LEFT JOIN countrylanguage on country.Code = countrylanguage.CountryCode WHERE country.Name IN(SELECT Name from country WHERE region="Southeast Asia");

```

## 6. Using a single query, list 25 cities around the world that start with the letter F

```sql

SELECT Name from city WHERE Name LIKE 'F%' LIMIT 25;

```

## 7. Using COUNT and JOIN ... ON, get the number of cities in China

```sql

SELECT COUNT(city.Name) FROM city LEFT JOIN country ON country.code = city.CountryCode WHERE country.name="China";

```

## 8. Using IS NOT NULL, ORDER BY, and LIMIT, which country has the lowest population? Discard non-zero populations

```sql

SELECT Name, Population from country WHERE Population = (SELECT MIN(Population) FROM country WHERE Population IS NOT NULL AND Population <> 0 ORDER BY Population DESC LIMIT 1);

```

### Although, this won't work if there are multiple countries with the same population

## 9. Using aggregate functions, return the number of countries the database contains

```sql

SELECT COUNT(Name) FROM country;


```

## 10. What are the top ten largest countries by area?

```sql

SELECT Name, SurfaceArea from country ORDER BY SurfaceArea DESC LIMIT 10;

```

## 11. List the five largest cities by population in Japan

```sql

SELECT city.Name, city.Population from city LEFT JOIN country ON city.CountryCode = country.Code WHERE country.Name="Japan" ORDER BY city.Population DESC LIMIT 5;

```

## 12. List the names and country codes of every country with Elizabeth II as its Head of State. You will need to fix the mistake first

```sql

SELECT Name, HeadOfState from country WHERE HeadOfState="Elisabeth II";

```

## 13. List the top ten countries with the smallest population-to-area ratio. Discard any countries with a ratio of 0

```sql

SELECT Name, (Population / SurfaceArea) as Density FROM country WHERE (Population / SurfaceArea) <> 0 ORDER BY Density ASC LIMIT 10;

```

## 14. List every unique world language

```sql

SELECT DISTINCT Language from countrylanguage;

```

## 15. List the names and GNP of the world's top 10 richest countries

```sql

SELECT Name, GNP from country ORDER BY GNP DESC LIMIT 10;

```

## 16. List the names of, and number of languages spoken by, the top ten most multilingual countries

```sql

SELECT country.Name, COUNT(countrylanguage.Language) AS Num_of_Languages FROM country LEFT JOIN countrylanguage ON country.Code = countrylanguage.CountryCode GROUP BY country.Name ORDER BY Num_of_Languages DESC LIMIT 10;


```

## 17. List every country where over 50% of its population can speak German

```sql

SELECT country.Name, countrylanguage.Percentage FROM country LEFT JOIN countrylanguage ON country.Code = countrylanguage.CountryCode WHERE countrylanguage.Language="German" AND countrylanguage.Percentage > 50;

```

## 18. Which country has the worst life expectancy? Discard zero or null values

```sql

SELECT Name, LifeExpectancy from country WHERE LifeExpectancy IS NOT NULL AND LifeExpectancy > 0 ORDER BY LifeExpectancy ASC LIMIT 1;

```

## 19. List the top three most common government forms

```sql

SELECT governmentform, COUNT(*) AS num_countries FROM country GROUP BY governmentform ORDER BY num_countries DESC LIMIT 3;

```

## 20. How many countries have gained independence since records began

```sql

SELECT COUNT(Name) from country WHERE IndepYear IS NOT NULL;

```
