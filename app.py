from flask import Flask, render_template, request, jsonify
import random

app = Flask(__name__)

# Initial devices state
devices = {
    "tv": "off",
    "lights": "off",
    "fan": "off",
    "ac": "off",
    "speakers": "off",
    "door_lock": "locked",
    "camera": "off",
    "doorbell": "off",
    "fire_alarm": "off",
    "smoke_detector": "off",
    "vacuum_cleaner": "off",
    "washing_machine": "off",
    "microwave": "off",
    "fridge": "off",
    "coffee_maker": "off",
    "window_curtains": "closed",
    "air_purifier": "off",
    "humidifier": "off",
    "alarm_clock": "off",
    "temperature": "22"
}

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.json.get('message')
    print(f"User message: {user_message}")  # Debugging

    # Default response
    response = "Sorry, I couldn't understand that."
    
    # Check user message for device commands
    if 'tv' in user_message.lower():
        devices["tv"] = "on" if devices["tv"] == "off" else "off"
        response = f"TV turned {devices['tv']}"
    
    elif 'lights' in user_message.lower():
        devices["lights"] = "on" if devices["lights"] == "off" else "off"
        response = f"Lights turned {devices['lights']}"
    
    elif 'fan' in user_message.lower():
        devices["fan"] = "on" if devices["fan"] == "off" else "off"
        response = f"Fan turned {devices['fan']}"
    
    elif 'ac' in user_message.lower():
        devices["ac"] = "on" if devices["ac"] == "off" else "off"
        response = f"AC turned {devices['ac']}"
    
    elif 'speakers' in user_message.lower():
        devices["speakers"] = "on" if devices["speakers"] == "off" else "off"
        response = f"Speakers turned {devices['speakers']}"
    
    elif 'door lock' in user_message.lower():
        devices["door_lock"] = "unlocked" if devices["door_lock"] == "locked" else "locked"
        response = f"Door lock is now {devices['door_lock']}"
    
    elif 'camera' in user_message.lower():
        devices["camera"] = "on" if devices["camera"] == "off" else "off"
        response = f"Camera turned {devices['camera']}"
    
    elif 'doorbell' in user_message.lower():
        devices["doorbell"] = "on" if devices["doorbell"] == "off" else "off"
        response = f"Doorbell turned {devices['doorbell']}"
    
    elif 'fire alarm' in user_message.lower():
        devices["fire_alarm"] = "on" if devices["fire_alarm"] == "off" else "off"
        response = f"Fire alarm turned {devices['fire_alarm']}"
    
    elif 'smoke detector' in user_message.lower():
        devices["smoke_detector"] = "on" if devices["smoke_detector"] == "off" else "off"
        response = f"Smoke detector turned {devices['smoke_detector']}"
    
    elif 'vacuum cleaner' in user_message.lower():
        devices["vacuum_cleaner"] = "on" if devices["vacuum_cleaner"] == "off" else "off"
        response = f"Vacuum cleaner turned {devices['vacuum_cleaner']}"
    
    elif 'washing machine' in user_message.lower():
        devices["washing_machine"] = "on" if devices["washing_machine"] == "off" else "off"
        response = f"Washing machine turned {devices['washing_machine']}"
    
    elif 'microwave' in user_message.lower():
        devices["microwave"] = "on" if devices["microwave"] == "off" else "off"
        response = f"Microwave turned {devices['microwave']}"
    
    elif 'fridge' in user_message.lower():
        devices["fridge"] = "on" if devices["fridge"] == "off" else "off"
        response = f"Fridge turned {devices['fridge']}"
    
    elif 'coffee maker' in user_message.lower():
        devices["coffee_maker"] = "on" if devices["coffee_maker"] == "off" else "off"
        response = f"Coffee maker turned {devices['coffee_maker']}"
    
    elif 'window curtains' in user_message.lower():
        devices["window_curtains"] = "opened" if devices["window_curtains"] == "closed" else "closed"
        response = f"Window curtains are now {devices['window_curtains']}"
    
    elif 'air purifier' in user_message.lower():
        devices["air_purifier"] = "on" if devices["air_purifier"] == "off" else "off"
        response = f"Air purifier turned {devices['air_purifier']}"
    
    elif 'humidifier' in user_message.lower():
        devices["humidifier"] = "on" if devices["humidifier"] == "off" else "off"
        response = f"Humidifier turned {devices['humidifier']}"
    
    elif 'alarm clock' in user_message.lower():
        devices["alarm_clock"] = "on" if devices["alarm_clock"] == "off" else "off"
        response = f"Alarm clock turned {devices['alarm_clock']}"
    
    elif 'temperature' in user_message.lower():
        # Optionally, you could set the temperature value based on user's input
        response = f"Current temperature is {devices['temperature']}°C"
    
    # Return response with current device statuses
    return jsonify({"response": response, "devices": devices})

if __name__ == '__main__':
    app.run(debug=True)
