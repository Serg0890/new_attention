count_empl = int(input("кол-во сотрудников в офисе "))
works_id = []
for _ in range(count_empl):
    work_id = int(input("Id сотрудника "))
    works_id.append(work_id)

search_id = int(input("какой id ищем "))

search = False
 
for id in works_id:
    if id == search_id:
        search = True

if search:
    print("работает")
else:
    print("отсутствует")