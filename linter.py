from SublimeLinter.lint import Linter  # or NodeLinter, PythonLinter, ComposerLinter, RubyLinter
from SublimeLinter.lint import STREAM_STDERR

class glslc(Linter):
    cmd = ('glslc', '-c', '${file_on_disk}')
    regex = r':(?P<line>\d+):\s((?P<warning>warning)|(?P<error>error)):\s\'(?P<near>.*)\'\s:\s+(?P<message>.+)'
    multiline = True
    defaults = {
        'selector': 'source.glsl'
    }
    tempfile_suffix = '-'
    error_stream = STREAM_STDERR
