import random
first_names = ['James', 'John', 'Robert', 'Michael', 'William', 'David', 'Richard', 'Joseph', 'Charles', 'Thomas',
               'Christopher', 'Daniel', 'Matthew', 'Anthony', 'Donald', 'Mark', 'Paul', 'Steven', 'Andrew', 'Kenneth',
               'George', 'Joshua', 'Kevin', 'Brian', 'Edward', 'Ronald', 'Timothy', 'Jason', 'Jeffrey', 'Ryan',
               'Jacob', 'Gary', 'Nicholas', 'Eric', 'Stephen', 'Jonathan', 'Larry', 'Justin', 'Scott', 'Brandon',
               'Benjamin', 'Samuel', 'Frank', 'Gregory', 'Raymond', 'Patrick', 'Alexander', 'Jack', 'Dennis', 'Jerry',
               'Tyler', 'Aaron', 'Henry', 'Douglas', 'Peter', 'Jose', 'Adam', 'Zachary', 'Nathan', 'Walter',
               'Harold', 'Kyle', 'Carl', 'Arthur', 'Gerald', 'Roger', 'Keith', 'Lawrence', 'Terry', 'Sean',
               'Jesse', 'Joe', 'Christian', 'Craig', 'Derrick', 'Travis', 'Jeremy', 'Ralph', 'Billy', 'Bruce',
               'Roy', 'Randy', 'Eugene', 'Vincent', 'Russell', 'Louis', 'Bobby', 'Philip', 'Johnny', 'Logan',
               'Wayne', 'Alan', 'Harry', 'Juan', 'Wayne', 'Roy', 'Dennis', 'Eugene', 'Victor', 'Mary', 'Patricia', 'Jennifer', 'Linda', 'Elizabeth', 'Barbara', 'Susan', 'Jessica', 'Sarah', 'Karen',
               'Nancy', 'Lisa', 'Betty', 'Margaret', 'Sandra', 'Ashley', 'Kimberly', 'Emily', 'Donna', 'Michelle',
               'Dorothy', 'Carol', 'Amanda', 'Melissa', 'Deborah', 'Stephanie', 'Rebecca', 'Laura', 'Sharon', 'Cynthia',
               'Kathleen', 'Amy', 'Shirley', 'Anna', 'Angela', 'Ruth', 'Brenda', 'Pamela', 'Nicole', 'Katherine',
               'Virginia', 'Catherine', 'Christine', 'Debra', 'Rachel', 'Carolyn', 'Janet', 'Emma', 'Maria', 'Heather',
               'Diane', 'Julie', 'Joyce', 'Frances', 'Alice', 'Joan', 'Julia', 'Evelyn', 'Grace', 'Sophia',
               'Emma', 'Olivia', 'Mia', 'Ava', 'Isabella', 'Amelia', 'Harper', 'Evelyn', 'Abigail', 'Sofia',
               'Scarlett', 'Ella', 'Emily', 'Camila', 'Aria', 'Layla', 'Chloe', 'Madison', 'Elizabeth', 'Lily',
               'Grace', 'Eleanor', 'Zoey', 'Natalie', 'Hannah', 'Lillian', 'Addison', 'Aubrey', 'Brooklyn', 'Stella',
               'Victoria', 'Claire', 'Skylar', 'Lucy', 'Paisley', 'Everly', 'Aubree', 'Eliana', 'Luna', 'Isabelle', 'Lewis']

last_names = ['Smith', 'Johnson', 'Williams', 'Brown', 'Jones', 'Miller', 'Davis', 'Garcia', 'Rodriguez', 'Martinez',
              'Hernandez', 'Lopez', 'Gonzalez', 'Wilson', 'Anderson', 'Thomas', 'Taylor', 'Moore', 'Jackson', 'Martin',
              'Lee', 'Perez', 'Thompson', 'White', 'Harris', 'Sanchez', 'Clark', 'Ramirez', 'Lewis', 'Robinson',
              'Walker', 'Young', 'Allen', 'King', 'Wright', 'Scott', 'Torres', 'Nguyen', 'Hill', 'Flores',
              'Green', 'Adams', 'Nelson', 'Baker', 'Hall', 'Rivera', 'Campbell', 'Mitchell', 'Carter', 'Roberts',
              'Gomez', 'Phillips', 'Evans', 'Turner', 'Diaz', 'Parker', 'Cruz', 'Edwards', 'Collins', 'Reyes',
              'Stewart', 'Morris', 'Morales', 'Murphy', 'Cook', 'Rogers', 'Gutierrez', 'Ortiz', 'Morgan', 'Cooper',
              'Peterson', 'Bailey', 'Reed', 'Kelly', 'Howard', 'Ramos', 'Kim', 'Cox', 'Ward', 'Richardson',
              'Watson', 'Brooks', 'Chavez', 'Wood', 'James', 'Bennett', 'Gray', 'Mendoza', 'Ruiz', 'Hughes',
              'Price', 'Alvarez', 'Castillo', 'Sanders', 'Patel', 'Myers', 'Long', 'Ross', 'Foster', 'Jimenez',
              'Powell', 'Jenkins', 'Perry', 'Russell', 'Sullivan', 'Bell', 'Coleman', 'Butler', 'Henderson', 'Barnes',
              'Gonzales', 'Fisher', 'Vasquez', 'Simmons', 'Romero', 'Jordan', 'Patterson', 'Alexander', 'Hamilton', 'Graham',
              'Reynolds', 'Griffin', 'Wallace', 'Moreno', 'West', 'Cole', 'Hayes', 'Bryant', 'Herrera', 'Gibson',
              'Ellis', 'Trans', 'Medina', 'Aguilar', 'Stevens', 'Murray', 'Ford', 'Castro', 'Marshall', 'Owens',
              'Harrison', 'Fernandez', 'Mcdonald', 'Woods', 'Washington', 'Kennedy', 'Wells', 'Vargas', 'Henry', 'Chen',
              'Freeman', 'Webb', 'Tucker', 'Guzman', 'Burns', 'Crawford', 'Olson', 'Simpson', 'Porter', 'Hunter',
              'Gordon', 'Mendez', 'Silva', 'Shaw', 'Snider', 'Vasquez', 'Tillman', 'Ochoa', 'Moss', 'Fitzgerald',
              'Fleming', 'Middleton', 'Mendez', 'Gibbs', 'Huang', 'Dixon', 'Fuentes', 'Haney', 'Frank', 'Aguirre',
              'Harrell', 'Padilla', 'Pacheco', 'Barron', 'Kim', 'Kidd', 'Widom', 'Yu', 'Greer', 'Briggs',
              'Pham', 'Valencia', 'Odonnell', 'Mays', 'Hale', 'Hobbs', 'Duran', 'Gibbons', 'Velez', 'Monroe',
              'Cobb', 'Merrick', 'Cline', 'Tran', 'Duran', 'Houston', 'Bryan', 'Huang', 'Roberson', 'Mcmahon',
              'Yu', 'Krause', 'Suarez', 'Frost', 'Avila', 'Hawkins', 'Hardin', 'Chen', 'Case', 'Cuevas']
name = ''
count = 0
while name != "Lewis Hamilton":
    name = random.choice(first_names) + " " + random.choice(last_names)
    count += 1
print("It took", count, "attempts to get Lewis Hamilton!")
