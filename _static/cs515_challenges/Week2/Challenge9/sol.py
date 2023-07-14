# define quieter_please
def quieter_please(s):
    if not s.islower() and s.isupper():
        return s.lower()
    else: return s