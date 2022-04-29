from read import read_inputtxt
from jieba_text import *
from write import lobel_print

jieba_load()
test = read_inputtxt()
jieba_cut_word(test)
lobel_print()

# 規則一
# for soln in prolog.query("公司地職("+Name+","+Position+","+Address+","+Address1+","+Address2+")"):
#   print (soln[Name]+Position+soln[Address]+soln[Address1]+soln[Address2])
# 規則二
# or soln in prolog.query("公司職學("+Name+","+Position+","+Salary+")"):
#    print(soln[Name] + Position + str(soln[Salary]) )
