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
            deadline_date = datetime.strptime(deadline_str, "%Y-%m-%d").date()
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

test_tasks = [
    # 1. Горящая задача (сегодня)
    {
        "id": 1,
        "title": "Сдать годовой отчет",
        "status": "в работе",
        "deadline": datetime.now().strftime("%Y-%m-%d"),  # Сегодня
        "priority": "высокий"
    },
    
    # 2. Горящая задача (завтра)
    {
        "id": 2,
        "title": "Встреча с инвесторами",
        "status": "в работе",
        "deadline": (datetime.now() + timedelta(days=1)).strftime("%Y-%m-%d"),
        "priority": "критический"
    },
    
    # 3. Горящая задача (послезавтра)
    {
        "id": 3,
        "title": "Подготовить презентацию",
        "status": "в работе",
        "deadline": (datetime.now() + timedelta(days=2)).strftime("%Y-%m-%d"),
        "priority": "средний"
    },
    
    # 4. Просроченная задача (должна попасть в горящие)
    {
        "id": 4,
        "title": "Отправить договор клиенту",
        "status": "в работе",
        "deadline": (datetime.now() - timedelta(days=1)).strftime("%Y-%m-%d"),
        "priority": "высокий"
    },
    
    # 5. Сильно просроченная задача (тоже попадет)
    {
        "id": 5,
        "title": "Обновить документацию",
        "status": "в работе",
        "deadline": (datetime.now() - timedelta(days=10)).strftime("%Y-%m-%d"),
        "priority": "низкий"
    },
    
    # 6. Выполненная задача (должна быть пропущена)
    {
        "id": 6,
        "title": "Провести код-ревью",
        "status": "выполнена",
        "deadline": (datetime.now() - timedelta(days=2)).strftime("%Y-%m-%d"),
        "priority": "средний"
    },
    
    # 7. Негорящая задача (больше 2 дней)
    {
        "id": 7,
        "title": "Спланировать следующий спринт",
        "status": "в работе",
        "deadline": (datetime.now() + timedelta(days=5)).strftime("%Y-%m-%d"),
        "priority": "средний"
    },
    
    # 8. Негорящая задача (очень далекая)
    {
        "id": 8,
        "title": "Изучить новый фреймворк",
        "status": "в работе",
        "deadline": (datetime.now() + timedelta(days=30)).strftime("%Y-%m-%d"),
        "priority": "низкий"
    },
    
    # 9. Задача без дедлайна (должна быть пропущена)
    {
        "id": 9,
        "title": "Позвонить заказчику",
        "status": "в работе",
        "deadline": None,
        "priority": "высокий"
    },
    
    # 10. Задача с некорректным форматом даты (должна быть пропущена)
    {
        "id": 10,
        "title": "Отправить отчет",
        "status": "в работе",
        "deadline": "20.05.2026",  # Неправильный формат
        "priority": "средний"
    },
    
    # 11. Задача без поля deadline (должна быть пропущена)
    {
        "id": 11,
        "title": "Купить подарок коллеге",
        "status": "в работе",
        "priority": "низкий"
    },
    
    # 12. Задача без ID (вызовет ошибку в display_urgent_tasks)
    {
        "title": "Нет ID у задачи",
        "status": "в работе",
        "deadline": (datetime.now() + timedelta(days=1)).strftime("%Y-%m-%d"),
        "priority": "средний"
    },
    
    # 13. Пустая строка в статусе (должна обработаться)
    {
        "id": 13,
        "title": "Статус не указан",
        "status": "",
        "deadline": (datetime.now() + timedelta(days=1)).strftime("%Y-%m-%d"),
        "priority": "средний"
    },
    
    # 14. Задача с разными вариантами статуса "выполнена"
    {
        "id": 14,
        "title": "Уже сделано (выполнено)",
        "status": "выполнено",  # Другой вариант
        "deadline": (datetime.now() - timedelta(days=1)).strftime("%Y-%m-%d"),
        "priority": "высокий"
    },
    
    # 15. Крайний случай: дедлайн ровно через 2 дня и 1 секунду
    {
        "id": 15,
        "title": "Пограничный случай",
        "status": "в работе",
        "deadline": (datetime.now() + timedelta(days=2, hours=1)).strftime("%Y-%m-%d"),
        "priority": "средний"
    }
]
if __name__ == "__main__":
    print("📅 Текущая дата:", datetime.now().date())
    print("=" * 50)
    display_urgent_tasks(test_tasks)