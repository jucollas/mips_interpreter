from .syntax_checker import SyntaxChecker
from .instruction_translator import InstructionTranslator
from .format_converter import FormatConverter

class Converter:
  def __init__(self, output_format : str):
    self.checker = SyntaxChecker()
    self.translator = InstructionTranslator()
    self.formater = FormatConverter(output_format)

  def run(self, mips_code) -> str:
    tags, code, data = self.checker.run(mips_code)
    program =  self.translator.run(tags, code, data)
    program_format = self.formater.run(program)

    return program_format