import time
import teslajson
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import random


i=0.0
bat_old = 50
key = {"T":[0, "Time (s)",100], "BL":[1, "Battery Level (%)",100], "CC":[2, "Charger Power (kW)",150], "CV":[3, "Charge Voltage (V)",420], "CR":[4, "Charge Rate (miles/hr)",300]}

# Updates car_data.txt in format (time, battery_level, charger_actual_current, charger_voltage, charge_rate(miles/hr))
# this is main place data gets captured from the car
def updateCarData():
	data = v.data_request('charge_state')

	try:
		tNow = round(time.time()-tStart, 2)
		battery_level = round(data['battery_level'], 2)
		#temporary fix
		charger_actual_current = round(data['charger_power'], 2)
		charger_voltage = round(data['charger_voltage'], 2)
		charge_rate = round(data['charge_rate'], 2)
	except:
		print("The car is not connected!")
		battery_level = round(0, 2)
		charger_actual_current = round(0, 2)
		charger_voltage = round(0, 2)
		charge_rate = round(0, 2)

	# Save Data into file for use later
	data_file = open('car_data.txt', 'a')
	T = "" + str(tNow) + "," + str(battery_level) + "," + str(charger_actual_current) + "," + str(charger_voltage) + "," + str(charge_rate)
	data_file.write( T + "\n")
	data_file.close()
	print(T)

#this is only to create fake data for testing purpose
#not used in actual functionning version
def updateCarDataWithRandomData():
	global bat_old
	tNow=round(time.time()-tStart, 2)
	battery_level = round(bat_old + random.uniform(-5,5), 2)
	charger_actual_current = round(random.uniform(0,100), 2)
	charger_voltage = round(random.uniform(0,100), 2)
	charge_rate = round(random.uniform(0,100), 2)
	bat_old = battery_level

	data_file = open('car_data.txt', 'a')
	data_file.write("" + str(tNow) + "," + str(battery_level) + "," + str(charger_actual_current) + "," + str(charger_voltage) + "," + str(charge_rate) + "\n")
	data_file.close()

# Will return x and y lists containing the corresponding values to the parameters
# e.g. getGraphData('T', 'BL') will return lists containing time and battery level values
def getGraphData(x,y):
	graph_data = open('car_data.txt', 'r').read()
	lines = graph_data.split('\n')
	xs=[]
	ys=[]
	for line in lines:
		if len(line) > 1:
			cx, cy = float(line.split(',')[key[x][0]]), float(line.split(',')[key[y][0]])
			xs.append(cx)
			ys.append(cy)
	return xs, ys

# subplots is a dictionary in the form {axis:['x-axis','y-axis']}
def animate(subplots):
	updateCarData()
	for subplot in subplots:
		xs, ys = getGraphData(subplots[subplot][0], subplots[subplot][1])
		subplot.clear()
		subplot.set_ylim([0,key[subplots[subplot][1]][2]])
		subplot.set_title(key[subplots[subplot][0]][1] + " / " + key[subplots[subplot][1]][1])
		subplot.set_xlabel(key[subplots[subplot][0]][1])
		subplot.set_ylabel(key[subplots[subplot][1]][1])
		subplot.plot(xs, ys)

c = teslajson.Connection('technomupet67@gmail.com', password='emmanuell3')
print("Getting Tesla data")

v = c.vehicles[0]
State_online = v['state']

if State_online == 'offline':
 	print("Car is offline, stopping code.")
else:
	print("Good News, Car is Online !")
	scan_time = float(input("How long should the car be monitored for? (in minutes)\n--> "))

	tStart = time.time()
	print("Trying to erase previous files")

	# Erase the contents of the file.
	data_file = open('car_data.txt', 'w')
	data_file.write('')
	data_file.close()

	fig = plt.figure()

	ax1 = fig.add_subplot(2,2,1)
	ax2 = fig.add_subplot(2,2,2)
	ax3 = fig.add_subplot(2,2,3)
	ax4 = fig.add_subplot(2,2,4)

	# loop until time specified has past
	# wait a few seconds before updating the charts and starting again
	while time.time()-tStart<scan_time*60:
		animate({ax1:['T','BL'], ax2:['T','CC'], ax3:['T','CV'], ax4:['T','CR']})
		print("Posted new data.")
		plt.tight_layout()
		plt.pause(5)

	print("Done!")
	fig.savefig('plot.png')
	plt.show()



