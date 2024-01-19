from django.db import models

class Authority(models.Model):
    name = models.CharField(max_length=15, blank=True)
    full_name = models.CharField(max_length=255, blank=True)

    def __str__(self) -> str:
        return self.name
    
    class Meta:
        ordering = ["name"]
        verbose_name_plural = "Authorities"

class Code(models.Model):
    authority = models.ForeignKey(
        Authority, on_delete=models.PROTECT, related_name="chapter", blank=True)
    title = models.CharField(max_length=15, blank=True)
    full_title = models.CharField(max_length=255, blank=True)

    def __str__(self) -> str:
        return self.title

    class Meta:
        ordering = ["title"]

class Chapter(models.Model):
    code = models.ForeignKey(
        Code, on_delete=models.PROTECT, related_name="chapter", blank=True)
    number = models.CharField(max_length=55, blank=True)
    title = models.CharField(max_length=55, blank=True)
    full_title = models.CharField(max_length=255, blank=True)

    def __str__(self) -> str:
        return f"{self.number} {self.title}"
    
    class Meta:
        ordering = ["title"]

class Section(models.Model):
    chapter = models.ForeignKey(
        Chapter, on_delete=models.PROTECT, related_name="section", blank=True)
    number = models.CharField(max_length=55, blank=True)
    title = models.CharField(max_length=55, blank=True)
    full_title = models.CharField(max_length=255, blank=True)

    def __str__(self) -> str:
        return f"{self.number} {self.title}"
    
    class Meta:
        ordering = ["title"]

class Requirement(models.Model):
    section = models.ForeignKey(
        Section, on_delete=models.PROTECT, related_name="requirement", blank=True)
    title = models.CharField(max_length=55, blank=True)
    text = models.CharField(max_length=255, blank=True)
    answer = models.CharField(max_length=255, blank=True)

    def __str__(self) -> str:
        return f"{self.section} {self.title}"
    
    class Meta:
        ordering = ["title"]
