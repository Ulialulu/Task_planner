from datetime import datetime, timedelta

def get_urgent_tasks(tasks):
    """ 
    Возвращает список задач, у которых дедлайн <= 2 дней от текущей даты 
    """
    today = datetime.now().date()
    urgent_tasks = []
    
    for task in tasks:
        if task.get("status") == "выполнена":
            continue  # Пропускаем выполненные задачи
            
        deadline_str = task.get("deadline")
        if not deadline_str:
            continue
            
        # Преобразуем строку дедлайна в объект даты. Если формат даты неверный, задача пропускается
        try:
            deadline_date = datetime.strptime(deadline_str, "%d-%m-%Y").date()
        except ValueError:
             continue
        
        days_left = (deadline_date - today).days
        
        if 0 <= days_left <= 2:
            task_with_days = task.copy()
            task_with_days["days_left"] = days_left
            urgent_tasks.append(task_with_days)
        # Добавляем просроченные задачи
        elif days_left < 0:
            task_with_days = task.copy()
            task_with_days["days_left"] = days_left
            task_with_days["is_overdue"] = True
            urgent_tasks.append(task_with_days)
    
    return urgent_tasks

def display_urgent_tasks(tasks):
    """
    Отображает горящие задачи с визуальным выделением
    """
    urgent = get_urgent_tasks(tasks)
    
    if not urgent:
        print("Горящих задач нет!")
        return
    
    print("=" * 50)
    print("Горящие задачи (дедлайн до 2 дней)!")
    print("=" * 50)
    
    for task in urgent:
        days = task.get("days_left", 0)
        is_overdue = task.get("is_overdue", False)
        
        if is_overdue:
            status_icon = "ПРОСРОЧЕНА!"
            color_code = "\033[91m"  # Красный 
        elif days == 0:
            status_icon = "СЕГОДНЯ!"
            color_code = "\033[38;5;208m"  #Оранжевый
        elif days == 1:
            status_icon = "ЗАВТРА!"
            color_code = "\033[93m"  #Желтый 
        else:
            status_icon = f"Осталось {days} дня"
            color_code = "\033[38;5;129m"
        
        reset_code = "\033[0m"
        
        print(f"{color_code}ID {task['id']}: {task['title']} [{status_icon}]{reset_code}")
        print(f"   Приоритет: {task['priority']}")
        print(f"   Дедлайн: {task['deadline']}")
        print("=" * 30)

