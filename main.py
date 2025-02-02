# zadanie, widzimy nazwę | datę 
class Task:
  def __init__(self, task_name, due_date):
    self.task_name = task_name
    self.due_date = due_date

# obsługa zadania | dodanie zadania | usunięcie zadania | wyświetlenie | edycja zadania |
class TaskManager:
  def __init__(self):
    self.tasks = []

  def add_task(self, task_name, due_date):
    task = Task(task_name, due_date)
    self.tasks.append(task)

  def remove_task(self, task_name):
    task_exists = False

    for task in self.tasks:
      if task.task_name == task_name:
        self.tasks.remove(task)
        task_exists = True
        break

    if not task_exists:
      print("Nie można odnaleźć zadania o podanej nazwie: ", task_name)
    
  def display_tasks(self):
    if not self.tasks:
      print("Brak zadań")
    else:
      print("Lista zadań:")

      for task in self.tasks:
        print(task.task_name, "| termin:", task.due_date)
  
  def change_due_date(self, task_name, new_due_date):
    task_exists = False
    for task in self.tasks:
      if task.task_name == task_name:
        task.due_date = new_due_date
        task_exists = True
        print("Termin zadania:", task_name, "został zmieniony na:", new_due_date)
        break

    if not task_exists:
      print("Nie można odnaleźć zadania o nazwie:", task_name)

task_manager = TaskManager()
task_manager.add_task("Umyj naczynia", "01.12.2023")
task_manager.add_task("Wynieś śmieci", "07.12.2023")
task_manager.add_task("Posprzątaj", "07.12.2023")
print("-------------------------------")
task_manager.display_tasks()

task_manager.change_due_date("Umyj naczynia", "08.12.2023")
task_manager.change_due_date("Posprzątaj", "11.11.2024")
task_manager.remove_task("Wynieś śmieci")

print("-------------------------------")
task_manager.display_tasks()