
/* 
   T-SQL
   Task 1 
   Shows the top equal departments as well 
*/

WITH TOP_DEPS
     AS (SELECT COUNT(*) AS In_Department, 
                Id_dep
         FROM [dbo].[PERSONAL]
         GROUP BY Id_dep)
     SELECT b.*
     FROM TOP_DEPS a
          INNER JOIN [dbo].[Department] b ON a.Id_dep = b.Id
     WHERE In_Department =
     (
         SELECT MAX(In_Department)
         FROM TOP_DEPS
     );

/* Task 2 */

SELECT Person.*
FROM [dbo].[PERSONAL] AS Person, 
     [dbo].[PERSONAL] AS Head
WHERE Head.Id = Person.Id_head
      AND Person.sal > Head.sal;
