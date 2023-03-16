# Functions

In programming, a function is a reusable block of code that executes a certain functionality when it is called. Functions are integral parts of every programming language because they help make your code more modular and reusable.

In Python, you define a function with the `def` keyword, then write the function identifier (name) followed by parentheses and a colon. For example:

```
def hello_world():
    print("Hello World")
```

# Built-in Functions

The Python interpreter has a number of functions and types built into it that are always available. They are listed here in alphabetical order:

<table class="docutils align-default">
<colgroup>
<col style="width: 26%">
<col style="width: 24%">
<col style="width: 24%">
<col style="width: 26%">
</colgroup>
<thead>
<tr class="row-odd"><th class="head" colspan="4"><p>Built-in Functions</p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><div class="line-block">
<div class="line"><strong>A</strong></div>
<div class="line"><a class="reference internal" href="https://docs.python.org/3/library/functions.html#abs" title="abs"><code class="xref py py-func docutils literal notranslate"><span class="pre">abs()</span></code></a></div>
<div class="line"><a class="reference internal" href="https://docs.python.org/3/library/functions.html#aiter" title="aiter"><code class="xref py py-func docutils literal notranslate"><span class="pre">aiter()</span></code></a></div>
<div class="line"><a class="reference internal" href="https://docs.python.org/3/library/functions.html#all" title="all"><code class="xref py py-func docutils literal notranslate"><span class="pre">all()</span></code></a></div>
<div class="line"><a class="reference internal" href="https://docs.python.org/3/library/functions.html#any" title="any"><code class="xref py py-func docutils literal notranslate"><span class="pre">any()</span></code></a></div>
<div class="line"><a class="reference internal" href="https://docs.python.org/3/library/functions.html#anext" title="anext"><code class="xref py py-func docutils literal notranslate"><span class="pre">anext()</span></code></a></div>
<div class="line"><a class="reference internal" href="https://docs.python.org/3/library/functions.html#ascii" title="ascii"><code class="xref py py-func docutils literal notranslate"><span class="pre">ascii()</span></code></a></div>
<div class="line"><br></div>
<div class="line"><strong>B</strong></div>
<div class="line"><a class="reference internal" href="https://docs.python.org/3/library/functions.html#bin" title="bin"><code class="xref py py-func docutils literal notranslate"><span class="pre">bin()</span></code></a></div>
<div class="line"><a class="reference internal" href="https://docs.python.org/3/library/functions.html#bool" title="bool"><code class="xref py py-func docutils literal notranslate"><span class="pre">bool()</span></code></a></div>
<div class="line"><a class="reference internal" href="https://docs.python.org/3/library/functions.html#breakpoint" title="breakpoint"><code class="xref py py-func docutils literal notranslate"><span class="pre">breakpoint()</span></code></a></div>
<div class="line"><a class="reference internal" href="https://docs.python.org/3/library/functions.html#func-bytearray"><code class="docutils literal notranslate"><span class="pre">bytearray()</span></code></a></div>
<div class="line"><a class="reference internal" href="https://docs.python.org/3/library/functions.html#func-bytes"><code class="docutils literal notranslate"><span class="pre">bytes()</span></code></a></div>
<div class="line"><br></div>
<div class="line"><strong>C</strong></div>
<div class="line"><a class="reference internal" href="https://docs.python.org/3/library/functions.html#callable" title="callable"><code class="xref py py-func docutils literal notranslate"><span class="pre">callable()</span></code></a></div>
<div class="line"><a class="reference internal" href="https://docs.python.org/3/library/functions.html#chr" title="chr"><code class="xref py py-func docutils literal notranslate"><span class="pre">chr()</span></code></a></div>
<div class="line"><a class="reference internal" href="https://docs.python.org/3/library/functions.html#classmethod" title="classmethod"><code class="xref py py-func docutils literal notranslate"><span class="pre">classmethod()</span></code></a></div>
<div class="line"><a class="reference internal" href="https://docs.python.org/3/library/functions.html#compile" title="compile"><code class="xref py py-func docutils literal notranslate"><span class="pre">compile()</span></code></a></div>
<div class="line"><a class="reference internal" href="https://docs.python.org/3/library/functions.html#complex" title="complex"><code class="xref py py-func docutils literal notranslate"><span class="pre">complex()</span></code></a></div>
<div class="line"><br></div>
<div class="line"><strong>D</strong></div>
<div class="line"><a class="reference internal" href="https://docs.python.org/3/library/functions.html#delattr" title="delattr"><code class="xref py py-func docutils literal notranslate"><span class="pre">delattr()</span></code></a></div>
<div class="line"><a class="reference internal" href="https://docs.python.org/3/library/functions.html#func-dict"><code class="docutils literal notranslate"><span class="pre">dict()</span></code></a></div>
<div class="line"><a class="reference internal" href="https://docs.python.org/3/library/functions.html#dir" title="dir"><code class="xref py py-func docutils literal notranslate"><span class="pre">dir()</span></code></a></div>
<div class="line"><a class="reference internal" href="https://docs.python.org/3/library/functions.html#divmod" title="divmod"><code class="xref py py-func docutils literal notranslate"><span class="pre">divmod()</span></code></a></div>
<div class="line"><br></div>
</div>
</td>
<td><div class="line-block">
<div class="line"><strong>E</strong></div>
<div class="line"><a class="reference internal" href="https://docs.python.org/3/library/functions.html#enumerate" title="enumerate"><code class="xref py py-func docutils literal notranslate"><span class="pre">enumerate()</span></code></a></div>
<div class="line"><a class="reference internal" href="https://docs.python.org/3/library/functions.html#eval" title="eval"><code class="xref py py-func docutils literal notranslate"><span class="pre">eval()</span></code></a></div>
<div class="line"><a class="reference internal" href="https://docs.python.org/3/library/functions.html#exec" title="exec"><code class="xref py py-func docutils literal notranslate"><span class="pre">exec()</span></code></a></div>
<div class="line"><br></div>
<div class="line"><strong>F</strong></div>
<div class="line"><a class="reference internal" href="https://docs.python.org/3/library/functions.html#filter" title="filter"><code class="xref py py-func docutils literal notranslate"><span class="pre">filter()</span></code></a></div>
<div class="line"><a class="reference internal" href="https://docs.python.org/3/library/functions.html#float" title="float"><code class="xref py py-func docutils literal notranslate"><span class="pre">float()</span></code></a></div>
<div class="line"><a class="reference internal" href="https://docs.python.org/3/library/functions.html#format" title="format"><code class="xref py py-func docutils literal notranslate"><span class="pre">format()</span></code></a></div>
<div class="line"><a class="reference internal" href="https://docs.python.org/3/library/functions.html#func-frozenset"><code class="docutils literal notranslate"><span class="pre">frozenset()</span></code></a></div>
<div class="line"><br></div>
<div class="line"><strong>G</strong></div>
<div class="line"><a class="reference internal" href="https://docs.python.org/3/library/functions.html#getattr" title="getattr"><code class="xref py py-func docutils literal notranslate"><span class="pre">getattr()</span></code></a></div>
<div class="line"><a class="reference internal" href="https://docs.python.org/3/library/functions.html#globals" title="globals"><code class="xref py py-func docutils literal notranslate"><span class="pre">globals()</span></code></a></div>
<div class="line"><br></div>
<div class="line"><strong>H</strong></div>
<div class="line"><a class="reference internal" href="https://docs.python.org/3/library/functions.html#hasattr" title="hasattr"><code class="xref py py-func docutils literal notranslate"><span class="pre">hasattr()</span></code></a></div>
<div class="line"><a class="reference internal" href="https://docs.python.org/3/library/functions.html#hash" title="hash"><code class="xref py py-func docutils literal notranslate"><span class="pre">hash()</span></code></a></div>
<div class="line"><a class="reference internal" href="https://docs.python.org/3/library/functions.html#help" title="help"><code class="xref py py-func docutils literal notranslate"><span class="pre">help()</span></code></a></div>
<div class="line"><a class="reference internal" href="https://docs.python.org/3/library/functions.html#hex" title="hex"><code class="xref py py-func docutils literal notranslate"><span class="pre">hex()</span></code></a></div>
<div class="line"><br></div>
<div class="line"><strong>I</strong></div>
<div class="line"><a class="reference internal" href="https://docs.python.org/3/library/functions.html#id" title="id"><code class="xref py py-func docutils literal notranslate"><span class="pre">id()</span></code></a></div>
<div class="line"><a class="reference internal" href="https://docs.python.org/3/library/functions.html#input" title="input"><code class="xref py py-func docutils literal notranslate"><span class="pre">input()</span></code></a></div>
<div class="line"><a class="reference internal" href="https://docs.python.org/3/library/functions.html#int" title="int"><code class="xref py py-func docutils literal notranslate"><span class="pre">int()</span></code></a></div>
<div class="line"><a class="reference internal" href="https://docs.python.org/3/library/functions.html#isinstance" title="isinstance"><code class="xref py py-func docutils literal notranslate"><span class="pre">isinstance()</span></code></a></div>
<div class="line"><a class="reference internal" href="https://docs.python.org/3/library/functions.html#issubclass" title="issubclass"><code class="xref py py-func docutils literal notranslate"><span class="pre">issubclass()</span></code></a></div>
<div class="line"><a class="reference internal" href="https://docs.python.org/3/library/functions.html#iter" title="iter"><code class="xref py py-func docutils literal notranslate"><span class="pre">iter()</span></code></a></div>
</div>
</td>
<td><div class="line-block">
<div class="line"><strong>L</strong></div>
<div class="line"><a class="reference internal" href="https://docs.python.org/3/library/functions.html#len" title="len"><code class="xref py py-func docutils literal notranslate"><span class="pre">len()</span></code></a></div>
<div class="line"><a class="reference internal" href="https://docs.python.org/3/library/functions.html#func-list"><code class="docutils literal notranslate"><span class="pre">list()</span></code></a></div>
<div class="line"><a class="reference internal" href="https://docs.python.org/3/library/functions.html#locals" title="locals"><code class="xref py py-func docutils literal notranslate"><span class="pre">locals()</span></code></a></div>
<div class="line"><br></div>
<div class="line"><strong>M</strong></div>
<div class="line"><a class="reference internal" href="https://docs.python.org/3/library/functions.html#map" title="map"><code class="xref py py-func docutils literal notranslate"><span class="pre">map()</span></code></a></div>
<div class="line"><a class="reference internal" href="https://docs.python.org/3/library/functions.html#max" title="max"><code class="xref py py-func docutils literal notranslate"><span class="pre">max()</span></code></a></div>
<div class="line"><a class="reference internal" href="https://docs.python.org/3/library/functions.html#func-memoryview"><code class="docutils literal notranslate"><span class="pre">memoryview()</span></code></a></div>
<div class="line"><a class="reference internal" href="https://docs.python.org/3/library/functions.html#min" title="min"><code class="xref py py-func docutils literal notranslate"><span class="pre">min()</span></code></a></div>
<div class="line"><br></div>
<div class="line"><strong>N</strong></div>
<div class="line"><a class="reference internal" href="https://docs.python.org/3/library/functions.html#next" title="next"><code class="xref py py-func docutils literal notranslate"><span class="pre">next()</span></code></a></div>
<div class="line"><br></div>
<div class="line"><strong>O</strong></div>
<div class="line"><a class="reference internal" href="https://docs.python.org/3/library/functions.html#object" title="object"><code class="xref py py-func docutils literal notranslate"><span class="pre">object()</span></code></a></div>
<div class="line"><a class="reference internal" href="https://docs.python.org/3/library/functions.html#oct" title="oct"><code class="xref py py-func docutils literal notranslate"><span class="pre">oct()</span></code></a></div>
<div class="line"><a class="reference internal" href="https://docs.python.org/3/library/functions.html#open" title="open"><code class="xref py py-func docutils literal notranslate"><span class="pre">open()</span></code></a></div>
<div class="line"><a class="reference internal" href="https://docs.python.org/3/library/functions.html#ord" title="ord"><code class="xref py py-func docutils literal notranslate"><span class="pre">ord()</span></code></a></div>
<div class="line"><br></div>
<div class="line"><strong>P</strong></div>
<div class="line"><a class="reference internal" href="https://docs.python.org/3/library/functions.html#pow" title="pow"><code class="xref py py-func docutils literal notranslate"><span class="pre">pow()</span></code></a></div>
<div class="line"><a class="reference internal" href="https://docs.python.org/3/library/functions.html#print" title="print"><code class="xref py py-func docutils literal notranslate"><span class="pre">print()</span></code></a></div>
<div class="line"><a class="reference internal" href="https://docs.python.org/3/library/functions.html#property" title="property"><code class="xref py py-func docutils literal notranslate"><span class="pre">property()</span></code></a></div>
<div class="line"><br></div>
<div class="line"><br></div>
<div class="line"><br></div>
<div class="line"><br></div>
</div>
</td>
<td><div class="line-block">
<div class="line"><strong>R</strong></div>
<div class="line"><a class="reference internal" href="https://docs.python.org/3/library/functions.html#func-range"><code class="docutils literal notranslate"><span class="pre">range()</span></code></a></div>
<div class="line"><a class="reference internal" href="https://docs.python.org/3/library/functions.html#repr" title="repr"><code class="xref py py-func docutils literal notranslate"><span class="pre">repr()</span></code></a></div>
<div class="line"><a class="reference internal" href="https://docs.python.org/3/library/functions.html#reversed" title="reversed"><code class="xref py py-func docutils literal notranslate"><span class="pre">reversed()</span></code></a></div>
<div class="line"><a class="reference internal" href="https://docs.python.org/3/library/functions.html#round" title="round"><code class="xref py py-func docutils literal notranslate"><span class="pre">round()</span></code></a></div>
<div class="line"><br></div>
<div class="line"><strong>S</strong></div>
<div class="line"><a class="reference internal" href="https://docs.python.org/3/library/functions.html#func-set"><code class="docutils literal notranslate"><span class="pre">set()</span></code></a></div>
<div class="line"><a class="reference internal" href="https://docs.python.org/3/library/functions.html#setattr" title="setattr"><code class="xref py py-func docutils literal notranslate"><span class="pre">setattr()</span></code></a></div>
<div class="line"><a class="reference internal" href="https://docs.python.org/3/library/functions.html#slice" title="slice"><code class="xref py py-func docutils literal notranslate"><span class="pre">slice()</span></code></a></div>
<div class="line"><a class="reference internal" href="https://docs.python.org/3/library/functions.html#sorted" title="sorted"><code class="xref py py-func docutils literal notranslate"><span class="pre">sorted()</span></code></a></div>
<div class="line"><a class="reference internal" href="https://docs.python.org/3/library/functions.html#staticmethod" title="staticmethod"><code class="xref py py-func docutils literal notranslate"><span class="pre">staticmethod()</span></code></a></div>
<div class="line"><a class="reference internal" href="https://docs.python.org/3/library/functions.html#func-str"><code class="docutils literal notranslate"><span class="pre">str()</span></code></a></div>
<div class="line"><a class="reference internal" href="https://docs.python.org/3/library/functions.html#sum" title="sum"><code class="xref py py-func docutils literal notranslate"><span class="pre">sum()</span></code></a></div>
<div class="line"><a class="reference internal" href="https://docs.python.org/3/library/functions.html#super" title="super"><code class="xref py py-func docutils literal notranslate"><span class="pre">super()</span></code></a></div>
<div class="line"><br></div>
<div class="line"><strong>T</strong></div>
<div class="line"><a class="reference internal" href="https://docs.python.org/3/library/functions.html#func-tuple"><code class="docutils literal notranslate"><span class="pre">tuple()</span></code></a></div>
<div class="line"><a class="reference internal" href="https://docs.python.org/3/library/functions.html#type" title="type"><code class="xref py py-func docutils literal notranslate"><span class="pre">type()</span></code></a></div>
<div class="line"><br></div>
<div class="line"><strong>V</strong></div>
<div class="line"><a class="reference internal" href="https://docs.python.org/3/library/functions.html#vars" title="vars"><code class="xref py py-func docutils literal notranslate"><span class="pre">vars()</span></code></a></div>
<div class="line"><br></div>
<div class="line"><strong>Z</strong></div>
<div class="line"><a class="reference internal" href="https://docs.python.org/3/library/functions.html#zip" title="zip"><code class="xref py py-func docutils literal notranslate"><span class="pre">zip()</span></code></a></div>
<div class="line"><br></div>
<div class="line"><strong>_</strong></div>
<div class="line"><a class="reference internal" href="https://docs.python.org/3/library/functions.html#import__" title="__import__"><code class="xref py py-func docutils literal notranslate"><span class="pre">__import__()</span></code></a></div>
</div>
</td>
</tr>
</tbody>
</table>

# References and credits

- [freecodecamp](https://www.freecodecamp.org/news/python-functions-define-and-call-a-function/)
- [Python](https://docs.python.org/3/library/functions.html)
