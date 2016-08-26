# Grammar

The source code for the interactive grammar of the Ngujari constructed language.

The site is built from Markdown files, using [pandoc](http://pandoc.org/) with a
custom Python filter to convert content to HTML.

Built using the excellent CSS framework [bulma](http://bulma.io/),
[jquery.sidenotes](https://github.com/acdlite/jquery.sidenotes) for responsive
sidenotes, and [list.js](http://www.listjs.com/) for the searchable lexicon.

## Installation

1. Clone or download the repository and open a terminal in the base directory.
2. Install the requirements, ensuring the executables `pandoc` and `python` are in your PATH:

    + [pandoc](http://pandoc.org/)
    + [python](https://www.python.org/)
    + [node](https://nodejs.org/en/)

3. Run `pip install pandocfilters` to install the Python dependency.
4. Run `npm install` to install all Node dependencies.
5. Run `grunt` to build the site for the first time, including CSS and Javascript.
6. Run `grunt run:lexicon` to build the lexicon page.
7. Place [list.js.min](http://www.listjs.com/) and
   [jquery.sidenotes.min.js]((https://github.com/acdlite/jquery.sidenotes) into
   the `build/js` folder (they'll stay there on rebuild).
7. All set!

## Usage

There are three sections to the site: chapters, texts, and the lexicon. Any .md
file in the `src/content` folder will be formatted as a chapter in the grammar.
and any in the `src/texts` folder will be formatted as an example text, with
just a simple `grunt update`.

However, both the chapter and text overview pages (`src/chapters.html` and
`src/texts.html`) must be manually updated to include new items. I'll try to
autogenerate it in the future but for now it isn't too much of a hassle.

Finally, the lexicon page is automatically generated from the CSV file
`src/data/lexicon.csv`.

The entire site is created in the `build` directory, which can then be uploaded
directly to a web directory. Behold the beauty of static generation!

## Markdown Features

The Python filter (`src/scripts/pandoc_filter.py`) implements new Markdown
features specific to linguistics.

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