from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMessageBox, QMainWindow, QWidget, QAction, QPushButton, QComboBox, QLabel, QLineEdit, QVBoxLayout, QTextEdit
from random import randint, random
from PyQt5.QtGui import QIcon
app = QApplication([])
main_window = QMainWindow()
main_window.setWindowIcon(QIcon('./icons/flower_plant.ico'))
main_window.setWindowTitle('Генератор уравнений')
main_window.setGeometry(100, 100, 500, 400)
menu = main_window.menuBar()
eqvals = menu.addMenu('Уравнения')
eqvals.addAction('Линейные уравнения',lambda: lin_win.show())
eqvals.addAction('Квадратные уравнения',lambda: sq_win.show())
eqvals.addAction('Произведение равно нулю',lambda: mul_win.show())
systems = menu.addMenu('Системы уравнений')
systems.addAction('Линейные',lambda: sys_win.show())
systems.addAction('Стандартные графики',lambda: sys1_win.show())
text_box = QTextEdit(main_window)
main_window.setCentralWidget(text_box)
class Line_Window(QWidget):
    def __init__(self):
        super().__init__() 
        self.lin_line = QVBoxLayout()
        self.setWindowTitle('Линейные уравнения')
        self.resize(300,200)
        self.vid_lin = QComboBox()
        self.vid_lin_label = QLabel('Выберите вид линейного уравнения')
        self.lin_line.addWidget(self.vid_lin_label)
        self.lin_line.addWidget(self.vid_lin)
        values=["□x+□=□+□x", "□x+□(x+□)=□x+□", "□(□+□x)-(□+□x)=□", "□(□+□x)+□=□x+□(□x+□)"]
        self.vid_lin.addItems(values)
        self.num_lin_label = QLabel('Необходимое количество вариантов')
        self.lin_line.addWidget(self.num_lin_label)
        self.num_lin = QLineEdit()
        self.lin_line.addWidget(self.num_lin)
        self.lin_button = QPushButton('Составить задания')
        self.lin_line.addWidget(self.lin_button)
        self.setLayout(self.lin_line)
    def click(self):
        try:
            a = self.vid_lin.currentIndex()
            k = int(self.num_lin.text())
            self.hide()
            self.num_lin.clear()
            return a, k
        except:
            q_box = QMessageBox()
            q_box.setText('В поле количества нужно ввести число')
            q_box.setWindowTitle('Предупреждение')
            q_box.setWindowIcon(QIcon('./icons/flower_plant.ico'))
            q_box.exec_()
         
lin_win = Line_Window()
lin_win.setWindowIcon(QIcon('./icons/flower_plant.ico'))
def press_button_lin():
    try:
        a, k = lin_win.click()
        if a == 0:
            text_box.setText(Type0(k))
        elif a == 1:
            text_box.setText(Type1(k))  
        elif a == 2:
            text_box.setText(Type2(k))  
        else:
            text_box.setText(Type3(k)) 
    except:
        pass
lin_win.lin_button.clicked.connect(press_button_lin)

class Squear_Window(QWidget):
    def __init__(self):
        super().__init__() 
        self.sq_line = QVBoxLayout()
        self.setWindowTitle('Квадратные уравнения')
        self.resize(300,250)
        self.vid_sq = QComboBox()
        self.vid_sq_label = QLabel('Выберите вид квадратного уравнения')
        self.sq_line.addWidget(self.vid_sq_label)
        self.sq_line.addWidget(self.vid_sq)
        values=["приведенное уравнение","целые коэффициенты"]
        self.vid_sq.addItems(values)
        self.type_sq = QComboBox()
        self.type_sq_label = QLabel('Выберите количество корней')
        self.sq_line.addWidget(self.type_sq_label)
        self.sq_line.addWidget(self.type_sq)
        values=["нет корней","один корень","два корня"]
        self.type_sq.addItems(values)        
        self.num_sq_label = QLabel('Необходимое количество вариантов')
        self.sq_line.addWidget(self.num_sq_label)
        self.num_sq = QLineEdit()
        self.sq_line.addWidget(self.num_sq)
        self.sq_button = QPushButton('Составить задания')
        self.sq_line.addWidget(self.sq_button)
        self.setLayout(self.sq_line) 
    def click(self):
        try:
            a = self.vid_sq.currentIndex()
            b = self.type_sq.currentIndex()
            k = int(self.num_sq.text())
            self.hide()
            self.num_sq.clear()
            return a, b, k
        except:
            q_box = QMessageBox()
            q_box.setText('В поле количества нужно ввести число')
            q_box.setWindowTitle('Предупреждение')
            q_box.setWindowIcon(QIcon('./icons/flower_plant.ico'))
            q_box.exec_()    
