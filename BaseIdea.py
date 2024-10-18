import time
import random

class TrafficLightControl:
    def __init__(self):
        self.lights = {'A1': 'red', 'A2': 'red', 'B1': 'red', 'B2': 'red'}
        self.traffic_data = {'A1': {'count': 0, 'average_distance': 0},
                             'A2': {'count': 0, 'average_distance': 0},
                             'B1': {'count': 0, 'average_distance': 0},
                             'B2': {'count': 0, 'average_distance': 0}}
        self.weather_condition = 'clear'  # Options: 'clear', 'rain', 'storm'
    
    def update_traffic_data_randomly(self):
        """Randomly updates the traffic data for all lanes."""
        for lane in self.traffic_data:
            count = random.randint(0, 20)  # Random number of cars between 0 and 20
            average_distance = random.uniform(5, 10)  # Random distance between 1 and 30 meters
            self.traffic_data[lane] = {'count': count, 'average_distance': average_distance}

    def update_weather_randomly(self):
        """Randomly updates the weather condition."""
        self.weather_condition = random.choice(['clear', 'rain', 'storm'])

    def calculate_green_time(self, lane):
        """
        Calculates the green light duration based on traffic volume and distance.
        This formula ensures that green time scales reasonably with the number of cars.
        """
        count = self.traffic_data[lane]['count']
        average_distance = self.traffic_data[lane]['average_distance']

        # Base green time calculation
        base_time = 10  # Minimum green light duration in seconds
        max_time = 90  # Maximum green light duration in seconds

        # Calculate traffic density factor: lower distance means higher density
        density_factor = max(1, (30 - average_distance) / 30)

        # Green time depends on the number of cars and density factor
        green_time = base_time + (count * density_factor * 2)

        # Ensure the green time is within the allowed range
        green_time = min(max(base_time, green_time), max_time)

        return green_time

    def adjust_for_weather(self):
        """Adjusts the light timing based on the current weather conditions."""
        if self.weather_condition == 'rain':
            return 10  # Add an extra 10 seconds if it's raining
        elif self.weather_condition == 'storm':
            return 15  # Add an extra 15 seconds if it's storming
        else:
            return 0  # No adjustment for clear weather

    def switch_light(self, lane, duration):
        """Switches the light for a specified lane to green for the duration."""
        self.lights[lane] = 'green'
        print(f"Switching lane {lane} to green for {duration} seconds.")
        time.sleep(duration)
        self.lights[lane] = 'red'
        print(f"Switching lane {lane} back to red.")

    def control_traffic(self):
        """Main logic for controlling traffic lights based on volume, distance, weather, and priority."""
        while True:  # Infinite loop to simulate continuous traffic control
            self.update_traffic_data_randomly()
            self.update_weather_randomly()

            for lane, data in self.traffic_data.items():
                count = data['count']
                avg_distance = data['average_distance']

                print(f"\nLane {lane}:")
                print(f"  - Number of Cars: {count}")
                print(f"  - Average Distance Between Cars: {avg_distance:.2f} meters")
                print(f"  - Traffic Volume: {'High' if count > 5 else 'Low'}")

                if count > 0:  # Check if there's traffic in the lane
                    green_time = self.calculate_green_time(lane)
                    weather_adjustment = self.adjust_for_weather()
                    total_duration = green_time + weather_adjustment

                    print(f"  - Calculated Green Time (based on traffic): {green_time:.2f} seconds")
                    print(f"  - Weather Adjustment: {weather_adjustment} seconds (Current Weather: {self.weather_condition})")
                    print(f"  - Total Green Light Duration for {lane}: {total_duration:.2f} seconds")

                    self.switch_light(lane, total_duration)
                else:
                    print(f"  - No traffic detected on lane {lane}. Waiting for the next check...")
                    time.sleep(2)  # Short wait before checking again

# Example Usage
control_system = TrafficLightControl()
control_system.control_traffic()

