from __future__ import annotations
from dataclasses import dataclass, field
from typing import Dict, List, Tuple, Optional


class Constraint:
    def __init__(
        self,
        start_time: str = "",
        end_time: str = "",
        max_duration: int = 0,
        day_of_week: Optional[List[str]] = None,
    ):
        self.start_time: str = start_time
        self.end_time: str = end_time
        self.max_duration: int = max_duration
        self.day_of_week: List[str] = day_of_week if day_of_week is not None else []

    def is_valid_window(self, time: str) -> bool:
        """Return True if the given time is within this constraint window."""
        raise NotImplementedError

    def get_available_slots(self) -> List[Tuple[str, str]]:
        """Return a list of available (start, end) time slots."""
        raise NotImplementedError


class OwnerProfile:
    def __init__(
        self,
        owner_id: str,
        name: str,
        email: str,
        pets: Optional[List[PetProfile]] = [],
        daily_availability: Optional[Constraint] = None,
    ):
        self.owner_id: str = owner_id
        self.name: str = name
        self.email: str = email
        self.pets = pets
        self.daily_availability: Optional[Constraint] = daily_availability

    def add_pet(self, pet: PetProfile) -> None:
        self.pets.append(pet)
    
    def remove_pet(self, pet: PetProfile) -> None:
        for p in self.pets:
            if p.pet_id == pet.pet_id:
                self.pets.remove(p)
                break

    def update_availability(self, constraint: Constraint) -> None:
        self.daily_availability = constraint

    def get_profile_summary(self) -> str:
        return f"Owner {self.name} ({self.owner_id}) - {self.email}"


class PetProfile:
    def __init__(
        self,
        pet_id: str,
        owner_id: str,
        name: str,
        age: int,
        breed: str,
        sex: str,
        dietary_restrictions: Optional[List[str]] = None,
        allergies: Optional[List[str]] = None,
        medical_notes: str = "",
    ):
        self.pet_id: str = pet_id
        self.owner_id: str = owner_id
        self.name: str = name
        self.age: int = age
        self.breed: str = breed
        self.sex: str = sex
        self.dietary_restrictions: List[str] = dietary_restrictions or []
        self.allergies: List[str] = allergies or []
        self.medical_notes: str = medical_notes

    def update_profile(self, data: Dict) -> None:
        for key, value in data.items():
            if hasattr(self, key):
                setattr(self, key, value)

    def get_summary(self) -> str:
        return f"Pet {self.name} ({self.pet_id}), {self.age} years old, breed {self.breed}."


class PetTask:
    def __init__(
        self,
        task_id: str,
        pet_id: str,
        task_type: str,
        duration: int, # in mins
        priority: int,
        preferred_time_window: Optional[Constraint] = None,
        is_recurring: bool = False,
        is_flexible: bool = False,
        is_required: bool = True,
        status: str = "pending",
    ):
        self.task_id: str = task_id
        self.pet_id: str = pet_id
        self.task_type: str = task_type
        self.duration: int = duration
        self.priority: int = priority
        self.preferred_time_window: Optional[Constraint] = preferred_time_window
        self.is_recurring: bool = is_recurring
        self.is_flexible: bool = is_flexible
        self.is_required: bool = is_required
        self.status: str = status

    def update_task(self, data: Dict) -> None:
        for key, value in data.items():
            if hasattr(self, key):
                setattr(self, key, value)

    def toggle_completed(self) -> None:
        self.status = "completed" if self.status != "completed" else "pending"

    def get_task_details(self) -> Dict:
        return {
            "task_id": self.task_id,
            "pet_id": self.pet_id,
            "task_type": self.task_type,
            "duration": self.duration,
            "priority": self.priority,
            "preferred_time_window": self.preferred_time_window,
            "is_recurring": self.is_recurring,
            "is_flexible": self.is_flexible,
            "is_required": self.is_required,
            "status": self.status,
        }


