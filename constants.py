import numpy as np

# engine variables
FORCE_GRAVITY = -9.8
NUM_ITERATIONS = 1000
SLEEP_TIME = 1/60

# motor variables
MAX_MOTOR_FORCE = 25
INPUT_ARRAY_LOWER = 0
INPUT_ARRAY_UPPER = 2*np.pi

# front leg oscillation
AMPLITUDE = np.pi/4
FREQUENCY = 10
PHASE_OFFSET = np.pi

# search variables
NUMBER_OF_GENERATIONS = 25
POPULATION_SIZE = 25

# robot variables
NUM_SENSOR_NEURONS = 4
NUM_MOTOR_NEURONS = 8
MOTOR_JOINT_RANGE = 0.2