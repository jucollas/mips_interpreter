from mips import MIPS, REGISTER
from .utils import is_hex, is_dec, is_bin
import re


class SyntaxChecker:
  def __init__(self) -> None:
    _index_text : int = -1
    _index_data : int = -1
    _index_end : int = -1
    _tags = dict()

  def remove_comments(self, code: str)-> list[str]:
    code_split = code.split('\n')
    ans = list()
    for line in code_split:
      i = 0
      while(i < len(line) and line[i] != '#'): 
        i += 1
      ans.append(line[:i])
    return ans
  
  def parsing(self, code_list : list[str]) -> list[list[str]]:
    ans = list()
    for line in code_list:
      aux = re.split(r'[ ,()]+', line.strip().lower())
      if not aux[-1] and len(aux) > 1:
        aux.pop()
      ans.append(aux)
    return ans
  
  def extract_labels_struct(self, code_matrix):
    n = len(code_matrix)
    i = 0
    self._index_text = self._index_data = self._index_end = -1
    while i < n:
      if self._index_text == -1:
        if code_matrix[i][0] == '.text':
          self._index_text = i
        elif code_matrix[i] != ['']:
          raise ValueError(f" Error: Line { i + 1 }| Cannot write data or instructions before declaring the '.text' tag")
      
      if self._index_data == -1 and code_matrix[i][0] == '.data':
        self._index_data = i

      if self._index_end == -1:
        if code_matrix[i][0] == '.end':
          self._index_end = i
      elif code_matrix[i] != ['']:
        raise ValueError(f"Error: Line { i + 1 } | Cannot write data or instructions after declaring the '.end' tag")

      i += 1

    if self._index_text == -1:
      raise ValueError("Error: The '.text' tag does not exist")
    elif self._index_data == -1:
      raise ValueError("Error: The '.data' tag does not exist")
    elif self._index_end == -1:
      raise ValueError("Error: The '.end' tag does not exist")
    
  def extract_tags(self, code):
    PC = 0
    tags = dict()
    i = self._index_text + 1
    while i <  self._index_end:
      if len(code[i][0]) and code[i][0][-1] == ':':
        if len(code[i]) > 1:
          raise ValueError(f"Error : line {i + 1} '{' '.join(code[i])}' | Asigancion desconocida despues de declarar una etiqueta.")
        tags[code[i][0][:-1]] = PC
      else:
        PC += 1
      i += 1
    return tags
  
  def check_text(self, text):
    i = 0
    ans = []
    while i < len(text):
      line = text[i]
      if line != [''] and line[0][-1] != ':':
        self.check_instruction(line)
        ans.append(line)
      i += 1
    return ans
  
  def check_parameters(self, expected : str, given : str):
    if expected in {'rd', 'rt', 'rs'}:
      if not given in REGISTER:
        raise ValueError(f"Error : '{ given }' | Register does not exist")
    elif expected in {'offset', 'immediate'}:
      if not (is_dec(given) or is_hex(given) or is_bin(given) or given in self._tags):
        raise ValueError(f"Error '{ given }': unrecognized parameter")

  def check_instruction(self, instruction):
    name = instruction[0]
    if name in MIPS:
      parameters = MIPS[name]["parameters"]
      if len(parameters) != len(instruction) - 1:
        raise ValueError(f"Error : '{' '.join(instruction)}' | Number of parameters not compatible with the declared instruction")
      i = 1
      for p in parameters:
        self.check_parameters(p, instruction[i])
        i += 1
    else:
      raise ValueError(f"Error : '{name}' unrecognized instruction.")
    
  def check_data(self, data: str):
    i = 0
    ans = []
    while i < len(data):
      d = data[i]
      if len(d) > 1:
        raise ValueError(f"Error: {' '.join(d)} | Only one piece of data is allowed per line")
      if d != [''] and d[0][-1] != ':':
        if not (is_bin(d[0]) or is_dec(d[0]) or is_hex(d[0])):
          raise ValueError(f"Error: '{d[0]}' | Data type not accepted")
        ans.append(d[0])
      i += 1
    return ans

  def run(self, code : str) -> list:
    code_list = self.remove_comments(code)
    code_matrix = self.parsing(code_list)
    self.extract_labels_struct(code_matrix)
    self._tags = self.extract_tags(code_matrix)

    text_ = code_matrix[self._index_text + 1: self._index_data] 
    data_ = code_matrix[self._index_data + 1: self._index_end]

    text_ = self.check_text(text_)
    data_ = self.check_data(data_)

    return self._tags, text_, data_

