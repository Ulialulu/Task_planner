from modules.task_1_zadachliiii import load_tasks, add_task


def main():
    """Главное меню программы"""
    tasks = load_tasks()
    while True:
        print("\n" + "=" * 50)
        print("ПЛАНИРОВЩИК ЗАДАЧ")
        print("=" * 50)
        print("1. Добавить задачу")
        #print("2. Показать все задачи")
        #print("3. Показать горящие задачи")
        #print("4. Фильтр по приоритету")
        #print("5. Отметить задачу выполненной")
        #print("6. Удалить задачу")
        #print("7. Статистика")
        print("8. Выход")
        print("-" * 50)
        while True:
            choice = input("Выберите действие (1-8): ").strip()
        
            if choice == 1:
                add_task()
                break

            elif choice == "8":
                print("\nДо свидания!")
                return
        
            else:
                print("Такого варианта нет!")
                

if __name__ == "__main__":
    main()
    