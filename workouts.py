from abc import ABC

from strategies import STRATEGIES, WorkoutStrategy


class Workout(ABC):
    name = ""
    base_minutes = 0
    base_sets = 0
    kcal_per_minute = 0
    exercises = []

    def __init__(self, strategy: WorkoutStrategy):
        self.strategy = strategy

    def set_strategy(self, strategy: WorkoutStrategy):
        self.strategy = strategy

    def plan(self):
        plan = self.strategy.build_plan(self.base_minutes, self.base_sets)
        plan["calories"] = plan["minutes"] * self.kcal_per_minute
        plan["workout"] = self.name
        plan["level"] = self.strategy.name
        plan["exercises"] = self.exercises
        return plan


class CardioWorkout(Workout):
    name = "Кардио"
    base_minutes = 30
    base_sets = 3
    kcal_per_minute = 9
    exercises = ["Бег на месте", "Прыжки", "Скакалка"]


class StrengthWorkout(Workout):
    name = "Силовая"
    base_minutes = 40
    base_sets = 4
    kcal_per_minute = 6
    exercises = ["Приседания", "Отжимания", "Планка"]


class YogaWorkout(Workout):
    name = "Йога"
    base_minutes = 45
    base_sets = 2
    kcal_per_minute = 3
    exercises = ["Поза собаки", "Поза воина", "Поза ребёнка"]


class WorkoutFactory:
    _registry = {
        "cardio": CardioWorkout,
        "strength": StrengthWorkout,
        "yoga": YogaWorkout,
    }

    @staticmethod
    def create(kind: str, level: str) -> Workout:
        if kind not in WorkoutFactory._registry:
            raise ValueError(f"Неизвестный тип тренировки: {kind}")
        if level not in STRATEGIES:
            raise ValueError(f"Неизвестный уровень: {level}")
        strategy = STRATEGIES[level]()
        return WorkoutFactory._registry[kind](strategy)