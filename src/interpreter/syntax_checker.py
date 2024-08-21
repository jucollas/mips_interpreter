
class SyntaxChecker:
  def __init__(self) -> None:
    pass

  def run(self, code : str) -> list:
    code_split = code.split('\n')
    ans = []
    for line in code_split:
      ans.append(list(map(lambda x: x.lower(), line.split())))
    print(ans)