sq_win = Squear_Window()
sq_win.setWindowIcon(QIcon('./icons/flower_plant.ico'))
def press_button_sq():
    try:
        a, b, k = sq_win.click()
        result = kvadratnoe_yravnenie(a,b,k)
        text_box.setText(result) 
    except:
        pass    
sq_win.sq_button.clicked.connect(press_button_sq)

class Multi_Window(QWidget):
    def __init__(self):
        super().__init__() 
        self.lin_line = QVBoxLayout()
        self.setWindowTitle('Произведение равно нулю')
        self.resize(300,200)
        self.vid_lin = QComboBox()
        self.vid_lin_label = QLabel('Выберите общий вид уравнения')
        self.lin_line.addWidget(self.vid_lin_label)
        self.lin_line.addWidget(self.vid_lin)
        values=["(x+□)(x+□)=0","(□x+□)(□+□x)=0","(□x+□)(□+□x)(□x+□)=0","□x(□x+□)(□+□x)=0"]
        self.vid_lin.addItems(values)
        self.num_lin_label = QLabel('Необходимое количество вариантов')
        self.lin_line.addWidget(self.num_lin_label)
        self.num_lin = QLineEdit()
        self.lin_line.addWidget(self.num_lin)
        self.lin_button = QPushButton('Составить задания')
        self.lin_line.addWidget(self.lin_button)
        self.setLayout(self.lin_line)
    def click(self):
        try:
            a = self.vid_lin.currentIndex()
            k = int(self.num_lin.text())
            self.hide()
            self.num_lin.clear()
            return a, k
        except:
            q_box = QMessageBox()
            q_box.setText('В поле количества нужно ввести число')
            q_box.setWindowTitle('Предупреждение')
            q_box.setWindowIcon(QIcon('./icons/flower_plant.ico'))
            q_box.exec_()
         
mul_win = Multi_Window()
mul_win.setWindowIcon(QIcon('./icons/flower_plant.ico'))
def press_button_mul():
    try:
        a, k = mul_win.click()
        text_box.setText(Multi0(a,k)) 
    except:
        pass    
mul_win.lin_button.clicked.connect(press_button_mul)

class System_Window(QWidget):
    def __init__(self):
        super().__init__() 
        self.lin_line = QVBoxLayout()
        self.setWindowTitle('Системы линейных уравнений')
        self.resize(300,200)
        self.vid_lin = QComboBox()
        self.vid_lin_label = QLabel('Выберите метод решения системы')
        self.lin_line.addWidget(self.vid_lin_label)
        self.lin_line.addWidget(self.vid_lin)
        values=["Графический метод", "Метод подстановки", "Метод сложения"]
        self.vid_lin.addItems(values)
        self.num_lin_label = QLabel('Необходимое количество вариантов')
        self.lin_line.addWidget(self.num_lin_label)
        self.num_lin = QLineEdit()
        self.lin_line.addWidget(self.num_lin)
        self.lin_button = QPushButton('Составить задания')
        self.lin_line.addWidget(self.lin_button)
        self.setLayout(self.lin_line)
    def click(self):
        try:
            a = self.vid_lin.currentIndex()
            k = int(self.num_lin.text())
            self.hide()
            self.num_lin.clear()
            return a, k
        except:
            q_box = QMessageBox()
            q_box.setText('В поле количества нужно ввести число')
            q_box.setWindowTitle('Предупреждение')
            q_box.setWindowIcon(QIcon('./icons/flower_plant.ico'))
            q_box.exec_()
         
sys_win = System_Window()
def press_button_sys():
    try:
        a, k = sys_win.click()
        text_box.setText(System0(a,k)) 
    except:
        pass    
