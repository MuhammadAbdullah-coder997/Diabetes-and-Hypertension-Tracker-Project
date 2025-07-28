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
    pulse_pressure = models.IntegerField(null=True, blank=True)

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
    medication_time = models.TimeField(null=True, blank=True)

    # Lifestyle Inputs
    meal_type = models.CharField(max_length=50, null=True, blank=True)  # e.g., breakfast, lunch
    meal_time = models.TimeField(null=True, blank=True)
    exercise_details = models.CharField(max_length=255, null=True, blank=True)
    sleep_hours = models.FloatField(null=True, blank=True)
    stress_level = models.IntegerField(null=True, blank=True)  # 1–10 scale
    alcohol_intake = models.BooleanField(default=False)
    caffeine_intake = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        # Calculate BMI
        if self.height and self.weight:
            try:
                height_m = self.height / 100
                self.bmi = round(self.weight / (height_m ** 2), 2)
            except ZeroDivisionError:
                self.bmi = None
        else:
            self.bmi = None

        # Calculate Pulse Pressure
        if self.systolic is not None and self.diastolic is not None:
            self.pulse_pressure = self.systolic - self.diastolic
        else:
            self.pulse_pressure = None

        # ✅ NEW: Compare with user's target ranges
        if self.user_id:  # Ensure user exists
            try:
                profile = self.user.userprofile
                if (profile.target_systolic and self.systolic and
                    self.systolic > profile.target_systolic):
                    # Example: You could set a flag
                    print("Warning: Systolic above target!")
            except UserProfile.DoesNotExist:
                pass

        super().save(*args, **kwargs)


    def __str__(self):
        return f"{self.user.username} - {self.date}"

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    # Additional fields
    age = models.PositiveIntegerField(null=True, blank=True)
    gender = models.CharField(
        max_length=10,
        choices=[("male", "Male"), ("female", "Female"), ("other", "Other")],
        null=True,
        blank=True
    )

    # Diagnosis
    diabetes_type = models.CharField(
        max_length=20,
        choices=[("type1", "Type 1"), ("type2", "Type 2"), ("gestational", "Gestational"), ("none", "None")],
        default="none"
    )
    hypertension_stage = models.CharField(
        max_length=20,
        choices=[("normal", "Normal"), ("stage1", "Stage 1"), ("stage2", "Stage 2"), ("crisis", "Hypertensive Crisis")],
        default="normal"
    )

    # Target ranges (from doctor)
    target_systolic = models.IntegerField(null=True, blank=True)
    target_diastolic = models.IntegerField(null=True, blank=True)
    target_fasting_glucose = models.FloatField(null=True, blank=True)
    target_post_meal_glucose = models.FloatField(null=True, blank=True)

    def __str__(self):
        return f"Profile of {self.user.username}"