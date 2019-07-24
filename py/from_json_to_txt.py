import json
from collections import OrderedDict


input_file = "intended_tests.json"
output_file = "intended_tests"

data = {}
with open(input_file, 'r') as fd:
    data = json.load(fd, object_pairs_hook=OrderedDict)

with open(output_file, 'w') as fd:
    for suite in data:
        fd.write('::TestSuite::{} "n/a"\n'.format(suite))
        for module in data[suite]:
            for test in data[suite][module]:
                for subtest in data[suite][module][test]:
                    fd.write('{}.{}.{} "n/a"\n'.format(module, test, subtest))
