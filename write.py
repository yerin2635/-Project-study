from jieba_text import jieba_pseg_cut
from read import read_inputtxt
from prolog_input import prolog_input_rule

prolog = prolog_input_rule()
test = read_inputtxt()
words = jieba_pseg_cut(test)


def lobel_print():
    store = dict()
    Name = "Name"  # 姓名
    Position = "Position"  # 位置
    Address = "Address"  # 地址
    Address1 = "Address1"  # 地址1
    Address2 = "Address2"  # 地址2
    Salary = "Salary"  # 薪水
    reSalary = "reSalary"  # 來記錄比較的薪水
    Exp = "Exp"  # 需要經驗
    Edu = "Edu"  # 教育程度
    why = "why"  # 問題
    wa = "wa"  # 地理問題
    wt = "wt"  # 時間問題
    wq = "wq"  # 比較問題的問題
    orr = "Or"  # 或
    perhaps = "perhaps"  # 某範圍問題的問題
    rT = "待遇面議"
    profession = "profession"  # 職業
    business = "business"  # 業務
    f2 = open('result.txt', 'w')
    for w, f in words:
        store[f] = w
        if f == "or":  # 問題中如果有or(或) 就先對自字詞打上標籤 然後進prolog判斷以後印出
            for n in store.keys():
                if n == "name":
                    Name = store.get(n)
                elif n == "position":
                    Position = store.get(n)
                elif n == "address":
                    Address = store.get(n)
                elif n == "address1":
                    Address = store.get(n)
                elif n == "address2":
                    Address = store.get(n)
                elif n == "m":
                    reSalary = store.get(n)
                elif n == "exp":
                    Exp = store.get(n)
                elif n == "edu":
                    Edu = store.get(n)
                elif n == "why":
                    why = store.get(n)
                elif n == "wa":
                    wa = store.get(n)
                elif n == "wt":
                    wt = store.get(n)
                elif n == "wq":
                    wq = store.get(n)
                elif n == "perhaps":
                    perhaps = store.get(n)
                elif n == "profession":
                    profession = store.get(n)
                elif n == "business":
                    business = store.get(n)
            # 規則
            if why != "why" and Address != "Address" and Address1 != "Address1":
                for soln in prolog.query(
                        "公司(" + Name + "," + Position + "," + Address + "," + Address1 + "," + Address2 + "," + Salary + "," + Exp + "," + Edu + ")"):
                    f2.write(
                        soln[Name] + soln[Position] + Address + Address1 + soln[Address2] + str(soln[Salary]) + str(
                            soln[Exp]) +
                        soln[Edu] + "\n")
                # 規則 地區加上錢
            elif why != "why" and Address != "Address" and wq != "wq" and reSalary != "reSalary":
                for soln in prolog.query(
                        "公司(" + Name + "," + Position + "," + Address + "," + Address1 + "," + Address2 + "," + Salary + "," + Exp + "," + Edu + ")"):
                    if soln[Salary] > reSalary:
                        f2.write(soln[Name] + soln[Position] + Address + soln[Address1] + soln[Address2] + str(
                            soln[Salary]) + str(
                            soln[Exp]) + soln[Edu] + "\n")
            elif profession != "profession" and perhaps != "perhaps":
                for soln in prolog.query(
                        "粗集職業(" + Name + "," + "Position" + "," + Address + "," + Address1 + "," + Address2 + "," + Salary + "," + Exp + "," + Edu + "," + profession + ")"):
                    f2.write(soln[Name] + soln["Position"] + soln[Address] + soln[Address1] + soln[Address2] + str(
                        soln[Salary]) + str(soln[Exp]) + soln[Edu] + "\n")
            elif business != "business" and perhaps != "perhaps":
                for soln in prolog.query(
                        "粗集職業二(" + Name + "," + "Position" + "," + Address + "," + Address1 + "," + Address2 + "," + Salary + "," + Exp + "," + Edu + "," + business + ")"):
                    f2.write(soln[Name] + soln["Position"] + soln[Address] + soln[Address1] + soln[Address2] + str(
                        soln[Salary]) + str(soln[Exp]) + soln[Edu] + "\n")
            elif Address != "Address" and Name != "Name":
                for soln in prolog.query(
                        "公司(" + Name + "," + Position + "," + Address + "," + Address1 + "," + Address2 + "," + Salary + "," + Exp + "," + Edu + ")"):
                    f2.write(
                        Name + soln[Position] + Address + soln[Address1] + soln[Address2] + str(soln[Salary]) + str(
                            soln[Exp]) +
                        soln[Edu] + "\n")
            elif why != "why" and Address != "Address":
                for soln in prolog.query(
                        "公司(" + Name + "," + Position + "," + Address + "," + Address1 + "," + Address2 + "," + Salary + "," + Exp + "," + Edu + ")"):
                    f2.write(soln[Name] + soln[Position] + Address + soln[Address1] + soln[Address2] + str(
                        soln[Salary]) + str(
                        soln[Exp]) + soln[Edu] + "\n")

            elif Name != "Name":
                for soln in prolog.query(
                        "公司(" + Name + "," + Position + "," + Address + "," + Address1 + "," + Address2 + "," + Salary + "," + Exp + "," + Edu + ")"):
                    f2.write(Name + soln[Position] + soln[Address] + soln[Address1] + soln[Address2] + str(
                        soln[Salary]) + str(
                        soln[Exp]) + soln[Edu] + "\n")
            elif Name != "Address":
                for soln in prolog.query(
                        "公司(" + Name + "," + Position + "," + Address + "," + Address1 + "," + Address2 + "," + Salary + "," + Exp + "," + Edu + ")"):
                    f2.write(soln[Name] + soln[Position] + Address + soln[Address1] + soln[Address2] + str(
                        soln[Salary]) + str(
                        soln[Exp]) + soln[Edu] + "\n")
        orr = "Or"

    for n in store.keys():  # 字詞中沒有or(或) 打上標籤給 prolog判斷以後印出
        if n == "name":
            Name = store.get(n)
        elif n == "position":
            Position = store.get(n)
        elif n == "address":
            Address = store.get(n)
        elif n == "address1":
            Address = store.get(n)
        elif n == "address2":
            Address = store.get(n)
        elif n == "m":
            reSalary = store.get(n)
        elif n == "exp":
            Exp = store.get(n)
        elif n == "edu":
            Edu = store.get(n)
        elif n == "why":
            why = store.get(n)
        # print("抓到")
        elif n == "wa":
            wa = store.get(n)
        elif n == "wt":
            wt = store.get(n)
        elif n == "wq":
            wq = store.get(n)
        elif n == "perhaps":
            perhaps = store.get(n)
        elif n == "profession":
            profession = store.get(n)
        elif n == "business":
            business = store.get(n)

    # 規則
    if why != "why" and Address != "Address" and Address1 != "Address1":
        for soln in prolog.query(
                "公司(" + Name + "," + Position + "," + Address + "," + Address1 + "," + Address2 + "," + Salary + "," + Exp + "," + Edu + ")"):
            f2.write(
                soln[Name] + soln[Position] + Address + Address1 + soln[Address2] + str(soln[Salary]) + str(soln[Exp]) +
                soln[Edu] + "\n")
    # 規則 地區加上錢
    elif why != "why" and Address != "Address" and wq != "wq" and reSalary != "reSalary":
        for soln in prolog.query(
                "公司價格(" + Name + "," + Position + "," + Address + "," + Address1 + "," + Address2 + "," + Salary + "," + Exp + "," + Edu + "," + reSalary + "," + rT + ")"):
            f2.write(soln[Name] + soln[Position] + Address + soln[Address1] + soln[Address2] + str(soln[Salary]) + str(
                soln[Exp]) + soln[Edu] + "\n")
    elif profession != "profession" and perhaps != "perhaps":
        print(profession + perhaps)
        for soln in prolog.query(
                "粗集職業(" + Name + "," + "Position" + "," + Address + "," + Address1 + "," + Address2 + "," + Salary + "," + Exp + "," + Edu + "," + profession + ")"):
            f2.write(soln[Name] + soln["Position"] + soln[Address] + soln[Address1] + soln[Address2] + str(
                soln[Salary]) + str(soln[Exp]) + soln[Edu] + "\n")
    elif business != "business" and perhaps != "perhaps":
        print(profession + perhaps)
        for soln in prolog.query(
                "粗集職業二(" + Name + "," + "Position" + "," + Address + "," + Address1 + "," + Address2 + "," + Salary + "," + Exp + "," + Edu + "," + business + ")"):
            f2.write(soln[Name] + soln["Position"] + soln[Address] + soln[Address1] + soln[Address2] + str(
                soln[Salary]) + str(soln[Exp]) + soln[Edu] + "\n")

    elif Address != "Address" and perhaps != "perhaps":
        for soln in prolog.query(
                "粗集公司(" + Name + "," + Position + "," + "Adress" + "," + Address1 + "," + Address2 + "," + Salary + "," + Exp + "," + Edu + "," + Address + ")"):
            f2.write(soln[Name] + soln[Position] + soln["Adress"] + soln[Address1] + soln[Address2] + str(
                soln[Salary]) + str(soln[Exp]) + soln[Edu] + "\n")
    elif Address != "Address" and Name != "Name":
        for soln in prolog.query(
                "公司(" + Name + "," + Position + "," + Address + "," + Address1 + "," + Address2 + "," + Salary + "," + Exp + "," + Edu + ")"):
            f2.write(
                Name + soln[Position] + Address + soln[Address1] + soln[Address2] + str(soln[Salary]) + str(soln[Exp]) +
                soln[Edu] + "\n")
    elif why != "why" and Address != "Address":
        for soln in prolog.query(
                "公司(" + Name + "," + Position + "," + Address + "," + Address1 + "," + Address2 + "," + Salary + "," + Exp + "," + Edu + ")"):
            f2.write(soln[Name] + soln[Position] + Address + soln[Address1] + soln[Address2] + str(soln[Salary]) + str(
                soln[Exp]) + soln[Edu] + "\n")
    elif reSalary != "reSalary" and wq != "wq":
        for soln in prolog.query(
                "公司價格(" + Name + "," + Position + "," + Address + "," + Address1 + "," + Address2 + "," + Salary + "," + Exp + "," + Edu + "," + reSalary + "," + rT + ")"):
            f2.write(soln[Name] + soln[Position] + Address + soln[Address1] + soln[Address2] + str(soln[Salary]) + str(
                soln[Exp]) + soln[Edu] + "\n")
    elif Name != "Name":
        for soln in prolog.query(
                "公司(" + Name + "," + Position + "," + Address + "," + Address1 + "," + Address2 + "," + Salary + "," + Exp + "," + Edu + ")"):
            f2.write(Name + soln[Position] + soln[Address] + soln[Address1] + soln[Address2] + str(soln[Salary]) + str(
                soln[Exp]) + soln[Edu] + "\n")
    elif Address != "Address":
        for soln in prolog.query(
                "公司(" + Name + "," + Position + "," + Address + "," + Address1 + "," + Address2 + "," + Salary + "," + Exp + "," + Edu + ")"):
            f2.write(soln[Name] + soln[Position] + Address + soln[Address1] + soln[Address2] + str(soln[Salary]) + str(
                soln[Exp]) + soln[Edu] + "\n")

    f2.close()