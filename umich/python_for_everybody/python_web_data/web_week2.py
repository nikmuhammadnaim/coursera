import re

# We have to solve for actual_file
sample_file = 'data/regex_sum_42.txt'
actual_file = 'data/regex_sum_233803.txt'

with open(sample_file) as content:
    sample_answer = re.findall('[0-9]+', content.read())

print('Sample answer: {:,}'.format(sum([int(ans) for ans in sample_answer])))

with open(actual_file) as content:
    actual_answer = re.findall('[0-9]+', content.read())

print('Actual answer: {:,}'.format(sum([int(ans) for ans in actual_answer])))
