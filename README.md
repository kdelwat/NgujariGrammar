# Grammar

The source code for the interactive grammar of the Ngujari constructed language.

The site is built from Markdown files in the `/src/content` folder, using
[pandoc](http://pandoc.org/) and a custom Python filter to convert content to
HTML.

## Markdown Features

The Python filter (`filter.py`) implements new Markdown features specific to
linguistics.

### Examples

Examples, including a gloss and translation, can be created using Pandoc's `(@)`
syntax, in the following form:

```
(@) sentence,
    gloss,
    translation
```

The commas following the sentence and gloss must be included. The following code
shows an actual usage of this feature:

```markdown
(@) wann-uma maaju-maaju-j ka jinn-u-m,
    see.aux-pst kangaroo-pl-nom 2.val.1 eat-an-3rd,
    The kangaroos ate/were eating.
```

Becomes:

```html
<div class="example" id="example-1">
    <span class="example-tag">1</span>
    <div class="example-target">wann-uma maaju-maaju-j ka jinn-u-m</div>
    <div class="example-gloss">see.aux-pst kangaroo-pl-nom 2.val.1 eat-an-3rd</div>
    <div class="example-native">The kangaroos ate/were eating.</div>
</div>
```

Which renders as:

![](http://imgur.com/wis8MUJl.png)

### Rules

Rules defining grammatical constructs can be created using a new syntax.

```
(*)label: rule

```

For example:

```
(*)Noun Phrase: np = [adj(s)-attr] n [rel(s)]
```

Becomes:

```html
<div class="rule">
    <div class="rule-name">Noun Phrase</div>
    <div class="rule-definition">np = [adj(s)-attr] n [rel(s)]</div>
</div>
```

Which renders as:

![](http://imgur.com/cWOvg2Tl.png)

### Definitions

Definitions of non-native words can be made to appear as hovertext, by surrounding them in backticks like ``so``.

Words are defined in the CSV file `lexicon.csv`, in the following format:

```
Conword,Local,Type,Gender,Definitions
bunn,to shine,verb,,"1d – x shines, 2 x shines on LOC"
```

Only the `Conword`, `Local`, and `Definitions` fields are currently used. The Pandoc filter looks up the word (say `garanya`) in the lexicon and produces the following code:

```html
<span class="word">garanya
    <span class="definition">adult<br>
        <span class="full-definition">applies to adults of the speaker's totem
        </span>
    </span>
</span>
```

Which renders when the non-native word is moused-over as the following hovertext:

![](https://i.imgur.com/kv05N6i.png)


