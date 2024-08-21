from .syntax_checker import SyntaxChecker
from .instruction_translator import InstructionTranslator
from .format_converter import FormatConverter

class Converter:
  def __init__(self, output_format : str):
    self.checker = SyntaxChecker()
    self.translator = InstructionTranslator()
    self.formater = FormatConverter(output_format)

  def run(self, mips_code) -> str:
    code_matrix = self.checker.run(mips_code)
    return ""
    #code_binary = self.translator.run(code_matrix)
    #code_format = self.formater.run(code_binary)
    #return code_format