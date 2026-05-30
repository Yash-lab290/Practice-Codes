def calculate_max_boxes(almirah_dims, box_dims):
    """Calculates the maximum number of boxes that can fit in an almirah,

    allowing for 3D rotation of the boxes.

    Parameters:
    almirah_dims (tuple): (length, width, height) of the almirah.
    box_dims (tuple): (length, width, height) of a single box.

    Returns:
    int: Maximum number of boxes.
    """
    from itertools import permutations

    # Unpack almirah dimensions
    al_l, al_w, al_h = almirah_dims

    max_boxes = 0

    # Test all 6 possible 3D orientation permutations for the box
    for box_orient in permutations(box_dims):
        b_l, b_w, b_h = box_orient

        # Calculate how many boxes fit along each axis
        fit_l = al_l // b_l
        fit_w = al_w // b_w
        fit_h = al_h // b_h

        # Total boxes for this orientation
        total_boxes = fit_l * fit_w * fit_h

        # Keep the maximum configuration found
        if total_boxes > max_boxes:
            max_boxes = total_boxes

    return max_boxes


# Example usage:
# Almirah: 100cm x 80cm x 200cm
# Box: 30cm x 25cm x 40cm
almirah = (100, 80, 200)
box = (30, 25, 40)

result = calculate_max_boxes(almirah, box)
print(f"Maximum number of boxes that can fit: {result}")
