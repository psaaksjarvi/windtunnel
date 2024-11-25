#include "HX711.h"

// Pin definitions for load cells
#define DOUT_PIN1  3  // Data output pin for the first load cell (weight)
#define CLK_PIN1   2  // Clock pin for the first load cell (weight)
#define DOUT_PIN2  4  // Data output pin for the second load cell (drag force)
#define CLK_PIN2   5  // Clock pin for the second load cell (drag force)

// Pin definition for wind sensor
#define WIND_SENSOR_PIN A1  // Analog pin for the wind sensor

// Constants for wind sensor
const float VOLT_MAX = 2.0;  // Maximum voltage output from the wind sensor
const float VOLT_MIN = 0.40;  // Minimum voltage output from the wind sensor
const float VOLT_CONVERSION_CONSTANT = 0.004882814;  // Conversion constant to convert sensor value to voltage
const float WIND_SPEED_MAX = 32;  // Maximum wind speed corresponding to VOLT_MAX
const int READINGS_COUNT = 5;  // Number of readings to average

// Calibration factors for load cells
const float CALIBRATION_FACTOR1 = -8434;  // Calibration factor for the first load cell (weight)
const float CALIBRATION_FACTOR2 = -8434;  // Calibration factor for the second load cell (drag force)

// HX711 instances
HX711 scale1;  // First load cell (weight)
HX711 scale2;  // Second load cell (drag force)

// Variables for wind sensor
float sensorVolt = 0.0;  // Stores the converted voltage from the wind sensor
float windSpeed = 0.0;  // Stores the calculated wind speed

void setup() 
{
  Serial.begin(115200);  // Initialize serial communication at 115200 baud

  // Initialize the first load cell
  scale1.begin(DOUT_PIN1, CLK_PIN1);
  scale1.set_scale();  // Set scale to default
  scale1.tare();  // Reset the scale to 0
  delay(5);  // Short delay to ensure stability
  scale1.set_scale(CALIBRATION_FACTOR1);  // Apply calibration factor

  // Initialize the second load cell
  scale2.begin(DOUT_PIN2, CLK_PIN2);
  scale2.set_scale();  // Set scale to default
  scale2.tare();  // Reset the scale to 0
  delay(5);  // Short delay to ensure stability
  scale2.set_scale(CALIBRATION_FACTOR2);  // Apply calibration factor
}

void loop() 
{
  // Get and print the weight
  float weight = getWeight();
  Serial.print("Mass: ");
  Serial.println(weight);

  // Get and print the drag force
  float drag = getDragForce();
  Serial.print("Drag: ");
  Serial.println(drag);

  // Get and print the wind speed
  float windSpeed = getWindSpeed();
  Serial.print("Velocity: ");
  Serial.println(windSpeed);
}

// Function to get the average weight from the first load cell
float getWeight() 
{
  float totalWeight = 0.0;
  // Take multiple readings for averaging
  for(int i = 0; i < READINGS_COUNT; i++) 
  {
    totalWeight += scale1.get_units();
  }
  // Return the average weight
  return abs(totalWeight / READINGS_COUNT);
}

// Function to get the average drag force from the second load cell
float getDragForce() 
{
  float totalDrag = 0.0;
  // Take multiple readings for averaging
  for(int i = 0; i < READINGS_COUNT; i++) 
  {
    totalDrag += scale2.get_units();
  }
  // Return the average drag force
  return abs(totalDrag / READINGS_COUNT) * 100;
}

// Function to get the average wind speed from the wind sensor
float getWindSpeed()
{
  int sensorValue = analogRead(WIND_SENSOR_PIN);  // Read the analog value from the wind sensor
  float voltage = sensorValue * VOLT_CONVERSION_CONSTANT;  // Convert sensor value to voltage
  sensorVolt = voltage;

  // If voltage is below minimum threshold, wind speed is zero
  if (sensorVolt <= VOLT_MIN) 
  {
    return 0.0;
  } 
  else 
  {
    float totalWindSpeed = 0.0;
    // Take multiple readings for averaging
    for (int i = 0; i < READINGS_COUNT; i++) 
    {
      // Calculate wind speed based on sensor voltage
      totalWindSpeed += ((sensorVolt - VOLT_MIN) * WIND_SPEED_MAX / (VOLT_MAX - VOLT_MIN)) * 2.232694;
    }
    // Return the average wind speed
    return abs(totalWindSpeed / READINGS_COUNT);
  }
}
