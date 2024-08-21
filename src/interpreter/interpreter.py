from .converter import Converter

class Interpreter:
  def __init__(self, input_file, output_file, output_format):
    self.input_file = input_file
    self.output_file = output_file
    self.output_format = output_format

  def run(self):
    with open(self.input_file, 'r') as file:
      mips_code = file.read()
      
    format_code = Converter(self.output_format).run(mips_code)

    with open(self.output_file, 'w') as file:
      file.write(format_code)
