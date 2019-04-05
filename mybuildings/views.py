from django.shortcuts import render
from mybuildings.models import SensorData, Floor, Room
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.shortcuts import redirect
def landing(request):
	if request.method == 'POST':
		if 'username' in request.POST and request.POST['username'] and 'password' in request.POST and request.POST['password']:
			username = request.POST['username']
			password = request.POST['password']
			user = authenticate(username=username, password=password)
			if user is not None:
				if user.is_active:
					
					#return render(request,'visvalize.html')
					return redirect('profile/')
				else:
					context={
					'error':'Sorry the account no longer exist'
					}
					return render(request,'landing.html',context=context)

			else:
				context={
					'error':'Invalid login'
					}
				return render(request,'landing.html',context=context)

		else:
			context={
					'error':'Enter all fields'
					}
			return render(request,'landing.html',context=context)
	else:
		return render(request,'landing.html')
	
'''
def visvalize(request):
	if request.method == 'POST':
		if request.POST.get("tooff"):
			status = request.POST.get("tooff")
		elif request.POST.get("toon"):
			status = request.POST.get("toon")		
		
		SensorData.set_status_of_device(status)
		
		return render(request,'visvalize.html')
		
		
	else:
		context = loadvisvalize()
		return render(request,'visvalize.html', context = context)
'''

def visvalize(request):
	if request.method == 'POST':
		if request.POST.get("floor1"):
			return redirect('floor/1')
		elif request.POST.get("floor0"):
			return redirect('floor/0')



	else:
		context = loadvisvalize()
		return render(request,'visvalize.html', context = context)

def insidefloor(request, offset):
	if request.method == 'POST':
		if request.POST.get("f0v"):
			return redirect('sensor-name/')
		else:
			return HttpResponse("sorry page yet to be designed")

	elif int(offset) == 0:
		floor = Floor.objects.get(floor_name= "Ground Floor")
		context = load_insidefloor(floor)
		return render(request,'floor.html',context = context)

	elif offset ==1:
		floor = Floor.objects.get(floor_name = "First Floor")
		context = load_insidefloor(floor)
		return render(request,'floor.html',context = context)
	else:
		return HttpResponse("sorry page cant load")

def sensor(request, offset, slug):
	if str(slug) =="sensor-name" and int(offset) == 0:
		if request.method == 'POST':
			if request.POST.get("tooff"):
				status = request.POST.get("tooff")
			elif request.POST.get("toon"):
				status = request.POST.get("toon")
			SensorData.set_status_of_device(status)
			status = SensorData.get_status_of_device()
			light = SensorData.objects.get(sensor_name = "light")
			power = 35
			i=0
			energy = 1.3 
			'''
			for lop in light:
				power += lop.power
				energy += lop.power/36000*5
				i+=1
			power = power/i'''
			context = {
			'power': power,
			'status': status,
			'energy':energy,
			}
			return render(request, 'sensor.html', context=context)
		else:
			status = SensorData.get_status_of_device()

			light = SensorData.objects.get(sensor_name = "light")
			power = 35
			i=0
			energy = 1.3
			'''
			for lop in light:
				power += lop.power
				energy += lop.power/36000*5
				i+=1
			power = power/i
			'''
			context = {
			'power': power,
			'status': status,
			'energy':energy,
			}
			return render(request, 'sensor.html',context=context)
	else:
		return HttpResponse("notok")


@csrf_exempt
def getdata(request):
	if request.method == 'POST':    	
		data = request.POST
		
		if data['type'] == 'data':
			floor=Floor.objects.get(floor_name=data['floor'])
			room=Room.objects.get(room_name=data['room'])
			SensorData.objects.create(sensor_name= data['sensor_name'],power=data['power'],floor=floor,room=room)
			return HttpResponse(SensorData.get_status_of_device())

		elif data['type'] == 'update':
			SensorData.set_status_of_device(data['status'])
			return HttpResponse(SensorData.get_status_of_device())

		elif data['type'] == 'status':
			return HttpResponse(SensorData.get_status_of_device())

		
		
	else:
		return HttpResponse(SensorData.get_status_of_device())

'''
		if 'control' in request.POST and request.POST['control']:
			status = request.POST['control']
			SensorData.set_status_of_device(status)
'''
def loadvisvalize():
	average_power = 0
	total_energy = 0
	i=0

	Floor_object = Floor.objects.all()
	allsensor = SensorData.objects.all()
	for looper in allsensor:
		average_power+=looper.power
		total_energy += looper.power/36000*5
		i+=1
		

	average_power=average_power/i

	data={
	'average_power':average_power,	
	'total_energy':total_energy,
	'Floor_object': Floor_object
	}
	return data


#sub_list_energy.append(time)
#		sub_list_energy.append(total_energy)

#		total_energy_chart.append(sub_list_energy)
def load_insidefloor(floor_object):
	floor = floor_object

	rooms = floor.room_set.all()

	power = 0
	energy = 0
	i=0
	sensor = floor.sensordata_set.all()
	for loop in sensor:
		power = loop.power
		energy += loop.power/36000*5
		i+=1

	power = power/i




	context = {
	'Floor': floor.floor_name,
	'Room_object': rooms,
	'power':power,
	'energy': energy,
	}
	return context
