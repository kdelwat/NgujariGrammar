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