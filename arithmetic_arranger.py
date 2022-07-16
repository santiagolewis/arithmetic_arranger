#This function arranges mathematical operations(only addition and subtraction). It's the first python challange on freecodecamp. It takes a list of strings containing the problems and arranges it so each problem is displayed the following way: 
#    32
# - 698
# -----
# You can see the instructions in this link to know exactly what this function does.
#https://www.freecodecamp.org/learn/scientific-computing-with-python/scientific-computing-with-python-projects/arithmetic-formatter

def arithmetic_arranger(problems, args = False):
  #First we check that there is 5 problems at most as the instructions indicates.
  if len(problems) > 5:
      return "Error: Too many problems."
  n1s = []
  n2s = []
  l3 = []
  ans = []
  for problem in problems:
    problem = problem.split()
    #Now we check that no other operators than "+" or "-" are being used on the problems 
    if "*" in problem or "/" in problem:
      return "Error: Operator must be '+' or '-'."
    #Here we verify that there are only digits on the problems and no other caracters.
    try:
      int(problem[0])
      int(problem[2])
            
    except ValueError:
      return "Error: Numbers must only contain digits."
    #In this part as the instructions say, we restrict that the numbers are four digits long at most.
    if len(problem[0]) > 4 or len(problem[2]) > 4:
      return "Error: Numbers cannot be more than four digits."
    #Now we begin to arrange the problems. The first thing to do is define the two numbers and the operator. As we have already split every problem, we just define these elements on variables.
    if "+" in problem or "-" in problem:
      oper = problem[1]
      n1 = problem[0]
      n2 = problem[2]
    #In this part we define the variable answer that only needs to be showed if there is a second argument "True". 
      if "+" in problem:
        answer = int(n1)+int(n2)
      else:
        answer = int(n1)-int(n2)
      #The problems need to be arranged right aligned and it must be one space between the operator and the longest number, so we define a width varible that will help us with this.
      if len(problem[0]) > len(problem[2]):
        width = (len(problem[0]) + 2)
      else:
        width = (len(problem[2]) + 2)
      #In this part we align the first number as we said using an fstring and we append it to the n1s list. 
      line_1 = f"{n1:>{width}}"
      n1s.append(line_1)
      #Now we do the same with the operator(that must be on the left of the second line) and the second number. Notice that we substract one to the width in the align of the second number because of the space that the operator occupies.
      line_2 = f"{oper}{n2:>{width-1}}"
      n2s.append(line_2)
      #The third line is just an "-" multiplied by the width so it shows a row that separates the problem from the answer(if this one needs to be showed).
      line_3 = f"{'-'*width}"
      l3.append(line_3)
      #The fourth line corresponds to the answer so we do the same as before.
      line_4 = f"{answer:>{width}}"
      ans.append(line_4)
  #Here we start constructing the sting that we want. For that we define an "a", "b", "c" and "d" varibles that will join every number from the "n1s", "n2s", "l3" and "ans" lists that we built before(with every element already aligned as it shoud be) on their respective variables.
  a = ""
  for x in n1s:
    a += "".join(x)
    #Notice that we add four spaces to every element so the problems are separated by this as the instructions indicate.
    a += "".join(" "*4)
  #Here i modified "a", "b", "c" and "d" because the last loop was adding four spaces at the end of the line and the pytest module was detecting that as wrong. Althoug visually it is the same.
  a = a[0:-4]
  b = ""
  for y in n2s:
    b += "".join(y)
    b += "".join(" "*4)
  b = b[0:-4]
  c = ""
  for z in l3:
    c += "".join(z)
    c += "".join(" "*4)
  c = c[0:-4]
  d = ""
  for k in ans:
    d += "".join(k)
    d += "".join(" "*4)
  d = d[0:-4]
  #In this final part we see if we have to show the answers just by adding or not the "d" variable to the arranged_problems var if args is True.
  if args:
    arranged_problems = f"{a}\n{b}\n{c}\n{d}"
  else:
    arranged_problems = f"{a}\n{b}\n{c}"

  return arranged_problems
