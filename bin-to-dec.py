
def bin_to_dec():
    while True:
      try:
          num_binary = input(
              """Must You\'r Input Like This  \'111.01\' - \'10.11\' - \'101\' - \'0.001\' \nInput You\'r Binary Number :""").strip()
          a = 0
          b = 2
          global result
          result = 0
          if "." in num_binary:
              part_int = num_binary[:num_binary.index(".")]
              part_int = reversed(part_int)
              for i in list(part_int):
                  i = int(i)
                  if i == 1 or i == 0:
                      if i == 1:

                          power_int = 1 * (2**a)
                          result = result + power_int
                          print(result)
                          print(f"Part The Int => {i} continue")
                          #continue
                          a += 1
                      else:
                          a += 1
                  else:
                      print(f"Part The Int => {i} Wrong")
                      break
              print("#" * 50, "\n", "Part The Float".center(50, "#"),
                    "\n", "#" * 50, sep="")
              part_float = num_binary[(num_binary.index(".")+1):]
              list_part_float = list(part_float)
              for ii in list_part_float:
                  ii = int(ii)
                  if ii == 0 or ii == 1:
                      if ii == 1:
                          fl = ii*(1/b)
                          result = result + fl
                          print(result)
                          print(f"Part The Float => {ii} continue")
                          continue
                          b += b
                          print(f"Part The Float => {ii} continue")
                          continue
                          #a = True
                      else:
                          b += b
                  else:
                      print(f"Part The Float => {ii} Wrong")
                      break
              print("#"*50)
          else:
              part_int = num_binary[:]
              part_int = reversed(part_int)
              for i in list(part_int):
                  i = int(i)
                  if i == 1 or i == 0:
                      if i == 1:
                          power_int = 1 * (2**a)
                          result = result + power_int
                          a += 1
                      else:
                          a += 1
                  else:
                      print(f"Part The Int => {i} Wrong")
                      break
              print("#" * 50, "\n", "  End  ".center(50, "#"),
                    "\n", "#" * 50, sep="")
          break
      except ValueError:
        print("ValueError")
        break
    result = f"   Result Is => {result}   "
    print(result.center(50, '#'))
    print('#' * 50)
bin_to_doc()
