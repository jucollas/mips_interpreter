MIPS = {
  "add": {
    "format": "R",
    "opcode": "0",
    "funct": "0x20",
    "parameters": ['rd', 'rs', 'rt']
  },
  "addi": {
    "format": "I",
    "opcode": "0x8",
    "parameters": ['rt', 'rs', 'immediate']
  },
  "and": {
    "format": "R",
    "opcode": "0",
    "funct": "0x24",
    "parameters": ['rd', 'rs', 'rt']
  },
  "beq": {
    "format": "I",
    "opcode": "0x4",
    "parameters": ['rs', 'rt', 'offset']
  },
  "bne": {
    "format": "I",
    "opcode": "0x5",
    "parameters": ['rs', 'rt', 'offset']
  },
  "j": {
    "format": "J",
    "opcode": "0x2",
    "parameters": ['address']
  },
  "lw": {
    "format": "I",
    "opcode": "0x23",
    "parameters": ['rt', 'offset', 'rs']
  },
  "nor": {
    "format": "R",
    "opcode": "0",
    "funct": "0x27",
    "parameters": ['rd', 'rs', 'rt']
  },
  "or": {
    "format": "R",
    "opcode": "0",
    "funct": "0x25",
    "parameters": ['rd', 'rs', 'rt']
  },
  "sw": {
    "format": "I",
    "opcode": "0x2b",
    "parameters": ['rt', 'offset', 'rs']
  },
  "sub": {
    "format": "R",
    "opcode": "0",
    "funct": "0x22",
    "parameters": ['rd', 'rs', 'rt']
  }
}
REGISTER = {
    "$0": 0,        # Constant value 0
    "$zero": 0,     # Constant value 0
    "$at": 1,       # Assembler temporary
    "$v0": 2,       # Function result
    "$v1": 3,       # Function result
    "$a0": 4,       # Argument 1
    "$a1": 5,       # Argument 2
    "$a2": 6,       # Argument 3
    "$a3": 7,       # Argument 4
    "$t0": 8,       # Temporary 1
    "$t1": 9,       # Temporary 2
    "$t2": 10,      # Temporary 3
    "$t3": 11,      # Temporary 4
    "$t4": 12,      # Temporary 5
    "$t5": 13,      # Temporary 6
    "$t6": 14,      # Temporary 7
    "$t7": 15,      # Temporary 8
    "$s0": 16,      # Saved temporary 1
    "$s1": 17,      # Saved temporary 2
    "$s2": 18,      # Saved temporary 3
    "$s3": 19,      # Saved temporary 4
    "$s4": 20,      # Saved temporary 5
    "$s5": 21,      # Saved temporary 6
    "$s6": 22,      # Saved temporary 7
    "$s7": 23,      # Saved temporary 8
    "$t8": 24,      # Temporary 9
    "$t9": 25,      # Temporary 10
    "$k0": 26,      # Reserved for OS kernel
    "$k1": 27,      # Reserved for OS kernel
    "$gp": 28,      # Global pointer
    "$sp": 29,      # Stack pointer
    "$fp": 30,      # Frame pointer
    "$s8": 30,      # Saved temporary 9 (alternate name for $fp)
    "$ra": 31       # Return address
}
