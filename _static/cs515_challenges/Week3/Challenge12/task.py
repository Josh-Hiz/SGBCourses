from challenge import red_filter_pixel

assert red_filter_pixel((0,0,0)) == (0,0,0), "ok on black"
assert red_filter_pixel((255,255,255)) == (255,0,0), "ok on white"
assert red_filter_pixel((128,128,128)) == (128,0,0), "ok on gray"
assert red_filter_pixel((0,0,255)) == (0,0,0), "ok on blue"