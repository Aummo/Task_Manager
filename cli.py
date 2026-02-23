from .services.TaskService import TaskService
from .infrastructure.SQLiteTaskRepository import SQLiteTaskRepository
repository = SQLiteTaskRepository()

service = TaskService(repository)

import click

@click.group()
def cli():
    """Task Manager CLI"""
    pass


@cli.command()
@click.argument('title')
@click.option('--desc','-d', default='',help='task description')
@click.option('--user_id', '-u', help='what is your user id?')
def add(title,desc,user_id):
    try:
        task = service.add_task(title, desc, user_id)
        click.echo(task.summary())
    except ValueError as e:
        click.echo(str(e))


@cli.command(name='list')
def list_tasks():
    tasks = service.list_tasks()
    if not tasks:
        click.echo('No tasks found')
        return
    for task in tasks:
        click.echo(task.summary())


@cli.command()
@click.argument('task_id')
def delete(task_id):
    removed = service.delete_task(task_id)
    if removed:
        click.echo('Task deleted')
    else:
        click.echo('task not found!')


@cli.command()
def clear():
    confirm = click.confirm('Are you sure you want to delete all tasks?')
    if confirm:
        service.clear_tasks()
        click.echo('all tasks cleared')
    else:
        click.echo('cancelled')



if __name__ == "__main__":
    cli()
