# modules/task_manager.py
# Автор: mamamarria
# Задачи: отметка выполненной, удаление, фильтрация, 
from datetime import datetime
# ЗАДАЧА 2. ОТМЕТКА ЗАДАЧИ ВЫПОЛНЕННОЙ

def complete_task(task, task_index):
    """Отмечает задачу выполненной по индексу"""
    if 0 <= task_index < len(tasks):
        tasks[task_index]['status'] = 'выполнена'
        tasks[task_index]['completed_at'] = str(datetime.now())
        print(f'Выполнено: {tasks[task_index]['title']}')
    else:
        print('Несуществующий индекс')
    return tasks

#ЗАДАЧА 3: УДАЛИТЬ задачу

def delete_task(tasks, task_index):
    """Удаляет задачу по индексу"""
    if 0 <= task_index < len(tasks):
        deleted = tasks.pop(task_index)
        print(f'Удалено: {deleted['title']}')
    else:
        print('Несуществующий индекс')    
    return tasks

#ЗАДАЧА 4: ФИЛЬТРАЦИЯ        

def filter_by_status(tasks, status):
    """Фильтрует по статусу ("выполнена" или "не выполнена")"""
    return [t for t in tasks if t['status']==status]
def filter_by_priority(tasks, priority):
    """Фильтрует по приоритету ('high', 'medium', 'low')"""
    return [t for t in tasks if t['priority']==priority]


def show_tasks(tasks, title="СПИСОК ЗАДАЧ"):
    """Красиво показывает список задач"""
    if not tasks:
        print(f'{title}: пусто')
        return
    
    print(f'{title}:')
    for i, task in enumerate(tasks):
        
        print(f"{i+1}. {task['title']} | до: {task['deadline']}")


# ========== ТЕСТИРОВАНИЕ (запускается только при прямом запуске файла) ==========
if __name__ == "__main__":
    # Тестовые задачи
    tasks = [
        {"title": "Сдать проект", "status": "не выполнена", "priority": "high", "deadline": "2026-05-20"},
        {"title": "Купить продукты", "status": "не выполнена", "priority": "medium", "deadline": "2026-05-15"},
        {"title": "Позвонить маме", "status": "выполнена", "priority": "low", "deadline": "2026-05-10"},
    ]
    
    print("=== ПРОВЕРКА РАБОТЫ ===\n")
    
    # Показываем все задачи
    show_tasks(tasks, "ВСЕ ЗАДАЧИ")
    
    # Отмечаем задачу выполненной
    print("\n--- Отмечаем задачу 3 как выполненную ---")
    complete_task(tasks, 2)
    
    # Фильтруем
    print("\n--- Только выполненные ---")
    done = filter_by_status(tasks, "выполнена")
    show_tasks(done, "ВЫПОЛНЕННЫЕ")
    
    print("\n--- Только высокий приоритет ---")
    high = filter_by_priority(tasks, "high")
    show_tasks(high, "HIGH PRIORITY")
    
    # Удаляем задачу
    print("\n--- Удаляем задачу 3 ---")
    delete_task(tasks, 2)
    
    # Что осталось
    show_tasks(tasks, "ОСТАВШИЕСЯ")