class ScheduledTask:
    def __init__(
        self,
        task_id: str,
        scheduled_time: str,
        duration: int,
        assigned_pet_id: str,
        completed: bool = False,
    ):
        self.task_id: str = task_id
        self.scheduled_time: str = scheduled_time
        self.duration: int = duration
        self.assigned_pet_id: str = assigned_pet_id
        self.completed: bool = completed

    def mark_complete(self) -> None:
        self.completed = True


class PlanExplanation:
    def __init__(
        self,
        scheduled_tasks: Optional[List[ScheduledTask]] = None,
        reasoning: str = "",
        constraints_applied: Optional[List[str]] = None,
    ):
        self.scheduled_tasks: List[ScheduledTask] = scheduled_tasks or []
        self.reasoning: str = reasoning
        self.constraints_applied: List[str] = constraints_applied or []

    def get_full_explanation(self) -> str:
        tasks = ", ".join([t.task_id for t in self.scheduled_tasks])
        return f"Tasks planned: {tasks}. Reasoning: {self.reasoning}. Constraints: {', '.join(self.constraints_applied)}"

    def get_brief_summary(self) -> str:
        return f"{len(self.scheduled_tasks)} tasks scheduled."


class TaskManager:
    def __init__(self):
        self.tasks: Dict[str, PetTask] = {}
        self.pet_preferences: Dict[str, Dict] = {}

    def create_task(self, pet_id: str, task_data: Dict) -> PetTask:
        task_id = task_data.get("task_id") or f"task_{len(self.tasks) + 1}"
        task = PetTask(pet_id=pet_id, **task_data)
        self.tasks[task.task_id] = task
        return task

    def get_tasks(self, pet_id: str) -> List[PetTask]:
        return [t for t in self.tasks.values() if t.pet_id == pet_id]

    def update_task(self, task_id: str, data: Dict) -> None:
        if task_id in self.tasks:
            self.tasks[task_id].update_task(data)

    def delete_task(self, task_id: str) -> None:
        self.tasks.pop(task_id, None)

    def set_task_preferences(self, pet_id: str, defaults: Dict) -> None:
        self.pet_preferences[pet_id] = defaults

    def get_pet_preferences(self, pet_id: str) -> Dict:
        return self.pet_preferences.get(pet_id, {})


class Scheduler:
    def __init__(self, task_manager: Optional[TaskManager] = None):
        self.task_manager: TaskManager = task_manager or TaskManager()

    def retrieve_tasks_for_owner(self, owner: OwnerProfile) -> List[PetTask]:
        all_tasks = []
        for pet in owner.pets:
            all_tasks.extend(self.task_manager.get_tasks(pet.pet_id))
        return all_tasks

    def generate_daily_plan(self, owner: OwnerProfile, date: str, constraints: Optional[Constraint] = None) -> PlanExplanation:
        # Step 1: Retrieve all tasks for the owner's pets
        tasks = self.retrieve_tasks_for_owner(owner)
        
        # Step 2: Rank tasks by priority (using existing helper)
        ranked_tasks = self._rank_by_priority(tasks)
        
        # Step 3: Calculate the best schedule (using existing helper)
        scheduled_tasks = self._calculate_best_schedule(ranked_tasks, constraints)
        
        # Step 4: Build reasoning and constraints list (placeholders for now)
        reasoning = f"Scheduled {len(scheduled_tasks)} tasks for {date} based on priority and constraints."
        constraints_applied = ["Owner availability", "Pet preferences"] if constraints else []
        
        # Step 5: Return the plan explanation
        return PlanExplanation(
            scheduled_tasks=scheduled_tasks,
            reasoning=reasoning,
            constraints_applied=constraints_applied)

    def explain_plan(self, plan: PlanExplanation) -> str:
        return plan.get_full_explanation()

    def allow_manual_adjust(self, plan: PlanExplanation, edits: Dict) -> PlanExplanation:
        raise NotImplementedError

    def _calculate_best_schedule(self, tasks: List[PetTask], constraints: Optional[Constraint] = None) -> List[ScheduledTask]:
        raise NotImplementedError

    def _rank_by_priority(self, tasks: List[PetTask]) -> List[PetTask]:
        return sorted(tasks, key=lambda t: t.priority, reverse=True)
