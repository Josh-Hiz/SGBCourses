from challenge import red_square

assert len(red_square) == 3, "# of rows should be 3"
for row in red_square:
    assert len(row) == 3, "# of cols should be 3"

assert red_square[1][1] == (255,255,255), "center should be white"

for i in range(3):
    for j in range(3):
        if i != 1 and j != 1:
            assert red_square[i][j] == (255,0,0), "outside should be red"