
# DATABASE

## TABLES

### USERS

| id | name  | email   | password | created_at | updated_at |
| ---|  ---  | ---     | ---      | ---        |        --- |
| INT|VARCHAR| VARCHAR | VARCHAR | DATETIME    | DATETIME   |

### POSTS

| id | title | body | user_id | created_at | updated_at |
| ---|  ---  | ---  | ---     | ---        |        --- |
| INT|VARCHAR| TEXT | INT     | DATETIME   | DATETIME   |

### COMMENTS

| id | body | user_id | post_id | created_at | updated_at |
| ---|  --- |   ---   |   ---   |    ---     |    ---     |
| INT|TEXT  | INT     | INT     | DATETIME   | DATETIME   |
