from pawpal_system import OwnerProfile, PetProfile, PetTask, TaskManager, Constraint


def main():
    # Create an Owner
    owner = OwnerProfile(
        owner_id="owner_001",
        name="Sarah Johnson",
        email="sarah.johnson@email.com"
    )
    print(f"✓ Owner created: {owner.get_profile_summary()}\n")
    
    # Create first Pet
    pet1 = PetProfile(
        pet_id="pet_001",
        owner_id="owner_001",
        name="Buddy",
        age=3,
        breed="Golden Retriever",
        sex="Male",
        dietary_restrictions=["grain-free"],
        allergies=["chicken"]
    )
    owner.add_pet(pet1)
    print(f"✓ Pet 1 created: {pet1.get_summary()}")
    
    # Create second Pet
    pet2 = PetProfile(
        pet_id="pet_002",
        owner_id="owner_001",
        name="Luna",
        age=2,
        breed="Siamese Cat",
        sex="Female",
        medical_notes="Indoor cat, needs regular playtime"
    )
    owner.add_pet(pet2)
    print(f"✓ Pet 2 created: {pet2.get_summary()}\n")
    
    # Create a Task Manager
    task_manager = TaskManager()
    
    # Task 1: Morning feeding for Buddy
    task1 = PetTask(
        task_id="task_001",
        pet_id="pet_001",
        task_type="Feeding",
        duration=15, # in mins
        priority=1,
        is_required=True,
        status="pending"
    )
    task_manager.tasks[task1.task_id] = task1
    print(f"✓ Task 1 added: {task1.task_type} for Buddy at 8:00 AM")
    
    # Task 2: Midday playtime for Luna
    task2 = PetTask(
        task_id="task_002",
        pet_id="pet_002",
        task_type="Playtime",
        duration=30,
        priority=2,
        is_required=True,
        status="pending"
    )
    task_manager.tasks[task2.task_id] = task2
    print(f"✓ Task 2 added: {task2.task_type} for Luna at 12:00 PM")
    
    # Task 3: Afternoon walk for Buddy
    task3 = PetTask(
        task_id="task_003",
        pet_id="pet_001",
        task_type="Walk",
        duration=45,
        priority=1,
        is_required=True,
        status="pending"
    )
    task_manager.tasks[task3.task_id] = task3
    print(f"✓ Task 3 added: {task3.task_type} for Buddy at 3:00 PM\n")
    
    # Print Today's Schedule
    print("=" * 60)
    print("TODAY'S SCHEDULE")
    print("=" * 60)
    
    schedule_times = [
        ("8:00 AM", "task_001", "Buddy"),
        ("12:00 PM", "task_002", "Luna"),
        ("3:00 PM", "task_003", "Buddy")
    ]
    
    for time, task_id, pet_name in schedule_times:
        if task_id in task_manager.tasks:
            task = task_manager.tasks[task_id]
            print(f"\n{time} - {task.task_type.upper()}")
            print(f"  Pet: {pet_name}")
            print(f"  Duration: {task.duration} minutes")
            print(f"  Priority: {'High' if task.priority == 1 else 'Normal'}")
            print(f"  Status: {task.status}")
    
    print("\n" + "=" * 60)
    print(f"Total Tasks Today: {len(task_manager.tasks)}")
    print("=" * 60)


if __name__ == "__main__":
    main()
