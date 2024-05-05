import random  # Import the random module to generate random numbers

def estimate_pi(num_samples):
    # This function estimates the value of Pi using the Monte Carlo method.
    
    inside_circle = 0  # Counter for points that fall inside the unit circle

    # Loop through the number of samples specified
    for _ in range(num_samples):
        # Generate random x, y coordinates between 0 and 1
        x, y = random.random(), random.random()
        
        # Check if the point (x, y) is inside the unit circle
        # The equation for a circle at the origin with radius 1 is x^2 + y^2 = 1
        # Points are inside if x^2 + y^2 is less than or equal to 1
        if x**2 + y**2 <= 1:
            inside_circle += 1  # Increment the counter if inside the circle

    # The ratio of points inside the circle to the total number of points, times 4,
    # gives an estimation of Pi. This is because the area of the unit circle is πr^2 (π*1^2 = π),
    # and the area of the bounding box (the unit square) is 1*1 = 1. Since we only consider a quarter
    # of the circle, multiplying the ratio by 4 estimates π.
    return 4 * inside_circle / num_samples

if __name__ == "__main__":
    # This block runs when the script is executed directly (not imported as a module).

    # Prompt the user to enter the number of samples to use for Pi estimation
    num_samples = int(input("Enter the number of samples to use for estimating Pi: "))
    
    # Call the function with the user-provided number of samples
    pi_estimate = estimate_pi(num_samples)
    
    # Print the estimated value of Pi
    print(f"Estimated value of Pi: {pi_estimate}")
