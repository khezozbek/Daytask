from django.shortcuts import render
from .models import Task
from django.utils import timezone
from datetime import datetime, timedelta


def main(request):
    tasks = Task.objects.all()
    current_time = timezone.now()
    tim = current_time + timedelta(hours=5)
    notifications = []
    print(tim)
    for task in tasks:
        if task.time >= current_time:
            notification = f"It's time to perform the task: {task.title}"
            notifications.append(notification)
        elif task.time <= current_time:
            notification = f"wait for done the task: {task.title}"
            notifications.append(notification)

    context = {
        "tasks": tasks,
        'notifications': notifications
    }
    return render(request, 'html/main.html', context)