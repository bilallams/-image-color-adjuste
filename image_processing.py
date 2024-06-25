from PIL import Image

def process_image(image, red, green, blue):
    # Calculate alpha for blending
    alpha = (abs(red) + abs(green) + abs(blue)) / (3 * 255)

    # Create a new image filled with the average color
    avg_color = (
        255 if red > 0 else 0,
        255 if green > 0 else 0,
        255 if blue > 0 else 0
    )
    filtered_image = Image.new('RGB', image.size, avg_color)

    # Blend the original image with the filtered image
    blended_image = Image.blend(image, filtered_image, alpha)
    return blended_image
