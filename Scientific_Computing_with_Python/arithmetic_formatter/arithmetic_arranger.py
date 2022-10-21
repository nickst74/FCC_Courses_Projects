def arithmetic_arranger(problems, compute = False):
  # check number of problems
  if len(problems) > 5:
    return "Error: Too many problems."

  l1 = l2 = l3 = l4 = ""
  for prob in problems:
    [x, op, y] = prob.split()
    # check operator
    if op != '+' and op != '-':
      return "Error: Operator must be '+' or '-'."
    # check operands
    if not x.isdigit() or not y.isdigit():
      return "Error: Numbers must only contain digits."
    # get max length for later
    length = max(len(x), len(y))
    if length > 4:
      return "Error: Numbers cannot be more than four digits."
    # line 1
    l1 += " " * (2 + length - len(x)) + x
    # line 2
    l2 += op + " " * (1 + length - len(y)) + y
    # line 3
    l3 += "-" * (2 + length)
    # line 4
    result = str(int(x) + int(y) if op == '+' else int(x) - int(y))
    l4 += " " * (2 + length - len(result)) + result
    
    # also check if needed to add whitespaces
    if prob is not problems[-1]:
      l1 += " " * 4
      l2 += " " * 4
      l3 += " " * 4
      l4 += " " * 4
    
  return l1 + "\n" + l2 + "\n" + l3 + ("\n" + l4 if compute else "")
