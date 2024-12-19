from django.db import models
from rest_framework.exceptions import ValidationError

from config.settings import NULLABLE
from users.models import User


class Habit(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user")
    action = models.CharField(
        max_length=255, verbose_name="Действие", help_text="Укажите действие"
    )
    time = models.TimeField(verbose_name="Время", help_text="Укажите время")
    place = models.CharField(
        max_length=255, verbose_name="Место", help_text="Укажите место"
    )
    reward = models.CharField(
        max_length=255,
        **NULLABLE,
        verbose_name="Награда",
        help_text="Укажите вознаграждение"
    )
    pleasant_habit = models.BooleanField(
        default=False,
        verbose_name="Приятная привычка",
        help_text="Признак приятной привычки",
    )
    related_habit = models.ForeignKey(
        "self", on_delete=models.SET_NULL, **NULLABLE, related_name="related_habits"
    )
    periodicity = models.PositiveIntegerField(
        default=1, verbose_name="Периодичность", help_text="Укажите период повторения"
    )
    duration = models.PositiveIntegerField(
        verbose_name="Продолжительность", help_text="Укажите продолжительность"
    )
    is_public = models.BooleanField(
        default=False, verbose_name="Публичность", help_text="Признак публичности"
    )

    def __str__(self):
        return self.action

    class Meta:
        verbose_name = "Привычка"
        verbose_name_plural = "Привычки"

    def clean(self):
        if self.reward and self.related_habit:
            raise ValidationError(
                "Невозможно одновременно указать вознаграждение, и связанную с ним привычку."
            )
        if self.duration > 120:
            raise ValidationError("Продолжительность не должна превышать 120 секунд.")
        if self.pleasant_habit and (self.reward or self.related_habit):
            raise ValidationError(
                "Приятная привычка не может быть вознаграждением или связанной с ней привычкой."
            )
        if self.periodicity < 1 or self.periodicity > 7:
            raise ValidationError("Периодичность должна составлять от 1 до 7 дней.")
