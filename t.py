print """<html><body><style>
.label {
  font-size: 80%;
}
"""

template = """
.classname {
  background-color: colorname;
  color: colorname;
}
"""

def print_css(classname, colorname):
    print (
        template
        .replace('classname', classname)
        .replace('colorname', colorname))

print_css('bg', '#fc9')
print_css('cS', 'silver')
print_css('cG', 'goldenrod')
colors = "black brown red orange yellow green blue purple grey white".split()

for index, color in enumerate(colors):
    print_css('c%d' % index, color)

print """</style>"""

R = """<p>
<span class='bg'>.
<span class='c%s'>.</span>
<span class='c%s'>.</span>
<span class='c%s'>.</span>
<span class='c%s'>.</span>
.</span><span class='label'>%s %s&#x2126;</span></p>"""

def foo(s, r):
    print R % (s[0], s[1], s[2], s[3], s, r)

foo('100G', '10')
foo('101G', '100')
foo('151G', '150')
foo('221G', '220')
foo('471G', '470')
foo('102G', '1.0K')
foo('222G', '2.2K')
foo('752G', '7.5K')

foo('103G', '10K')
foo('104G', '100K')
foo('105G', '1M')
foo('106G', '10M')
