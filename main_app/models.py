from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    github_url = models.URLField(blank=True, null=True)
    order = models.PositiveIntegerField(default=0, help_text="Order in which to display projects")

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['order', 'title']

class Skill(models.Model):
    name = models.CharField(max_length=100)
    order = models.PositiveIntegerField(default=0, help_text="Order in which to display skills")

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['order', 'name']

class Experience(models.Model):
    date_range = models.CharField(max_length=50, help_text="e.g., '2025', '2022-2023'")
    title = models.CharField(max_length=200)
    description = models.TextField()
    order = models.PositiveIntegerField(default=0, help_text="Use for chronological sorting (e.g., higher numbers for more recent)")

    def __str__(self):
        return f"{self.date_range} - {self.title}"

    class Meta:
        ordering = ['-order'] # Default to reverse chronological (most recent first)
