from datetime import datetime
def statistics(tasks):
    total = len(tasks)
    finished = 0
    missed = 0
    today = datetime.now().date()

    for task in tasks:
        if task.get("status") == "выполнена":
            finished += 1
            continue  
        deadline_str = task.get("deadline")
        if deadline_str:
            try:
                deadline_date = datetime.strptime(deadline_str, "%Y-%m-%d").date()
                if deadline_date < today:
                    missed += 1
            except ValueError:
                pass
    return total, finished, missed
