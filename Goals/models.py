from django.db import models
from django.utils import timezone

PRIORITY_CHOICES = (
    ("T", "Top"),
    ("H", "Hight"),
    ("N", "Normal"),
    ("L", "Low")
)

STATUS_CHOICES = (
    ("P", "Planned"),
    ("I", "In work"),
    ("Pr", "Procrastinate"),
    ("O", "Outstanding"),
    ("C", "Closed"),
    ("D", "Deleted")
)


class Category(models.Model):
    Item = models.CharField(max_length=30)
    Help_text = models.CharField(max_length=30, blank=True)


class Group(models.Model):
    Item = models.CharField(max_length=30)
    Help_text = models.CharField(max_length=30, blank=True)


class Goal(models.Model):
    Name = models.CharField(max_length=30)
    Title = models.TextField(blank=True)
    Priority = models.CharField(max_length=2, choices=PRIORITY_CHOICES, default="T")
    Status = models.CharField(max_length=2, choices=STATUS_CHOICES, default="P")
    Category = models.ForeignKey(Category, on_delete=models.SET_NULL, blank=True, null=True)
    Group = models.ForeignKey(Group, on_delete=models.SET_NULL,  blank=True, null=True)
    Date_create = models.DateField(auto_now_add=True)
    Date_start = models.DateField()
    Date_end = models.DateField()

    def add(self):
        self.Date_create = timezone.now()
        self.save()
