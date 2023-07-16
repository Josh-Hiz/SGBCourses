def longest_lines(f):
    contents = open(f).read().split('\n')
    
    longest = max(map(lambda l: len(l), contents))

    return list(filter(lambda line: len(line) == longest, contents))