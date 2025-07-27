from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class HealthMetric(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    #Date and time
    date = models.DateField()
    measurement_time = models.TimeField(null=True, blank=True)

    # Blood Pressure
    systolic = models.IntegerField(null=True, blank=True)
    diastolic = models.IntegerField(null=True, blank=True)

    # Blood Sugar
    fasting_glucose = models.FloatField(null=True, blank=True)
    post_meal_glucose = models.FloatField(null=True, blank=True)
    hba1c = models.FloatField(null=True, blank=True)
    cgm_reading = models.FloatField(null=True, blank=True)  # Continuous Glucose Monitor

     # Weight & Body Metrics
    weight = models.FloatField(null=True, blank=True)
    height = models.FloatField(null=True, blank=True)  # optional for BMI calculation
    bmi = models.FloatField(null=True, blank=True)

     # Heart Rate
    heart_rate = models.IntegerField(null=True, blank=True)

    # Medication Tracking
    medication_taken = models.CharField(max_length=255, null=True, blank=True)

    # Lifestyle Inputs
    meal_type = models.CharField(max_length=50, null=True, blank=True)  # e.g., breakfast, lunch
    meal_time = models.TimeField(null=True, blank=True)
    exercise_details = models.CharField(max_length=255, null=True, blank=True)
    sleep_hours = models.FloatField(null=True, blank=True)
    stress_level = models.IntegerField(null=True, blank=True)  # 1–10 scale
    alcohol_intake = models.BooleanField(default=False)
    caffeine_intake = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        if self.height and self.weight:
            try:
                height_m = self.height / 100
                self.bmi = round(self.weight / (height_m ** 2), 2)
            except ZeroDivisionError:
                self.bmi = None
        else:
            self.bmi = None
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.user.username} - {self.date}"
