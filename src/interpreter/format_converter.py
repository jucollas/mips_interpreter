class FormatConverter:
  def __init__(self, format) -> None:
    self.format = format
  
  def run(self, program):
    if self.format == 'hex':
      program =map(lambda x : hex(int(x, 2)), program)
    return '\n'.join(program)