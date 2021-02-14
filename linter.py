from SublimeLinter.lint import Linter  # or NodeLinter, PythonLinter, ComposerLinter, RubyLinter
from SublimeLinter.lint import STREAM_STDERR

class glslc(Linter):
    cmd = ('glslc', '-c', '${file}')
    regex = r':(?P<line>\d+):\s((?P<warning>warning)|(?P<error>error)):\s\'(?P<near>.*)\'\s:\s+(?P<message>.+)'
    multiline = True
    defaults = {
        'selector': 'source.glsl'
    }
    error_stream = STREAM_STDERR
