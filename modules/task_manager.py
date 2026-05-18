# modules/task_manager.py
# Автор: mamamarria
# Задачи: отметка выполненной, удаление, фильтрация, 
from datetime import datetime
#  ЗАДАЧА 2: ОТМЕТКА ЗАДАЧИ ВЫПОЛНЕННОЙ 
def complete_task(tasks, task_id):
    
    for i, task in enumerate(tasks):
        if task['id'] == task_id:
            tasks[i]['status'] = 'выполнена'
            tasks[i]['completed_at'] = str(datetime.now())
            save_tasks(tasks)
            print(f" Выполнено: {task['title']}")
            return tasks
    print(f'Задача с ID {task_id} не найдена')
    return tasks


#  ЗАДАЧА 3: УДАЛИТЬ ЗАДАЧУ 

def delete_task(tasks, task_id):
    
    for i, task in enumerate(tasks):
        if task['id'] == task_id:
            deleted = tasks.pop(i)
            save_tasks(tasks)
            print(f" Удалено: {deleted['title']}")
            return tasks
    print(f" Задача с ID {task_id} не найдена")
    return tasks


#  ЗАДАЧА 4: ФИЛЬТРАЦИЯ 

def filter_by_status(tasks, status):
        return [t for t in tasks if t['status'] == status]


def filter_by_priority(tasks, priority):
        return [t for t in tasks if t['priority'] == priority]


def show_tasks(tasks, title="СПИСОК ЗАДАЧ"):
    if not tasks:
        print(f'{title}: пусто')
        return
    
    print(f'\n{title}:')

    for task in tasks:
        print(f"ID: {task['id']} | {task['title']} | до: {task['deadline']} | {task['priority']} | {task['status']}")
        if task.get('description'):
            print(f'Описание: {task['description']}')
        print("-" * 70)
# ТЕСТИРОВАНИЕ
if __name__ == "__main__":
    print("=== ТЕСТИРОВАНИЕ МОДУЛЯ ===\n")
    
    tasks = load_tasks()
    
    if not tasks:
        print("Нет сохранённых задач. Сначала добавьте задачи через add_task()")
        print("\nПример добавления задачи:")
        #add_task()  # раскомментируй для теста
    else:
        show_tasks(tasks, "СПИСОК ЗАДАЧ")
        
        # Примеры работы 
        print("\n--- Отмечаем задачу 1 как выполненную ---")
        complete_task(tasks, 1)
        
        print("\n--- Только выполненные ---")
        done = filter_by_status(tasks, "выполнена")
        show_tasks(done, "ВЫПОЛНЕННЫЕ")
        
        print("\n--- Только высокий приоритет ---")
        high = filter_by_priority(tasks, "высокий")
        show_tasks(high, "ВЫСОКИЙ ПРИОРИТЕТ")