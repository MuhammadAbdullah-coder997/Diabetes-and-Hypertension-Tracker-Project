from django.contrib import admin
from .models import HealthMetric

@admin.register(HealthMetric)
class HealthMetricAdmin(admin.ModelAdmin):
    list_display = ('user', 'date', 'systolic', 'diastolic', 'fasting_glucose', 'weight', 'height', 'bmi')
    readonly_fields = ('bmi',)

    def get_readonly_fields(self, request, obj=None):
        # Ensures bmi is always read-only
        return self.readonly_fields

    def save_model(self, request, obj, form, change):
        # Forces BMI recalculation
        obj.save()
