import pytest
from pawpal_system import ScheduledTask, TaskManager


def test_mark_complete_changes_task_status():
    """Verify that calling mark_complete() actually changes the task's status."""
    # Create a scheduled task with completed=False
    task = ScheduledTask(
        task_id="task_1",
        scheduled_time="10:00",
        duration=30,
        assigned_pet_id="pet_1",
        completed=False
    )
    
    # Initially, completed should be False
    assert task.completed == False
    
    # Call mark_complete()
    task.mark_complete()
    
    # After calling mark_complete(), completed should be True
    assert task.completed == True


def test_adding_task_increases_pet_task_count():
    """Verify that adding a task to a Pet increases that pet's task count."""
    # Create a TaskManager
    task_manager = TaskManager()
    
    # Initially, no tasks for pet_1
    initial_count = len(task_manager.get_tasks("pet_1"))
    assert initial_count == 0
    
    # Add a task for pet_1
    task_data = {
        "task_id": "task_1",
        "task_type": "feeding",
        "duration": 15,
        "priority": 1
    }
    task_manager.create_task("pet_1", task_data)
    
    # After adding, task count should increase by 1
    new_count = len(task_manager.get_tasks("pet_1"))
    assert new_count == 1