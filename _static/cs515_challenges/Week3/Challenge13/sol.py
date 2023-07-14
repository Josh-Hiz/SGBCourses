def custom_blue_filter(img, top_left, height, width):
    for row in range(top_left[0], top_left[0]+height):
        for col in range(top_left[1], top_left[1]+width):
            px = img[row][col]
            img[row][col] = (0, 0, px[2])