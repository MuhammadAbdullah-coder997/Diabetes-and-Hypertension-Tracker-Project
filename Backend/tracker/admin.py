from django.contrib import admin
from .models import HealthMetric, UserProfile

@admin.register(HealthMetric)
class HealthMetricAdmin(admin.ModelAdmin):
    list_display = ('user', 'date', 'systolic', 'diastolic','pulse_pressure', 'fasting_glucose', 'weight', 'height', 'bmi')
    readonly_fields = ('bmi',)

    def get_readonly_fields(self, request, obj=None):
        # Ensures bmi is always read-only
        return self.readonly_fields

    def save_model(self, request, obj, form, change):
        # Forces BMI recalculation
        obj.save()

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('age', 'gender', 'diabetes_type', 'hypertension_stage', 'target_systolic', 'target_diastolic', 'target_fasting_glucose', 'target_post_meal_glucose')
