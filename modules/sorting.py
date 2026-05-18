from datetime import datetime

def sorting_tasks(tasks, sort_type):
    """ Сортирует задачи по дедлайну или приоритету
        sort_type: "deadline" или "priority"
    """
    if sort_type == "deadline":
        by_deadline = sorted(tasks, key= lambda task: 
                            datetime.strptime("9999-12-31", "%Y-%m-%d").date() 
                            if not task.get("deadline") 
                            else datetime.strptime(task.get("deadline"), "%Y-%m-%d").date()
                            )
        return by_deadline
    elif sort_type == "priority":
        def get_priority(task):
            priority = task.get("priority")
            if priority == "высокий":
                return 1
            elif priority == "средний":
                return 2
            elif priority == "низкий":
                return 3
            else:
                return 4

        by_priority = sorted(tasks, key= get_priority)
        return by_priority
    

    

    



