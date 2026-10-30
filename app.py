def calculate_rental_cost(hours, hourly_rate):
    if hours <= 0:
        raise ValueError("Hours must be greater than zero")

    if hourly_rate <= 0:
        raise ValueError("Hourly rate must be greater than zero")

    return hours * hourly_rate










