#!/usr/bin/env python

from pandocfilters import toJSONFilter, Str, Para, RawBlock, DefinitionList, Header
from itertools import groupby


def markup(value):
    if value['t'] == "Strong":
        s = '\\textbf{'
    elif value['t'] == "Emph":
        s = '\\textit{'
    elif value['t'] == "Code":
        s = '{\small \\textcolor{Gray}{' + value['c'][1] + '}}'
        return s

    for val in value['c']:
        if val['t'] == 'Space':
            s += " "
        else:
            s += val['c']
    s += '}'
    return s.strip()


def math(value):
    for val in value['c']:
        if isinstance(val, dict):
            if val['t'] == "DisplayMath":
                mode = "display"
            else:
                mode = "inline"
    for val in value['c']:
        if not isinstance(val, dict):
            if mode == "inline":
                return "$" + val + "$"
            elif mode == "display":
                return "$$" + val + "$$"


def formattext(value):
    con = ""
    for val in value:
        if val['t'] == 'Space':
            con += " "
        elif val['t'] in ['Strong', 'Emph', 'Code']:
            con += markup(val)
        elif val['t'] == 'Math':
            con += math(val)
        else:
            con += val['c']
    return con.strip()


def marginnote(value):
    opener = value[0]['c']
    if len(opener) > 5:
        shift = opener[4:-1]
    else:
        shift = "0"
    text = formattext(value[1:-1])
    return RawBlock("latex", "\\marginnote[" + shift + "in]{" + text + "}")


def lines(working):
    l = []
    for k, g in groupby(working, lambda x: x == Str('.')):
        if not k:
            l.append(list(g))
    return l


def answer(line):
    if line[0] == "$":
        answer = "$\\therefore " + line[1:]
    else:
        answer = "$\\therefore$ " + line

    return "\\multicolumn{1}{p{7cm}}{\\textcolor{BrickRed}{" + answer + "}}\\\\"

def example(value):
    header = "\\multicolumn{1}{c}{\\textbf{Example " + value[2]['c'] + "}}\\\\"
    question = "\\textit{"
    question += formattext(value[value.index(Str("Q:")) + 1:value.index(Str("A:"))])
    question += "}\\\\"

    working = lines(value[value.index(Str("A:")) + 1:])
    workstring = ""
    for line in working:
        s = formattext(line)
        if s[:2] == "->":
            workstring += answer(s[2:])
        else:
            workstring += s + "\\\\ "

    return RawBlock("latex",
                    "\\begin{center}"
                    + "{\\tabulinesep=1.2mm\\begin{tabu}{p{7cm}}"
                    + header
                    + question
                    + workstring
                    + "\\end{tabu}}\\newline"
                    + "\\end{center}")


def fullwidth(value):
    text = formattext(value[1:-1])
    latex = "\\begin{fullwidth}\\textit{" + text + "}\\end{fullwidth}"
    return RawBlock("latex", latex)


def figure(value, mode, offset):
    link = value[1][0]
    caption = formattext(value[0])

    if mode == "marginfigure":
        if offset == "":
            offset = "0"
        latex = "\\begin{marginfigure}[" + offset + "in]"
    else:
        latex = "\\begin{" + mode + "}"
    latex += "\\centering"
    if mode == "marginfigure":
        latex += "\\includegraphics[width=5cm,height=5cm,keepaspectratio]{" + link + "}"
    else:
        latex += "\\includegraphics[width=10cm, height=10cm,keepaspectratio]{" + link + "}"
    latex += "\\caption{" + caption + "}"
    latex += "\\end{" + mode + "}"

    #return Para([Str("Image with offset of " + str(offset))])
    return RawBlock("latex", latex)


def replace(key, value, format, meta):
    if key == 'Para':
        mode = "debug"
        if mode == "debug":
            value.append(Str(str(value)))
            return Para(value)
        else:
            if value[-1] == Str("[>>>]"):
                return marginnote(value)
            elif value[-1] == Str("[###]"):
                return fullwidth(value)
            elif value[0]['c'][0] == '!' and value[1]['t'] == 'Image':
                offset = value[0]['c'][1:]
                return figure(value[1]['c'], 'marginfigure', offset)
            elif value[0]['t'] == 'Image':
                return figure(value[0]['c'], 'figure', None)
            elif value[0] == Str("Example") and Str("Q:") in value:
                return example(value)
    elif key == "DefinitionList":
        return DefinitionList(value)
        for item in value:
            item[0] = Str("poo")
        return Para([Str(str(value))])


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
    #return RawBlock('html', shrink_list(example_list))

def create_rule(rule_list):
    raw = shrink_list(rule_list)[3:].split(':')
    rule_name = '<div class="rule-name">{0}</div>'.format(raw[0])
    rule_definition = '<div class="rule-definition">{0}</div>'.format(raw[1].strip())
    html = '<div class="rule">' + rule_name + rule_definition + '</div>'

    return RawBlock('html', html)

def test(key, value, format, meta):
    if key == 'OrderedList':
        if value[0][1]['t'] == 'Example':
            return create_example(value[1][0][0]['c'])
    elif key == 'Para':
        if value[0]['t'] == 'Str':
            if value[0]['c'][0:3] == '(*)':
                return create_rule(value)

    #return RawBlock('html', str(key) + ' ' + str(value))

if __name__ == "__main__":
    toJSONFilter(test)
