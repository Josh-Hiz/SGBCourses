# N[not P][ST][not P]
# This function will always return an answer or an error
# so this is a pretty simple for loop in O(N)
def find_nglycosylation_motif(lst):
    for i in range(len(lst)):
        if i + 3 >= len(lst):
            raise ValueError("N-glycosylation motif not found")
        if lst[i] == 'N' and lst[i+1] != 'P' and (lst[i+2] == 'S' or lst[i+2]=='T') and lst[i+3] != 'P':
            return i

print(find_nglycosylation_motif(list('MNPSNTTT')))