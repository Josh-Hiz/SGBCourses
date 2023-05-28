#DO NOT EDIT THE CODE BELOW
import unittest
import challenge as variable

class SimpleTestCase(unittest.TestCase):
    def testOthers(self):
        defs = [v for v in dir(variable) if v[0] != '_']
        assert 'num_profs' in defs, 'Could not find num_profs definition'
        assert 'num_tas' in defs, 'Could not find num_tas definition'
        for f in ['num_profs', 'num_tas', 'num_students']:
            if f in defs:
                defs.remove(f)
        assert len(defs) == 0, f'Found extra definitions: {", ".join(defs)}'
        assert variable.num_profs == 1, f'Expected 1 prof, got {variable.num_profs}'
        assert variable.num_tas == 2, f'Expected 2 TAs; got {variable.num_tas}'
        
    def testStudents(self):
        assert 'num_students' in dir(variable), f'Could not find num_students definition'
        assert variable.num_students == 45, f'Expected 45 students; got {variable.num_students}'

unittest.main(exit=False)