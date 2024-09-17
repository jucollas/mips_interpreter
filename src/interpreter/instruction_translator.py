from mips import MIPS, REGISTER
from .utils import dec_to_bin, hex_to_bin, is_hex, is_bin, is_dec

class InstructionTranslator:
  def __init__(self) -> None:
    pass
  
  def translate_immediate_bin(self, inmediate, tags):
    if inmediate in tags:
      ans = dec_to_bin(tags[inmediate], 32)
    elif is_hex(inmediate):
      ans = dec_to_bin(int(inmediate, 16), 32)
    elif is_dec(inmediate):
      ans = dec_to_bin(int(inmediate), 32)
    elif is_bin(inmediate):
      ans = inmediate
    return ans


  def translate_immediate_hex(self, inmediate, tags):
    if inmediate in tags:
      ans = hex(tags[inmediate])
    elif is_hex(inmediate):
      ans = inmediate
    elif is_dec(inmediate):
      ans = hex(int(inmediate))
    elif is_bin(inmediate):
      ans = hex(int(inmediate, 2))
    return ans

  def translate_line(self, tags: dict[str : int], line : list, PC : int):
    type_inst = MIPS[line[0]]['format']
    opcode = MIPS[line[0]]['opcode']
    bin = list()
    if(type_inst == 'R'):
      rs = REGISTER[line[2]]
      rt = REGISTER[line[3]]
      rd = REGISTER[line[1]]
      funct = MIPS[line[0]]['funct']
      shamt = 0
      bin = [
        hex_to_bin(opcode, 6),  
        dec_to_bin(rs, 5),
        dec_to_bin(rt, 5),
        dec_to_bin(rd, 5),
        dec_to_bin(shamt, 5),
        hex_to_bin(funct, 6)
      ]
    elif(type_inst == 'I'):
      rt = REGISTER[line[1]]
      if line[0] in {'sw', 'lw'}:
        immediate = line[2]
        rs = REGISTER[line[3]]
      else:
        rs = REGISTER[line[2]]
        if line[0] == 'beq':
          immediate = hex(tags[line[3]] - (PC + 1))
          rs, rt = rt, rs
        else:
          immediate = self.translate_immediate_hex(line[3], tags)
          
      bin = [
        hex_to_bin(opcode, 6),
        dec_to_bin(rs, 5),
        dec_to_bin(rt, 5),
        hex_to_bin(immediate, 16)
      ]
    elif(type_inst == 'J'):
      targe = tags[line[1]]
      bin = [
        hex_to_bin(opcode, 6),
        dec_to_bin(targe, 26)
      ]
    return bin

  def code_to_bin(self, tags, code, program):
    PC = 0
    for line in code:
      binary_list = self.translate_line(tags, line, PC)
      binary_str = ''.join(binary_list)
      program.append(binary_str)

  def data_to_bin(self, tags, data, program):
    for d in data:
      program.append(self.translate_immediate_bin(d, tags))

  def run(self, tags, code, data):
    program = []
    self.code_to_bin(tags, code, program)
    self.data_to_bin(tags, data, program)
    return program