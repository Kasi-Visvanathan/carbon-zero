from django.db import models
import datetime

class SensorData(models.Model):
	status_of_device = False
	sensor_name = models.CharField(max_length =200)
	data_id = models.AutoField(primary_key=True)
	time_stamp = models.DateTimeField(auto_now_add=True)
	power = models.IntegerField()
	floor = models.ForeignKey('Floor', on_delete=models.CASCADE, null=True)
	room = models.ForeignKey('Room', on_delete=models.CASCADE, null=True)
	#current = models.IntegerField()
	#voltage = models.IntegerField()
	#status_of_device = models.BooleanField(default=False)

	def __str__(self):
		return self.sensor_name

	class Meta:
		ordering = ['data_id']
	
	@staticmethod
	def get_status_of_device():
		return SensorData.status_of_device

	@staticmethod
	def set_status_of_device(value):
		SensorData.status_of_device = value

class Floor(models.Model):
	floor_name = models.CharField(max_length=50, default="floor")

	def __str__(self):
		return self.floor_name

class Room(models.Model):	
	room_name = models.CharField(max_length = 50, default="room")
	floor = models.ForeignKey('Floor', on_delete=models.CASCADE)

	def __str__(self):
		return self.room_name
		



