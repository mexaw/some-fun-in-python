''''
and if not return assert del finally import or try break
elif for in pass while
class else from is print yield
countine exept

'''
import time
import os 
print("------------------------------------")
print("- (2)and(3)if+not(4)assert-")
print("- (5)elif(6)for+in(7)pass(8)while   -")
print("-(6)class(7)else(8)countine(9)execpt-")
print("- Coder By MeXaW aL3TuBe           -")
print("-                                  -")
print("-                                  -")
print("-                                  -")
print("-                                  -")
print("------------------------------------")

x = True

while x:

    s = int(input(" Hello freind choose a Number plz "))

    if s==2:# شرط الاول بدايه سكربت طباعه عدد الاكبر !
        print(" you choose and !")
        f = print("  راح اقارن بين اعداد و اطبع الاكبر برنامج بسيط :)بس حدد الارقام ! يتكون من ٣ ارقام !  ")
        n1 = input(" : ")
        n2 = input(" : ")
        n3 = input(" : ")
        if n1 > n2 and n1 > n3:
            print("the number is : {} ".format(n1))
        elif n2> n1 and n2>n3: # ال ايلف تاتي بعد الاف : )
            print("the number is : {} ".format(n2))
        else: # تفيد الايلس انها  م يحتاج اي شرط فقط لو م تححق الاثنان طباعه !! + تقدر تحط شرط ايضا لاكن نكتفي ب ذا
            print("the number is : {} ".format(n3))

    elif s==3:
        print(" you choose if+not")
        print("راح اسالك سؤال ولازم تكتب hatim")
        q = str(input("who is king ? LOL : "))
        if not q=='hatim':
            print(' wrong man')
        elif q=='hatim':
            print("correct")
        else:
            print("ركز ")
    elif s==4:
        print(" assert #  تفيد ل تصحيح من صحه الخطا واذ خطا بيطبع له السببب")
        n00 = input(" حط رقم :")
        n11 = input(" حط رقم :")
        print(" بيقارن الحين  اذا صح بيطبع اذا خطا بيقولك")
    elif n00<n11:
        print(n11)

        assert n00>n11,"wrong Man !"

    elif s==5:
        print(" # if  الاساس و elif  يتكون اكثر من شرط م عندك مشكله  else م يحتاج شرط اذا م نجحو الاثنين الشرطين يطبع عطول او اي شي ")
    elif s==6:
        class s:
            print(' صنع اوبكجت او كان يسوي عمل محدد ')
            print('will take a time ')


            os.system('rebot')
    elif s==7:
        print(" م يحتاج شرح يخوك هعهع")
    elif s==8:
        print(" write  number 1 ")
        w2 = int(input(" : "))
        if w2 == 1:
            print("Can't stop ",w2+1)
        else:
            continue
    elif s==9:
        print(" i will open file اذا مو موجود بيطبع خطا ")
        try:
            filename= str(input(" write file name :  "))

            g = open(filename,"r").read().splitlines()
            for line in g:
                print(" Hello i'm hacker lol !")
                print(line)

        except FileExistsError:
            print(" Not exists")
    else:
        print("wrong namer")

print(" Done thank you To my Freind Dr.Glay ")



