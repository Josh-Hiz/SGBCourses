def red_filter(img):
    for row in range(len(img)):
        for col in range(len(img[row])):
            px = img[row][col]
            img[row][col] = (px[0],0,0)