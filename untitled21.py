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
        print("1.View list books")
        print("2. Add books")
        print("3. Modify books")
        print("4. Delete books")
        print("5. Search books")
        s2=int(input())
        if s==1:
            books.sort()
            print (books)
        if s2 == 1:
            view_add= open('library.txt','r')
            my_view= view_add.read()
            print(my_view)
            view_add.close()
        if s2== 2:
            view_add= open('library.txt','a')
            m= input()
            view_add.write(m)
            books.append(m)
            view_add.close()
        if s2== 3:
            view_add= open('library.txt','r')
            lines = view_add.readlines()
            view_add.close()
            print("Enter the book you want to modify")
            modify= input()
            view_add= open('library.txt','w')
            for line in lines:
                if line!= modify:
                    view_add.write(line)
                else:
                    print("enter your modiffication in the book")
                    modification= input()
                    view_add.write(modification)
            view_add.close()  
        if s2== 4:
            import os
            view_add= open('library.txt','r')
            lines = view_add.readlines()
            view_add.close()
            print("enter the book to be deleted")
            book= input()
            os.remove('library.txt')
            view_add= open('library.txt','w')
            for line in lines:
                if line!= book :
                    view_add.write(line)
            view_add.close()
        if s2== 5:
            view_add= open('library.txt','r')
            lines = view_add.readlines()
            view_add.close()
            print("Enter the book you want to search")
            book = input()
            view_add= open('library.txt','r')
            for line in lines:
                if line== book:
                    print("Your requested book:")
                    print(book)
            view_add.close()
    if s==3:
        print("1.View list books")
        print("2. Add books")
        print("3. Modify books")
        print("4. Delete books")
        print("5. Search books")
        s3= int(input())
        if s3== 1:
            view_add= open('library1.txt','r')
            my_view= view_add.read()
            print(my_view)
            view_add.close()
        if s3== 2:
            view_add= open('library1.txt','a')
            m= input()
            view_add.write(m)
            books.append(m)
            view_add.close()
       
        if s3== 3:
            view_add= open('library1.txt','r')
            lines = view_add.readlines()
            view_add.close()
            print("Enter the book you want to modify")
            modify= input()
            view_add= open('library1.txt','w')
            for line in lines:
                if line!= modify:
                    view_add.write(line)
                else:
                    print("enter your modification in the book")
                    modification= input()
                    view_add.write(modification)
            view_add.close()
        if s3== 4:
            import os
            view_add= open('library1.txt','r')
            lines = view_add.readlines()
            view_add.close()
            print("enter the book to be deleted")
            book= input()
            os.remove('library1.txt')
            view_add= open('library1.txt','w')
            for line in lines:
                if line!= book :
                    view_add.write(line)
            view_add.close()
        if s3== 5:
            view_add= open('library1.txt','r')
            lines = view_add.readlines()
            view_add.close()
            print("Enter the book you want to search")
            book = input()
            view_add= open('library1.txt','r')
            for line in lines:
                if line== book:
                    print("Your requested book:")
                    print(book)
            view_add.close()
    if s== 4:
        print("1.View list books")
        print("2. Add books")
        print("3. Modify books")
        print("4. Delete books")
        print("5. Search books")
        s4= int(input())
        if s4== 1:
            view_add= open('library2.txt','r')
            my_view= view_add.read()
            print(my_view)
            view_add.close()
        if s4== 2:
            view_add= open('library2.txt','a')
            m= input()
            view_add.write(m)
            books.append(m)
            view_add.close()
        if s4== 3:
            view_add= open('library2.txt','r')
            lines = view_add.readlines()
            view_add.close()
            print("Enter the book you want to modify")
            modify= input()
            view_add= open('library2.txt','w')
            for line in lines:
                if line!= modify:
                    view_add.write(line)
                else:
                    print("enter your modification in the book")
                    modification= input()
                    view_add.write(modification)
            view_add.close()
        if s4== 4:
            import os
            view_add= open('library2.txt','r')
            lines = view_add.readlines()
            view_add.close()
            print("enter the book to be deleted")
            book= input()
            os.remove('library2.txt')
            view_add= open('library2.txt','w')
            for line in lines:
                if line!= book :
                    view_add.write(line)
            view_add.close()
        if s4== 5:
            view_add= open('library2.txt','r')
            lines = view_add.readlines()
            view_add.close()
            print("Enter the book you want to search")
            book = input()
            view_add= open('library2.txt','r')
            for line in lines:
                if line== book:
                    print("Your requested book:")
                    print(book)
            view_add.close()
    if s==5:
        print("1.View list books")
        print("2. Add books")
        print("3. Modify books")
        print("4. Delete books")
        print("5. Search books")
        s5= int(input())
        if s5== 1:
            view_add= open('library3.txt','r')
            my_view= view_add.read()
            print(my_view)
            view_add.close()
        if s5== 2:
            view_add= open('library3.txt','a')
            m= input()
            view_add.write(m)
            books.append(m)
            view_add.close()
       
        if s5== 3:
            view_add= open('library3.txt','r')
            lines = view_add.readlines()
            view_add.close()
            print("Enter the book you want to modify")
            modify= input()
            view_add= open('library3.txt','w')
            for line in lines:
                if line!= modify:
                    view_add.write(line)
                else:
                    print("enter your modification in the book")
                    modification= input()
                    view_add.write(modification)
            view_add.close()
        if s5== 4:
            import os
            view_add= open('library3.txt','r')
            lines = view_add.readlines()
            view_add.close()
            print("enter the book to be deleted")
            book= input()
            os.remove('library3.txt')
            view_add= open('library3.txt','w')
            for line in lines:
                if line!= book :
                    view_add.write(line)
            view_add.close()
        if s5== 5:
            view_add= open('library3.txt','r')
            lines = view_add.readlines()
            view_add.close()
            print("Enter the book you want to search")
            book = input()
            view_add= open('library3.txt','r')
            for line in lines:
                if line== book:
                    print("Your requested book:")
                    print(book)
            view_add.close()
