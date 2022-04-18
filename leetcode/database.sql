/************************************************************分割线************************************************************/

/* todo 0175（合并两表） */
SELECT person.firstname,person.lastname,address.city,address.state FROM person LEFT JOIN address ON person.personid=address.personid

/* todo 0181（超过经理收入的员工） */
SELECT e1.name AS employee FROM employee e1,employee e2 WHERE e1.managerid=e2.id AND e1.salary>e2.salary

/* todo 0182（重复的邮件） */
SELECT email FROM person GROUP BY email HAVING COUNT(id)>1

/* todo 0183（从不订购的客户） */
SELECT name AS customers FROM customers WHERE id NOT IN (SELECT customerid FROM orders)

/* todo 0196（删除重复的邮件） */
DELETE p2 FROM person p1,person p2 WHERE p1.email=p2.email AND p2.id>p1.id
