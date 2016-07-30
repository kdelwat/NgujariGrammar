#!/usr/bin/env python

from pandocfilters import toJSONFilter, RawBlock


def shrink_list(pandoc_list):
    '''Convert crazy pandoc nested list of Str and Space into
    a nice string.'''
    string = ''
    for item in pandoc_list:
        if item['t'] == 'Str':
            string += item['c']
        elif item['t'] == 'Space':
            string += ' '
    return string


def create_example(example_list):
    examples = [line.strip() for line in shrink_list(example_list).split(',')]
    target = '<div class="example-target">{0}</div>'.format(examples[0])
    gloss = '<div class="example-gloss">{0}</div>'.format(examples[1])
    native = '<div class="example-native">{0}</div>'.format(examples[2])
    html = '<div class="example">' + target + gloss + native + '</div>'
    return RawBlock('html', html)


def create_rule(rule_list):
    raw = shrink_list(rule_list)[3:].split(':')
    rule_name = '<div class="rule-name">{0}</div>'.format(raw[0])
    rule_definition = '<div class="rule-definition">{0}</div>'.format(raw[1].strip())
    html = '<div class="rule">' + rule_name + rule_definition + '</div>'

    return RawBlock('html', html)


def filter(key, value, format, meta):
    if key == 'OrderedList':
        if value[0][1]['t'] == 'Example':
            return create_example(value[1][0][0]['c'])
    elif key == 'Para':
        if value[0]['t'] == 'Str':
            if value[0]['c'][0:3] == '(*)':
                return create_rule(value)

    #return RawBlock('html', str(key) + ' ' + str(value))

if __name__ == "__main__":
    toJSONFilter(filter)
