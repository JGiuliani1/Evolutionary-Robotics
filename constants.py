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