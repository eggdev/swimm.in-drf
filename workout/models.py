import datetime
from django.db import models

# Strokes will be needed in some interesting capacity
# How do you do make this easy to add numerous strokes to one set?
STROKES = (
    ("free", "Freestyle"),
    ("back", "Backstroke"),
    ("breast", "Breaststroke"),
    ("fly", "Butterfly"),
    ("im", "IM"),
    ("choice", "Choice"),
    ("kick", "Kick"),
)

# Equipment should be added by the coach, maybe it comes pre-baked with board, bouy, paddles, snorkel.
# Can select more than one, no validation on that cause who cares
EQUIPMENT = (
    ("none", "None"),
    ("kickboard", "Kickboard"),
    ("bouy", "Pull Bouy"),
    ("paddles", "Paddles"),
    ("snorkel", "Snorkel"),
)


class Set(models.Model):
    repetitions = models.CharField(max_length=100, default="")
    distance = models.CharField(max_length=100, default="")
    interval = models.CharField(max_length=100, default="")

    stroke = models.CharField(max_length=100, choices=STROKES, default="free")
    equipment = models.CharField(max_length=100, choices=EQUIPMENT, default="none")

    def __str__(self):
        return f"{self.repetitions} x {self.distance} on {self.interval}"

    class Meta:
        ordering = ["id"]
