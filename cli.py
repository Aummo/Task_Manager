import click 
from manger import Taskmanager



@click.group()
def cli():
    """Simple Task Manager CLI"""
    pass

@cli.command()
@click.argument('title')
@click.option('--desc', '-d', default='', help='Task description')
def add(title, desc):
    """Add a new task"""
    manager = Taskmanager()
    manager.add_task(title, desc)

@cli.command()
@click.argument('task_id', type=int)
def delete(task_id):
    """Delete a task by ID"""
    manager = Taskmanager()
    manager.del_task(task_id)

@cli.command(name='list')
def list_tasks():
    """List all tasks"""
    manager = Taskmanager()
    manager.list_task()

@cli.command()
@click.argument('task_id', type=int)
@click.argument('new_title')
@click.option('--desc', '-d', default=None, help='New description')
def update(task_id, new_title, desc):
    """Update a task"""
    manager = Taskmanager()
    task = manager.find_task(task_id)

    if task:
        task.title = new_title
        if desc is not None:
            task.desc = desc
        print(f"Task updated: {task}")
    else:
        print(f"Task with ID {task_id} not found")

@cli.command()
def clear():
    """Clear all tasks"""
    manager = Taskmanager()
    confirm = input("Are you sure you want to delete all tasks? (y/n): ")
    if confirm.lower() == 'y':
        manager.tasks.clear()
        manager.next_id = 1  # reset ID counter
        print("All tasks cleared")
    else:
        print("Clear cancelled")


if __name__ == '__main__':
    cli()