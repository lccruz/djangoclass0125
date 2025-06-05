# create a Django command to create N tasks
from django.core.management.base import BaseCommand
from tasks.models import Task
from django.utils import timezone
import random  

class Command(BaseCommand):
    help = 'Create N tasks with random data'

    def add_arguments(self, parser):
        parser.add_argument('number_of_tasks', type=int, help='Number of tasks to create')

    def handle(self, *args, **kwargs):
        number_of_tasks = kwargs['number_of_tasks']
        for i in range(number_of_tasks):
            Task.objects.create(
                title=f'Task {i + 1}',
                description=f'This is the description for task {i + 1}',
                status=random.choice(['pending', 'in_progress', 'completed'])
            )
        self.stdout.write(self.style.SUCCESS(f'Successfully created {number_of_tasks} tasks'))
        return f'Successfully created {number_of_tasks} tasks'