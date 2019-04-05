from django.contrib import admin
from mybuildings.models import SensorData,Floor, Room


class SensorView(admin.ModelAdmin):
	list_display = ('data_id','time_stamp','sensor_name','power')
	list_filter = ['sensor_name']

admin.site.register(SensorData, SensorView)

admin.site.register(Floor)
admin.site.register(Room)