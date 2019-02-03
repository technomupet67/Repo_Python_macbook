#
#
# This version works directly from Mac OSX on Laptop
#
#



import time
import os
import teslajson
import yagmail


__Author__ = "Made By Oli Dehon Sept.2018"
__Updated__= "Updated Feb. 2019."

# for sending emails
receiver = "3zeed.ltd@gmail.com"
body = "Data from my Tesla"
# filename = ["car_email_data.txt", "plot_old.png"]
filename = "Tesla_email_data.txt"
send_e = True

# cost in pence
cost_per_kw = 14.99




c = teslajson.Connection('technomupet67@gmail.com', password='emmanuell3')
print('Retreiving Data from Tesla')

v = c.vehicles[0]
State_online = v['state']
if State_online == 'offline':
    print("Car is offline")
else:
    
    # might try a few others
    #img = Image.open("T_Logo.jpg")
    # printer.printImage(img)

    # Erase the contents of the file.
    data_file = open(filename, 'w')
    data_file.write('')
    data_file.close()

    # Create new file.
    data_file = open(filename, 'a')
    data_file.write("" + "\n")
    
    T = time.strftime("%d/%m/%Y") + " - " + time.strftime("%H:%M:%S")
    
    print('Connecting to Tesla')
    
   
    print("For Car : ")
    print(v['vin'])
    
    print('Getting Vehicle State')
    data = v.data_request('vehicle_state')
    
    print('Getting Charge State')
    data2 = v.data_request('charge_state')
    
    print('Getting Climate Settings')
    data3 = v.data_request('climate_state')
    
    print('Getting Driving and Location')
    data4 = v.data_request('drive_state')
    
    print('Starting output')
    
    T = "Vehicle Name: %s" %(data['vehicle_name'])
    print(T)
    data_file.write( T + "\n")
    
    T = "Car Version: %s" %(data['car_version'])
    print(T)
    data_file.write( T + "\n")
    
    miles = data['odometer']
    km = miles * 1.609
    T = "Odometer : %.2f Miles" %(miles)
    print(T)
    data_file.write( T + "\n")
    
    T = "Odometer : %.2f Km" %(km)
    print(T)
    data_file.write( T + "\n")
    
    T = "Locked ?: %s" %(data['locked'])
    print(T)
    data_file.write( T + "\n"+ "\n"+ "\n"+ "======= Charge Sate  ========"+ "\n")
    print("")
    print("")
    print("======= Charge Sate  ========")
    
    T = "Charging State: %s" %(data2['charging_state'])
    print(T)
    data_file.write( T + "\n")
    
    current = data2['charger_actual_current']
    T = "Charger Actual Current: %s amps" %(current)
    print(T)
    data_file.write( T + "\n")
    
    volts = data2['charger_voltage']
    T = "Charger Voltage: %s" %(volts)
    print(T)
    data_file.write( T + "\n")
    
    watts = current * volts
    T = "Charger: %s watts" %(watts)
    print(T)
    data_file.write( T + "\n")
    d = data2['charger_power']
    
    if d is not None:
        T = "Charger Power KW: %.1f" %(d)
        print(T)
        data_file.write( T + "\n")


    d = data2['charge_rate']
    T = "Charge Rate: %s miles/hr" %(d)
    print(T)
    data_file.write( T + "\n")
    
    d = d * 1.609
    T = "Charge Rate: %.1f km/hr" %(d)
    print(T)
    data_file.write( T + "\n")
    
    
    T = "Charge Limit: %s" %(data2['charge_limit_soc'])
    print(T)
    data_file.write( T + "\n")

    T = "Battery level: %s" %(data2['battery_level'])
    print(T)
    data_file.write( T + "\n")

    T = "Battery usable level: %s" %(data2['usable_battery_level'])
    print(T)
    data_file.write( T + "\n")

    time_left = data2['time_to_full_charge']
    T = "Time to full charge: %s" %(time_left)
    print(T)
    data_file.write( T + "\n")

    total_cost = time_left * watts /1000 * cost_per_kw / 100
    T = "Cost to full charge: %.2f" %(total_cost)
    print(T)
    data_file.write( T + "\n")
    
    d = data2['battery_range']
    T = "Battery Range : %.1f Miles" %(d)
    print(T)
    data_file.write( T + "\n")
    d = d * 1.609
    BR = d
    T = "Battery Range : %.1f Kilometers" %(d)
    print(T)
    data_file.write( T + "\n")
    
    d = data2['ideal_battery_range']
    T = "Ideal Batt. range: %.1f miles" %(d)
    print(T)
    data_file.write( T + "\n")
    d = d * 1.609
    IBR = d
    T = "Ideal Batt. range: %.1f km" %(d)
    print(T)
    data_file.write( T + "\n")
    
    d = data2['est_battery_range']
    T = "Estimated range: %.1f miles" %(d)
    print(T)
    data_file.write( T + "\n")
    d = d * 1.609
    EBR = d
    T = "Estimated range: %.1f km" %(d)
    print(T)
    data_file.write( T + "\n")
    
    d = 100 * (EBR / BR)
    T = "Estimated versus Battery Range %.1f percent" %(d)
    print(T)
    data_file.write( T + "\n")
    
    d = 100 * (EBR / IBR)
    T = "Estimated versus Ideal Battery Range %.1f percent" %(d)
    print(T)
    data_file.write( T + "\n")
    
    T = "Charge energy added: %s" %(data2['charge_energy_added'])
    print(T)
    data_file.write( T + "\n")
    
    d = data2['charge_energy_added'] * cost_per_kw / 100
    T = "GBP energy added: %.2f" %(d)
    print(T)
    data_file.write( T + "\n")


    d = data2['charge_miles_added_ideal']
    T = "Ideal Miles added: %.1f" %(d)
    print(T)
    data_file.write( T + "\n")

    d = d * 1.609
    T = "Ideal Km added: %.1f" %(d)
    print(T)
    data_file.write( T + "\n")

    d = data2['charge_miles_added_rated']
    T = "Rated Miles added: %.1f" %(d)
    print(T)
    data_file.write( T + "\n")
    d = d * 1.609
    T = "Rated Km added: %.1f" %(d)
    print(T)
    data_file.write( T + "\n"+ "\n"+ "\n"+ "====== Climate Sate  =======" +"\n")
    
    print("")
    print("")
    print("====== Climate Sate  =======")
    
    T = "Is Climate on ?: %s" %(data3['is_climate_on'])
    print(T)
    data_file.write( T + "\n")
    
    T = "Temp setting: %.1f" %(data3['driver_temp_setting'])
    print(T)
    data_file.write( T + "\n")

    if not (data3['inside_temp'] is None):
    	T = "Inside temp: %.1f" %(data3['inside_temp'])
    	print(T)
    	data_file.write( T + "\n")
    else :
    	T = "Inside temp: unavailable"
    	print(T)
    	data_file.write( T + "\n")

    T = "Outside temp: %.1f" %(data3['outside_temp'])
    print(T)
    data_file.write( T + "\n"+ "\n"+ "\n"+ "=== Driving & Location  ====" +"\n")

    print("")
    print("")
    print("=== Driving & Location  ====")

    T = "Power: %s" %(data4['power'])
    print(T)
    data_file.write( T + "\n")


    T = "Longitude: %.5f" %(data4['longitude'])
    print(T)
    data_file.write( T + "\n")


    T = "Latitude: %.5f" %(data4['latitude'])
    print(T)
    data_file.write( T + "\n")


    T = "Speed: %s" %(data4['speed'])
    print(T)
    data_file.write( T + "\n")


    T = "Heading: %s" %(data4['heading'])
    print(T)
    data_file.write( T + "\n")

    data_file.close()

    if send_e is True:
        print("")
        print("Sending email of Data...")
        yag = yagmail.SMTP("technomupet67@gmail.com", "piTHeRiu67")
        yag.send(to=receiver, subject="Model X - Data",contents=body, attachments=filename,)


print(__Author__)
print(__Updated__)
print('All Finished !')

