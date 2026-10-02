from abc import ABC, abstractmethod


class WorkoutStrategy(ABC):
    name = ""

    @abstractmethod
    def build_plan(self, base_minutes, base_sets):
        """Возвращает параметры тренировки для данного уровня."""


class BeginnerStrategy(WorkoutStrategy):
    name = "Начинающий"

    def build_plan(self, base_minutes, base_sets):
        return {
            "minutes": round(base_minutes * 0.7),
            "sets": max(1, base_sets - 1),
            "rest_seconds": 90,
            "intensity": "низкая",
        }


class AdvancedStrategy(WorkoutStrategy):
    name = "Продвинутый"

    def build_plan(self, base_minutes, base_sets):
        return {
            "minutes": round(base_minutes * 1.3),
            "sets": base_sets + 1,
            "rest_seconds": 45,
            "intensity": "высокая",
        }


STRATEGIES = {
    "beginner": BeginnerStrategy,
    "advanced": AdvancedStrategy,
}