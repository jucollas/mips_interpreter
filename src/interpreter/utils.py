def is_hex(txt :str) -> bool:
  ans = True
  if len(txt) < 3 or txt[:2] != '0x':
    ans = False
  i = 2
  while i < len(txt) and ans:
    if not( txt[i].isdigit() or ord('a') <= ord(txt[i]) <= ord('f') ):
      ans = False
    i += 1
  return ans

def is_dec(txt :str) -> bool:
  ans = True
  i = 0
  while i < len(txt) and ans:
    if not txt[i].isdigit():
      ans = False
    i += 1
  return ans

def is_bin(txt :str) -> bool:
  ans = True
  if len(txt) < 3 or txt[:2] != '0b':
    ans = False
  i = 2
  while i < len(txt) and ans:
    if not txt[i] in {'1', '0'}:
      ans = False
    i += 1
  return ans

def hex_to_bin(hex_: str, legth: int ):
  aux = bin(int(hex_, 16))[2:]
  ans = ('0' * (legth - len(aux))) + aux
  return ans

def dec_to_bin(dec_: int, legth: int ):
  aux = bin(dec_)[2:]
  ans = ('0' * (legth - len(aux))) + aux
  return ans