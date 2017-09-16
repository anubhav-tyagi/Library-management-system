import untitled20
#College Library Details!!
print("Choose as requirment:")
print("1. College Library Details")
print("2. College Student Details")
print("3. Notes")
r=int(input())
books=list()
if r== 1:
    print("Choose your requirement:")
    print("1. List of issued and unissued book")
    print("2. Books for first year")
    print("3. Books for second year")
    print("4. Books for third year")
    print("5. Books for fourth year")
    s=int(input())
    if s==1:
        books.sort()
        print(books)
    if s==2:
        untitled20.prnt()
        s2=int(input())
        if s2 == 1:untitled20.view()
        if s2== 2:untitled20.add()
        if s2== 3:untitled20.modify()
        if s2== 4:untitled20.delete()
        if s2== 5:untitled20.search()
    if s==3:
        untitled20.prnt()
        s3= int(input())
        if s3== 1:untitled20.view2()
        if s3== 2:untitled20.add2()
        if s3== 3:untitled20.modify2()
        if s3== 4:untitled20.delete2()
        if s3== 5:untitled20.search2()
    if s== 4:
        untitled20.prnt()
        s4= int(input())
        if s4== 1:untitled20.view3()
        if s4== 2:untitled20.add3()
        if s4== 3:untitled20.modify3()
        if s4== 4:untitled20.delete3()
        if s4== 5:untitled20.search3()
    if s==5:
        untitled20.prnt()
        s5= int(input())
        if s5== 1:untitled20.view4()
        if s5== 2:untitled20.add4()
        if s5== 3:untitled20.modify4()
        if s5== 4:untitled20.delete4()
        if s5== 5:untitled20.search4()
#college students details!!
elif r== 2:
    print("Choose the year of students:")
    print("1. First year")
    print("2. Second year")
    print("3. Third year")
    print("4. Fourth year")
    year= int(input())
    if year==1:
        untitled20.details()
        choice= int(input())
        if choice==1:untitled20.list1()
        if choice==2:untitled20.details1()
        if choice==3:untitled20.issues1()
    if year==2:
        untitled20.details()
        choice= int(input())
        if choice==2:untitled20.list2()
        if choice==1:untitled20.details2()
        if choice==3:untitled20.issues2()
    if year==3:
        untitled20.details()
        choice= int(input())
        if choice==2:untitled20.list3()
        if choice==1:untitled20.details3()
        if choice==3:untitled20.issues3()
    if year==4:
        untitled20.details()
        choice= int(input())
        if choice==2:untitled20.list4()
        if choice==1:untitled20.details4()
        if choice==3:untitled20.issues4()
#Notes
elif r==3:
    print("Choose year of notes:")
    print("1. First year")
    print("2. Second year")
    print("3. third year")
    print("4. Fourth year")
    note= int(input())
    if note ==1:untitles20.notes1
    if note ==2:untitles20.notes2()
    if note ==3:untitles20.notes3
    if note ==4:untitles20.notes4()
else:
    print("Invalid option!!")
    
            
        
        