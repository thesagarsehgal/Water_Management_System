# Water_Management_System
Built as a part of ITWS-3 project.
It is the system developed in Django where people can log in and monitor the condition of their plant.
It can be used to remotely monitor the plant and control the water supply and check the health of the plant.
The aim of the project to save plants by minimum use of water and provide automatic irrigation to plants.

### Tech-Stack
- Arduino 
- Raspberry Pi
- Python
- Django
- HTML
- CSS
- JS
- Ajax
- JSON
 
Sensors are attached near the plants and this information is sent to Arduino, which using the GSM module send the data to the server. This data is then collected by the app and the complete info like the soil moisture level, chances of raining, etc. is displayed on the web app using Django. The plants are plotted on the map using Google Map's API. As the soil moisture level drops under a certain value, then using the actuators the motor is switched ON. Also, as soon as the water level gets more than the sufficient value, then using actuators the motor is stopped.        

The data is collected from the sensors and then plot a real-time graph using the sensors data.
