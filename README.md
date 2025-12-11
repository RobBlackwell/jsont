# jsont

`jsont` is a simple JSONL templating system based on Python f-strings.

![Alpha](https://img.shields.io/badge/status-alpha-red)

## Introduction

JSONL is a useful data storage format with good support in most
programming languages, including Python. JSONL is both human readable
and machine readable. The `jq` tool is particularly useful for
visualisation and data extraction.

For example, you might have a list of colours as a
`colours.jsonl` file:

``` jsonl
{"name": "Red", "hex": "#FF0000"}
{"name": "Orange", "hex": "#FFA500"}
{"name": "Yellow", "hex": "#FFFF00"}
{"name": "Green", "hex": "#00FF00"}
{"name": "Blue", "hex": "#0000FF"}
{"name": "Violet", "hex": "#8F00FF"}
```

You might want to view the file in the terminal with

``` bash
jq . colours.jsonl
```

or just get a list of the hex fields:

``` bash
jq -r .hex colours.jsonl
```

Suppose we want to turn this `colours.jsonl` into an HTML list of
colours We can transform the data using `jsont` by defining a template
(let's call it `template1.jsont`) like this:

``` text
<p style="color:{line['hex']};">{line['name']}</p>
```

We can then say

``` bash
./jsont.py template1.jsont colours.jsonl > colours.html
```

and we end up with `questions.jsonl` file like this:

``` html
<p style="color:#FF0000;">Red</p>
<p style="color:#FFA500;">Orange</p>
<p style="color:#FFFF00;">Yellow</p>
<p style="color:#00FF00;">Green</p>
<p style="color:#0000FF;">Blue</p>
<p style="color:#8F00FF;">Violet</p>
```

So how did this work? `jsont` went through every line in
`colours.jsonl` and applied the template `template1.jsont`. Any text
not in an f-string was copied across.  Any f-string expression was
expanded.

Note that the output can be any line-oriented, textual format, for
example [CSV](examples/csv/), or [another JSONL](examples/questions/).

This might all look a bit baroque to start with, but trust me, if you
are a Python programmer who is familiar with f-strings, you'll soon
get the hang of it and find it surprisingly powerful. `jsont.py` is
just one file with about 50 lines of code, so it's easy to understand
and extend if necessary.

`jsont` is useful for creating HTTP JSON request payloads for HTTP web
APIs. We use it for LLM experiments, e.g. with OpenAI, Google Gemini
and OpenRouter. We use `jsont` in conjunction with
[golem](https://github.com/RobBlackwell/golem) and
[talos](https://github.com/RobBlackwell/talos).


## Notes

If you need to include `{` or `}` in your verbatim text then you will
need to escape them as `{{` and `}}` respectively, otherwise they will
be interpreted as an f-string. This is commonly required in JSON
output, see [questions](examples/questions/) as an example.

If your template is long, it can be useful to split it over multiple
lines. However you may not want the line breaks in your resulting
output, and so you can run `./jsont.py --remove-line-endings`.

Sometime you need to add end of line markers within a string - you can
do that with `\\n`.
