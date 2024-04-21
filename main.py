def cky_parser(input_str, grammar):
  def find_rule(prod, grammar):
      return grammar.get(prod, "0")

  def split_string(start, length, splits_cache):
      if (start, length) in splits_cache:
          return splits_cache[start, length]

      splits = []
      for i in range(1, length):
          first = (start, start + i)
          second = (start + i, start + length)
          splits.append((first, second))

      splits_cache[start, length] = splits
      return splits

  def construct_table(input_str, grammar, splits_cache):
      size = len(input_str) + 1
      table = [["" for _ in range(size)] for _ in range(size)]
      for length in range(1, size):
          remaining = size - length
          for i in range(remaining):
              result = ""
              if length > 1:
                  splits = split_string(i, length, splits_cache)
                  for split in splits:
                      idx1, idx2 = split[0]
                      idx3, idx4 = split[1]
                      prod = table[idx1][idx2] + table[idx3][idx4]
                      result = find_rule(prod, grammar)
                      if result != "0":
                          break
              else:
                  result = find_rule(input_str[i:i+1], grammar)
              table[i][i+length] = result
      return table

  def check_start_symbol(table):
      size = len(table)
      return table[0][size-1] == "S"

  splits_cache = {}
  table = construct_table(input_str, grammar, splits_cache)
  return check_start_symbol(table)


if __name__ == '__main__':
  numgramaticas = int(input())
  output = []
  for _ in range(numgramaticas):
      nonterminals, tests = map(int, input().split())
      grammar = {}
      for _ in range(nonterminals):
          production = input().strip()
          head, *productions = production.split()
          for derived in productions:
              grammar[derived] = head
      for _ in range(tests):
          x = input().strip()
          if cky_parser(x, grammar):
              output.append("yes")
          else:
              output.append("no")
  print("")          
  for out in output:
      print(out)
