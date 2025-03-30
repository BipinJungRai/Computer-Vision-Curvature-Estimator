def convert_curvature_to_meters(curvatures, camera_height_m, focal_length_mm, sensor_width_mm, image_width_px):
    """
    Converts curvature values from pixels^-1 to meters^-1 using the pinhole camera model.
    """
    meters_per_pixel = (sensor_width_mm / 1000) * camera_height_m / ((focal_length_mm / 1000) * image_width_px)
    pixels_per_meter = 1 / meters_per_pixel
    curvatures_meters = [curv / pixels_per_meter for curv in curvatures]
    return curvatures_meters, pixels_per_meter

# TODO: TEST in labs