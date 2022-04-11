/************************************************************分割线************************************************************/

/* todo 0175（合并两表） */
SELECT Person.FirstName,Person.LastName,Address.City,Address.State FROM Person LEFT JOIN Address ON Person.PersonId=Address.PersonId

/* todo 0181（超过经理收入的员工） */
SELECT e1.Name as Employee FROM Employee e1,Employee e2 WHERE e1.ManagerId=e2.Id and e1.Salary>e2.Salary

/* todo 0182（重复的邮件） */
SELECT Email FROM Person GROUP BY Email HAVING COUNT(Id)>1