sys_win.lin_button.clicked.connect(press_button_sys)
sys_win.setWindowIcon(QIcon('./icons/flower_plant.ico'))
class System1_Window(QWidget):
    def __init__(self):
        super().__init__() 
        self.lin_line = QVBoxLayout()
        self.setWindowTitle('Стандартные графики')
        self.resize(300,200)
        self.vid_lin = QComboBox()
        self.vid_lin_label = QLabel('Выберите вид первого уравнения системы')
        self.lin_line.addWidget(self.vid_lin_label)
        self.lin_line.addWidget(self.vid_lin)
        values=["y=x²", "y=a/x", "y=√x"]
        self.vid_lin.addItems(values)
        self.num_lin_label = QLabel('Необходимое количество вариантов')
        self.lin_line.addWidget(self.num_lin_label)
        self.num_lin = QLineEdit()
        self.lin_line.addWidget(self.num_lin)
        self.lin_button = QPushButton('Составить задания')
        self.lin_line.addWidget(self.lin_button)
        self.setLayout(self.lin_line)
    def click(self):
        try:
            a = self.vid_lin.currentIndex()
            k = int(self.num_lin.text())
            self.hide()
            self.num_lin.clear()
            return a, k
        except:
            q_box = QMessageBox()
            q_box.setText('В поле количества нужно ввести число')
            q_box.setWindowTitle('Предупреждение')
            q_box.setWindowIcon(QIcon('./icons/flower_plant.ico'))
            q_box.exec_()
         
sys1_win = System1_Window()
def press_button_sys1():
    try:
        a, k = sys1_win.click()
        text_box.setText(System1(a,k)) 
    except:
        pass    
sys1_win.lin_button.clicked.connect(press_button_sys1)
sys1_win.setWindowIcon(QIcon('./icons/flower_plant.ico'))
def kvadratnoe_yravnenie(vid,tip,n):
    ret=''
    answers='\nОтветы:\n'
    for i in range(n):
        if vid == 1:
            a = randint(-10,10)    
            while a == 0:
                a = randint(-10,10)
        else:
            a = 1
        x1 = randint(-10,10)
        while x1 == 0:
            x1 = randint(-10,10)
        if tip == 2:
            x2 = randint(-10,10)
            while x2 == 0 or x2 == x1:
                x2 = randint(-20,20) 
            b = - (a*x2+x1)
            c = x1*x2 
            x1=x1/a
            if round(x1)==x1: x1=round(x1)
            answers+=str(i+1)+'. '+str(x1)+';'+str(x2)+'\n'
        elif tip == 1:
            b = 0
            while b==0 or b%2!=0 or (b*b)%a!=0:
                    b=randint(-40,40)
            c=round(b*b/(4*a))
            x1=-b/(2*a)
            if round(x1)==x1: x1=round(x1)
            answers+=str(i+1)+'. '+str(x1)+'\n'
        else:
            b = randint(-10,10)
            c = round(b*b/(4*a))
            if a > 0: c += randint(1,10)
            else: c -= randint(1,10)
            answers+=str(i+1)+'. нет корней\n'
        if a == 1: ans = 'x²'
        elif a == -1: ans = '-x²'
        else: ans = str(a)+'x²'
        if b >= 0: ans += '+'
        if b == 1: ans += 'x'
        elif b == -1: ans += '-x'
        else: ans += str(b)+'x'
        if c >= 0: ans += '+'
        ans += str(c)+'=0'
        ret += str(i+1)+'. '+ans+'\n'
    return ret+answers
def Type0(n):
    ret=""
    answers='\nОтветы:\n'
    for i in range(n):
        a=0
        b=0
        d=0
        x = randint(-20,20)
        while a==0:
            a=randint(-9,9)
        while b==0:
            b=randint(-9,9)    
        while d==0:
            d=randint(-9,9) 
        c=a*x+b-d*x
        ans=str(i+1)+'. '+str(a)+'x'
        if b>0: ans+='+' 
        ans+= str(b)+'='+str(c)
        if d>0: ans+='+'  
        ans+=str(d)+'x'  
        ret+=ans+'\n'
        answers+=str(i+1)+'. '+str(x)+'\n'
    return ret+answers        
