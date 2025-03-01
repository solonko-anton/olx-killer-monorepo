from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from simple_history.admin import SimpleHistoryAdmin

from apps.locations.models import Location


@admin.register(Location)
class LocationAdmin(SimpleHistoryAdmin):
    list_display = ('get_location_name', 'location_type', 'get_region', 'latitude', 'longitude')
    readonly_fields = ('created_at', 'updated_at')
    search_fields = ['city__name', 'village__name']
    show_full_result_count = False

    @admin.display(description=_('Location'), ordering='city__name')
    def get_location_name(self, obj):
        return obj.city.name

    @admin.display(description=_('Region'), ordering='city__region__name')
    def get_region(self, obj):
        return obj.city.region.name

    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        return queryset.select_related('city', 'village', 'city__region').order_by('-created_at')