#college students details!!
elif r== 2:
    print("Choose the year of students:")
    print("1. First year")
    print("2. Second year")
    print("3. Third year")
    print("4. Fourth year")
    year= int(input())
    if year==1:
        print("Choose your requirment:")
        print("1. Student Details")
        print("2. List of students in first year")
        print("3. Any pending issues")
        choice= int(input())
        if choice==2:
            file= open('First_year.txt','r')
            my_str= file.read()
            print(my_str)
            file.close()
        if choice==1:
            file= open('First_year.txt','r')
            lines= file.readline()
            file.close()
            print("Enter the name of the student")
            name= str(input())
            file= open('First_year.txt', 'r')
            for line in lines:
                if line== name:
                    print("Your requested book:")
                    print(book)
            file.close()
        if choice==3:
            file= open('1styr_issue.txt.','r')
            my_str= file.read()
            print(my_str)
            file.close()
    if year==2:
        print("Choose your requirment:")
        print("1. Student Details")
        print("2. List of students in second year")
        print("3. Any pending issues")
        choice= int(input())
        if choice==2:
            file= open('second_year.txt','r')
            my_str= file.read()
            print(my_str)
            file.close()
        if choice==1:
            file= open('second_year.txt','r')
            lines= file.readline()
            file.close()
            print("Enter the name of the student")
            name= str(input())
            file= open('second_year.txt', 'r')
            for line in lines:
                if line== name:
                    print("Your requested book:")
                    print(line)
            file.close()
        if choice==3:
            file= open('2ndyr_issue.txt','r')
            my_str= file.read()
            print(my_str)
            file.close()
    if year==3:
        print("Choose your requirment:")
        print("1. Student Details")
        print("2. List of students in third year")
        print("3. Any pending issues")
        choice= int(input())
        if choice==2:
            file= open('third_year.txt','r')
            my_str= file.read()
            print(my_str)
            file.close()
        if choice==1:
            file= open('third_year.txt','r')
            lines= file.readline()
            file.close()
            print("Enter the name of the student")
            name= str(input())
            file= open('third_year.txt', 'r')
            for line in lines:
                if line== name:
                    print("Your requested book:")
                    print(line)
            file.close()
        if choice==3:
            file= open('3rdyr_issue.txt','r')
            my_str= file.read()
            print(my_str)
            file.close()
    if year==4:
        print("Choose your requirment:")
        print("1. Student Details")
        print("2. List of students in fourth year")
        print("3. Any pending issues")
        choice= int(input())
        if choice==2:
            file= open('Fourth_year.txt','r')
            my_str= file.read()
            print(my_str)
            file.close()
        if choice==1:
            file= open('Fourth_year.txt','r')
            lines= file.readline()
            file.close()
            print("Enter the name of the student")
            name= str(input())
            file= open('fourth_year.txt', 'r')
            for line in lines:
                if line== name:
                    print("Your requested book:")
                    print(line)
            file.close()
        if choice==3:
            file= open('4thyr_issue.txt','r')
            my_str= file.read()
            print(my_str)
            file.close()
#Notes
elif r==3:
    print("Choose year of notes:")
    print("1. First year")
    print("2. Second year")
    print("3. third year")
    print("4. Fourth year")
    note= int(input())
    if note ==1:
        file= open('note1.txt','r')
        st=file.read()
        print(st)
        file.close()
    if note ==2:
        file = open('note2.txt','r')
        st=file.read()
        print(st)
        file.close()
    if note ==3:
        file = open('note3.txt','r')
        st= file.read()
        print(st)
        file.close()
    if note ==4:
        file = open('note4.txt','r')
        st = file.read()
        print(st)
        file.close()
else:
    print("Invalid option!!")
    
            
        
        