def Type1(n):
    ret=""
    answers='\nОтветы:\n'
    for i in range(n):
        a=0
        b=0
        c=0
        d=0 
        x = randint(-20,20)
        while a==0:
            a=randint(-9,9)
        while b==0:
            b=randint(-9,9)    
        while c==0:
            c=randint(-9,9)   
        while d==0:
            d=randint(-9,9)
        e=a*x+b*(x+c)-d*x
        ans=str(i+1)+'. '+str(a)+'x'
        if b>0: ans+='+' 
        ans+= str(b)+'(x'
        if c>0: ans+='+'  
        ans+=str(c)+')='+str(d)+'x'
        if e>0: ans+='+'
        if e!=0: ans+=str(e)
        ret+=ans+'\n'
        answers+=str(i+1)+'. '+str(x)+'\n'           
    return ret+answers 
def Type2(n):
    ret=""
    answers='\nОтветы:\n'
    for i in range(n):    
        a=0
        b=0
        c=0
        d=0 
        e=0
        x = randint(-20,20)
        while a==0:
            a=randint(-9,9)
        while b==0:
            b=randint(-9,9)    
        while c==0:
            c=randint(-9,9)   
        while d==0:
            d=randint(-9,9)  
        while e==0:
            e=randint(-9,9)
        f=a*(b+c*x)-(d+e*x)
        ans=str(i+1)+'. '+str(a)+'('+str(b)
        if c>0: ans+='+'
        ans+=str(c)+'x)-('+str(d)
        if e>0: ans+='+'
        ans+=str(e)+'x)='+str(f)
        ret+=ans+'\n'
        answers+=str(i+1)+'. '+str(x)+'\n'
    return ret+answers 
def Type3(n):
    ret=""
    answers='\nОтветы:\n'
    for i in range(n):    
        a=0
        b=0
        c=0
        e=0 
        f=0
        g=0
        h=0
        x = randint(-20,20)
        while a==0:
            a=randint(-9,9)
        while b==0:
            b=randint(-9,9)    
        while c==0:
            c=randint(-9,9)   
        while e==0:
            e=randint(-9,9)  
        while f==0:
            f=randint(-9,9)    
        while g==0:
            g=randint(-9,9)   
        while h==0:
            h=randint(-9,9)    
        d=e*x+f*(g*x+h)-a*(b+c*x)
        ans=str(i+1)+'. '+str(a)+'('+str(b)
        if c>0: ans+='+'
        ans+=str(c)+'x)'
        if d>0: ans+='+'
        ans+=str(d)+'='+str(e)+'x'
        if f>0: ans+='+'
        ans+=str(f)+'('+str(g)+'x'
        if h>0: ans+='+'
        ans+=str(h)+')'
        ret+=ans+'\n'
        answers+=str(i+1)+'. '+str(x)+'\n'
    return ret+answers 
