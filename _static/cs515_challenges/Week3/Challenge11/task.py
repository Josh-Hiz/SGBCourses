from challenge import checker

try:
    
    assert checker == [[(255,0,0), (255,255,255), (255,0,0), (255,255,255), (255,0,0)],
            [(255,255,255), (255,0,0), (0,0,0), (0,0,0), (255,255,255)],
            [(255,0,0), (255,255,255), (0,0,0), (0,0,0), (255,0,0)]]
    
    print("Success!")
except AssertionError as e:
    print(e)