def red_filter(img):
    copy = []
    for row in range(len(img)):
        copy.append([])
        for col in range(len(img[row])):
            px = img[row][col]
            copy[row].append((px[0],0,0))
    return copy