def Multi0(vid,n):
    ret=''
    answers='\nОтветы:\n'
    for i in range(n):
        a=0
        b=0
        c=0
        d=0
        e=0
        f=0
        ans=''
        if vid==0:
            while a==0: a=round(random()*50-25,2)
            while b==0: b=round(random()*50-25,2)
            x1 = -a
            x2 = -b
            ans=str(i+1)+'. '+'('
            if randint(0,1)==1: 
                ans+='-'
                x1 *= -1
            ans+='x'
            if a>0: ans+='+'
            ans+=str(a)+')('
            if randint(0,1)==1: 
                ans+='-'
                x2 *= -1
            ans+='x'
            if b>0: ans+='+'
            ans+=str(b)+')=0'
            answers+=str(i+1)+'. '+str(x1)+'; '+str(x2)+'\n'
        if vid==1:
            while a==0:a=randint(-10,10)
            while b==0:b=randint(-10,10)
            while c==0:c=randint(-10,10)
            while d==0:d=randint(-10,10)
            ans=str(i+1)+'. '+'('+str(a)+'x'
            if b>0: ans+='+'
            ans+=str(b)+')('+str(c)
            if d>0: ans+='+'
            x1=-b/a
            if round(x1)==x1: x1=round(x1)
            x2=-c/d
            if round(x2)==x2: x2=round(x2)
            answers+=str(i+1)+'. '+str(x1)+'; '+str(x2)+'\n'
            ans+=str(d)+'x)=0'
        if vid==2:
            while a==0:a=randint(-10,10)
            while b==0:b=randint(-10,10)
            while c==0:c=randint(-10,10)
            while d==0:d=randint(-10,10)
            while e==0:e=randint(-10,10)
            while f==0:f=randint(-10,10)
            ans=str(i+1)+'. '+'('+str(a)+'x'
            if b>0: ans+='+'
            ans+=str(b)+')('+str(c)
            if d>0: ans+='+'
            ans+=str(d)+'x)('+str(e)+'x'
            if f>0: ans+='+'
            ans+=str(f)+')=0'
            x1=-b/a
            if round(x1)==x1: x1=round(x1)
            x2=-c/d
            if round(x2)==x2: x2=round(x2)
            x3=-f/e
            if round(x3)==x3: x3=round(x3)
            answers+=str(i+1)+'. '+str(x1)+'; '+str(x2)+'; '+str(x3)+'\n'            
        if vid==3:
            while a==0:a=randint(-10,10)
            while b==0:b=randint(-10,10)
            while c==0:c=randint(-10,10)
            while d==0:d=randint(-10,10)
            while e==0:e=randint(-10,10)
            ans=str(i+1)+'. '+str(a)+'x('+str(b)
            if c>0: ans+='+'
            ans+=str(c)+'x)('+str(d)+'x'
            if e>0: ans+='+'
            ans+=str(e)+')=0'
            x1=0
            x2=-b/c
            if round(x2)==x2: x2=round(x2)
            x3=-e/d
            if round(x3)==x3: x3=round(x3)
            answers+=str(i+1)+'. '+str(x1)+'; '+str(x2)+'; '+str(x3)+'\n'             
        ret+=ans+'\n'
    return ret+answers 
def System0(vid,n):
    ret=''
    answers='\nОтветы:\n'
    for i in range(n):
        a=0
        b=0
        c=0
        d=0
        ans1=''
        ans2=''
        if vid==0:
            x=randint(-7,7)
            y=randint(-7,7)
            while a==0: a=randint(-5,5)
            while b==0: b=randint(-2,2)
            while c==0: c=randint(-5,5)
            while d==0 or (a/c==b/d): d=randint(-2,2) 
        if vid==1:
            x=randint(-50,50)
            y=randint(-50,50)
            while a==0: a=randint(-10,10)
            while b==0: b=randint(-10,10)
            while c==0: c=randint(-10,10)
            while d==0 or (a/c==b/d): d=randint(-10,10) 
            if abs(a)>2 and abs(b)>2 and abs(c)>2 and abs(d)>2:
                f=randint(1,4)
                k=0
                while k==0: k=randint(-2,2)
                if f==1: a=k
                elif f==2: b=k
                elif f==3: c=k
                else: d=k
        if vid==2:
            x=randint(-50,50)
            y=randint(-50,50)  
            while a==0: a=randint(-10,10)
            while b==0: b=randint(-10,10)
            while c==0: c=randint(-10,10)
            while d==0 or (a/c==b/d): d=randint(-10,10)             
        t=a*x+b*y
        p=c*x+d*y
        ans1 = '⎰ '
        if a==1:ans1+='x'
        elif a==-1: ans1+='-x'
        else: ans1+=str(a)+'x'
        if b>0: ans1+='+'
        if b==-1: ans1+='-'
        elif b!=1: ans1+=str(b)
        ans1+='y='+str(t)
        ans2='⎱ '
        if c==1:ans2+='x'
        elif c==-1: ans2+='-x'
        else: ans2+=str(c)+'x'
        if d>0: ans2+='+'
        if d==-1: ans2+='-'
        elif d!=1: ans2+=str(d)
        ans2+='y='+str(p)
        ret+=ans1+'\n'+ans2+'\n\n'
        answers+=str(i+1)+'. ('+str(x)+'; '+str(y)+')\n'
    return ret+answers
