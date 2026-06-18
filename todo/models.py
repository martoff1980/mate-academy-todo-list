from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name


class Task(models.Model):
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    deadline = models.DateTimeField(null=True, blank=True)
    is_done = models.BooleanField(default=False)
    tags = models.ManyToManyField(Tag, related_name="tasks")

    class Meta:
        # Сортировка: сначала невыполненные (False), затем выполненные (True)
        # Внутри этих групп — от самых новых к старым
        ordering = ["is_done", "-created_at"]

    def __str__(self):
        return f"{self.content[:30]}... (Done: {self.is_done})"
