from rest_framework import serializers
from .models import HealthMetric
from .models import UserProfile  # import if in same app, otherwise adjust import

class HealthMetricSerializer(serializers.ModelSerializer):
    # Add computed fields
    systolic_status = serializers.SerializerMethodField()
    diastolic_status = serializers.SerializerMethodField()

    class Meta:
        model = HealthMetric
        fields = '__all__'  # includes all model fields
        # + you can add computed fields by listing them explicitly:
        extra_fields = ['systolic_status', 'diastolic_status']

    def get_systolic_status(self, obj):
        """Return whether systolic BP is in target range."""
        try:
            profile = obj.user.userprofile
        except UserProfile.DoesNotExist:
            return None

        if profile.target_systolic is not None and obj.systolic is not None:
            return "high" if obj.systolic > profile.target_systolic else "normal"
        return None

    def get_diastolic_status(self, obj):
        """Return whether diastolic BP is in target range."""
        try:
            profile = obj.user.userprofile
        except UserProfile.DoesNotExist:
            return None

        if profile.target_diastolic is not None and obj.diastolic is not None:
            return "high" if obj.diastolic > profile.target_diastolic else "normal"
        return None

    def to_representation(self, instance):
        """Ensure extra fields are included."""
        rep = super().to_representation(instance)
        rep['systolic_status'] = self.get_systolic_status(instance)
        rep['diastolic_status'] = self.get_diastolic_status(instance)
        return rep
