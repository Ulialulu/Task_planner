from modules.Tasks_adding import load_tasks, save_tasks, add_task
from modules.hot_tasks import get_urgent_tasks, display_urgent_tasks
from modules.sorting import sorting_tasks
from modules.task_manager import complete_task, delete_task, filter_by_status, filter_by_priority, show_tasks
from modules.statistics import statistics

def main():
    """Главное меню программы"""
    tasks = load_tasks()
    while True:
        print("\n" + "=" * 50)
        print("ПЛАНИРОВЩИК ЗАДАЧ")
        print("=" * 50)
        print("1. Добавить задачу")
        print("2. Показать все задачи")
        print("3. Показать горящие задачи")
        print("4. Сортировать задачи")
        print("5. Фильтровать задачи")
        print("6. Отметить задачу выполненной")
        print("7. Удалить задачу")
        print("8. Статистика")
        print("9. Выход")
        print("-" * 50)
    
        choice = input("Выберите действие (1-8): ").strip()
        
        if choice == "1":                
            add_task()
            tasks = load_tasks()

        elif choice == "2":
            if not tasks:
                print("Список задач пуст!")
            else:
                show_tasks(tasks, "ВСЕ ЗАДАЧИ")
                
        elif choice == "3":
            display_urgent_tasks(tasks)

        elif choice == "4":
            if not tasks:
                print("Нет задач для сортировки!")
                continue
            while True:
                sort_type = input("Введите критерий сортировки (deadline/priority): ").strip()
                if sort_type not in ["deadline", "priority"]:
                    print("Такого варианта нет!")
                else:
                    break
            sorted_tasks = sorting_tasks(tasks, sort_type)
            show_tasks(sorted_tasks, f"ЗАДАЧИ, ОТСОРТИРОВАННЫЕ ПО {sort_type.upper()}")

        elif choice == "5":
            if not tasks:
                print("Нет задач для фильтрации!")
                continue
            while True:
                filter_type = input("Введите критерий фильтраци (статус/приоритет): ").strip()
                if filter_type not in ["статус", "приоритет"]:
                    print("Такого варианта нет!")
                else:
                    break
            if filter_type == "приоритет":
                print("\nДоступные приоритеты: высокий, средний, низкий")
                while True:
                    priority = input("Введите приоритет: ").lower().strip()
                    if priority not in ("высокий", "средний", "низкий"):
                        print("Неверный приоритет! Доступны: высокий, средний, низкий")
                    else:
                        break
                filtered = filter_by_priority(tasks, priority)
                if filtered:
                    show_tasks(filtered, f"ЗАДАЧИ С ПРИОРИТЕТОМ: {priority.upper()}")
                else:
                    print(f"Нет задач с приоритетом '{priority}'")
            if filter_type == "статус":
                print("\nДоступные статусы: выполнено, не выполнена")
                while True:
                    status = input("Введите статус: ").lower().strip()
                    if status not in ("выполнено", "не выполнена"):
                        print("Неверный статус! Доступны: выполнено, не выполнена")
                    else:
                        break
                filtered = filter_by_status(tasks, status)
                if filtered:
                    show_tasks(filtered, f"ЗАДАЧИ СО СТАТУСОМ: {status.upper()}")
                else:
                    print(f"Нет задач со статусом '{status}'")
                    
        elif choice == "6":
            if not tasks:
                print("Нет задач для отметки!")
                continue
            show_tasks(tasks, "ДОСТУПНЫЕ ЗАДАЧИ")
            task_id = int(input("\nВведите ID задачи: "))
            tasks = complete_task(tasks, task_id)

        elif choice == "7":    
            if not tasks:
                print("Нет задач для удаления!")
                continue
            show_tasks(tasks, "ДОСТУПНЫЕ ЗАДАЧИ")
            task_id = int(input("\nВведите ID задачи для удаления: "))
            tasks = delete_task(tasks, task_id)

        elif choice == "8":    
            print("\n--- СТАТИСТИКА ---")
            total, finished, missed = statistics(tasks)
            print(f"Всего задач: {total}")
            print(f"Выполнено: {finished}")
            print(f"Просрочено: {missed}")
            if total > 0:
                print(f"Выполнено: {finished/total*100:.1f}%")
            else:
                print("Выполнено: 0%")

        elif choice == "9":
            print("\nДо свидания!")
            return
        
        else:
            print("Такого варианта нет!")
                

if __name__ == "__main__":
    main()
    