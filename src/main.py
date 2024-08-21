import argparse
from interpreter.interpreter import Interpreter
from editor import Editor

def main():
  parser = argparse.ArgumentParser(description="MIPS to Binary Compiler")
  parser.add_argument('-i', '--input', help="Input MIPS file")
  parser.add_argument('-o', '--output', help="Output file")
  parser.add_argument('-f', '--format', choices=['bin', 'hex'], default='bin', help="Output format")
  parser.add_argument('-e', '--editor', action='store_true', help="Open terminal editor")

  args = parser.parse_args()

  if args.editor:
    editor = Editor()
    editor.run()
  else:
    interpreter = Interpreter(args.input, args.output, args.format)
    interpreter.run()

if __name__ == "__main__":
  main()
