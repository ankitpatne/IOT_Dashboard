# IoT Dashboard

This is a Django-based web application for an IoT (Internet of Things) Dashboard. It allows users to monitor sensor data from various stations.

## Live Demo

The project is hosted on PythonAnywhere and can be accessed [here](https://iotcontroldashboard.pythonanywhere.com/).

## Screenshots
![image](https://github.com/ankitpatne/IOT_Dashboard/assets/50258606/dbe61f81-8223-4018-8dd0-9424189394f3)
<br><br>
![image](https://github.com/ankitpatne/IOT_Dashboard/assets/50258606/35d548e7-e914-4a88-b51c-f892c52c5554)



## Features

- User authentication: Users can sign up, log in, and log out.
- Sensor data monitoring: Each station's sensor data is displayed on the dashboard.
- Admin access: Users with staff status can access the Django admin page.

## Installation

1. Clone this repository.
2. Navigate to the project directory.
3. Create a virtual environment: `python -m venv myenv`
4. Activate the virtual environment: `source myenv/bin/activate` (Linux/Mac) or `myenv\Scripts\activate` (Windows)
5. Install the dependencies: `pip install -r requirements.txt`
6. Run the migrations: `python manage.py migrate`
7. Start the development server: `python manage.py runserver`

## Usage

Open your web browser and navigate to `http://localhost:8000` to see the application in action.

## Scheduled Tasks

The application includes a Django management command (`generate_data`) that generates sensor data for each station. This command can be run manually or scheduled to run at regular intervals.

## Contributing

Contributions are welcome. Please open an issue to discuss your idea or submit a pull request.
