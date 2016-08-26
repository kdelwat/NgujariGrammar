#!/usr/bin/env python
# coding=utf-8

from __future__ import unicode_literals
import csv

dummy = ['kujari',
         'Southern Cassowary',
         'noun',
         'animate',
         'Southern Cassowary; (fig) a person prone to listlessness',
         'The Southern Cassowary is seen as untamable and always in control. However, it seems to have no definite plans and spends its time wandering aimlessly. This sentiment can be applied to people.']


def tag(str, tag_id, cls=None):
    '''Surrounds str with the opening and closing tag of given class.'''
    if cls is None:
        return '<{0}>{1}</{0}>'.format(tag_id, str)
    else:
        return '<{0} class="{1}">{2}</{0}>'.format(tag_id, cls, str)


def format_definition(definition):
    '''Format a single definition string.'''
    if definition.count('(') == definition.count(')'):
        return definition.replace('(', '<em>(').replace(')', ')</em>') + ' ;'
    else:
        return definition + ' ;'


def definition_list(definition):
    '''Return a string of <li> tags from a definition.'''
    meanings = definition.split(';')
    return ''.join(tag(format_definition(meaning), 'li') for meaning in meanings)


def format_word(word):
    '''Takes a word as a list, and returns its formatted HTML.'''
    heading = tag(word[0], 'h1', 'lexicon-word')

    if word[3] != '':
        pos = tag(word[3] + ' ' + word[2], 'h2', 'part-of-speech')
    else:
        pos = tag(word[2], 'h2', 'part-of-speech')

    definition = tag(definition_list(word[4]), 'ul', 'lexicon-definition')
    cultural = tag(word[5], 'p', 'cultural-note')

    return tag(heading + pos + definition + cultural, 'li')


def main(template, lexicon, output):
    with open(lexicon, 'r') as f:
        data = '\n'.join([format_word(line) for line in csv.reader(f)][1:])

    with open(template, 'r') as f:
        temp = f.read()

    with open(output, 'w') as f:
        f.write(temp.replace('{data}', data))

if __name__ == '__main__':
    print(main('src/templates/lexicon.html', 'src/data/lexicon.csv', 'build/lexicon.html'))