def System1(vid,n):
    ret=''
    answers='\nОтветы:\n'
    for i in range(n):
        if vid == 0:
            x = randint(-3,3)
            y = x**2
            if randint(0,1)==1: y *= -1
            a = 0
            b = 0
            while a==0: a=randint(-10,10)
            while b==0: b=randint(-10,10)
            c = a*x + b*y
            ans1='⎰ y='
            if y < 0: ans1+='-'
            ans1+='x²'
            ans2='⎱ '
            if a==1:ans2+='x'
            elif a==-1: ans2+='-x'
            else: ans2+=str(a)+'x'
            if b>0: ans2+='+'
            if b==-1: ans2+='-'
            elif b!=1: ans2+=str(b)
            ans2+='y='+str(c) 
            ret+=ans1+'\n'+ans2+'\n\n'
            D = a**2 + 4*b*c
            if D > 0:
                x1 = (-a + D**0.5)/(2*b)
                if round(x1) == x1: x1=round(x1)
                x2 = (-a - D**0.5)/(2*b)
                if round(x2) == x2: x2=round(x2)
                y1 = x1**2
                y2 = x2**2
                if y < 0:
                    y1 *= -1
                    y2 *= -1
                answers+=str(i+1)+'. ('+str(x1)+'; '+str(y1)+'),('+str(x2)+'; '+str(y2)+')\n'
            else:
                answers+=str(i+1)+'. ('+str(x)+'; '+str(y)+')\n'
        if vid == 1:
            x = 0
            y = 0
            while x==0: x=randint(-5,5)
            while y==0: y=randint(-5,5)
            d = x*y
            a = 0
            b = 0
            while a==0: a=randint(-10,10)
            while b==0: b=randint(-10,10)
            c = a*x + b*y
            ans1='⎰ y='+str(d)+'/x'
            ans2='⎱ '
            if a==1:ans2+='x'
            elif a==-1: ans2+='-x'
            else: ans2+=str(a)+'x'
            if b>0: ans2+='+'
            if b==-1: ans2+='-'
            elif b!=1: ans2+=str(b)
            ans2+='y='+str(c) 
            ret+=ans1+'\n'+ans2+'\n\n' 
            D = c**2 - 4*a*b*d
            if D > 0:
                x1 = (c + D**0.5)/(2*a)
                if round(x1) == x1: x1=round(x1)
                x2 = (c - D**0.5)/(2*a)
                if round(x2) == x2: x2=round(x2)
                y1 = d / x1
                if round(y1) == y1: y1=round(y1)
                y2 = d / x2
                if round(y2) == y2: y2=round(y2)
                answers+=str(i+1)+'. ('+str(x1)+'; '+str(y1)+'),('+str(x2)+'; '+str(y2)+')\n'
            else:
                answers+=str(i+1)+'. ('+str(x)+'; '+str(y)+')\n'
        if vid == 2:
            y = randint(-4,4)
            x = y**2
            ans1='⎰ y='
            if y < 0: ans1+='-'
            ans1+='√x'
            a = 0
            b = 0
            while a==0: a=randint(-10,10)
            while b==0: b=randint(-10,10)
            c = a*x + b*y
            ans2='⎱ '
            if a==1:ans2+='x'
            elif a==-1: ans2+='-x'
            else: ans2+=str(a)+'x'
            if b>0: ans2+='+'
            if b==-1: ans2+='-'
            elif b!=1: ans2+=str(b)
            ans2+='y='+str(c) 
            ret+=ans1+'\n'+ans2+'\n\n'
            D = b**2 + 4*a*c
            if D > 0:
                y1 = (-b + D**0.5)/(2*a)
                if round(y1) == y1: y1=round(y1)
                y2 = (-b - D**0.5)/(2*a)
                if round(y2) == y2: y2=round(y2)
                x1 = y1**2
                x2 = y2**2
                if (y>=0 and y1>=0 and y2>=0) or (y<0 and y1<=0 and y2<=0):
                    answers+=str(i+1)+'. ('+str(x1)+'; '+str(y1)+'),('+str(x2)+'; '+str(y2)+')\n'
                else:
                    answers+=str(i+1)+'. ('+str(x)+'; '+str(y)+')\n'
            else:
                answers+=str(i+1)+'. ('+str(x)+'; '+str(y)+')\n'
    return ret+answers
main_window.show()
app.exec_()