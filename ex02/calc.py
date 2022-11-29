import tkinter as tk
import tkinter.messagebox as tkm

# def button_click(event):
    #btn = event.widget
    #txt = btn["text"]
    #tkm.showinfo(txt, f"[{txt}]ボタンが押されたぞ")
    #tkm.showwarning("WARNING", "")


#root = tk. Tk() #tkモジュールのTKクラスを生成
#root.title("電卓やで")
#root.geometry("300x500")

#for num in range(10):
    #buttonlist = []
    #button = tk.Button(root, text=f"{num}", width=4, height=2, font =("", 30))
    #buttonlist += button
#for i in range(5):
    #for j in range(3):
            #button.grid(row = i, column = j)
            #print(i)
            #print(j)
        #button.bind(("<1>", button_click))

#root.mainloop()

# 練習３
def button_click(event):
    btn = event.widget
    num = btn["text"]
    if num == "=":
        siki = entry.get() # 数式の文字列
        res = eval(siki) # 数式文字列の評価
        entry.delete(0, tk.END) # 表示文字列の削除
        entry.insert(tk.END, res) # 結果の挿入
    elif num == "aldel":
        entry.delete(0, tk.END)
    elif num == "del":
        entry.delete(len(entry.get())-1, tk.END)#1文字ずつの削除する
    else: # 「=」以外のボタン字
        #tkm.showinfo("", f"{num}ボタンがクリックされました")
        # 練習６
        entry.insert(tk.END, num)

    
# 練習１
root = tk.Tk()
root.geometry("300x500")

# 練習４
entry = tk.Entry(root, justify="right", width=10, font=("",40))
entry.grid(row=0, column=0, columnspan=3)

# 練習２
r, c = 1, 0
for num in range(9, -1, -1):
    button = tk.Button(root, text=f"{num}", width=4, height=2, font=("", 30))
    button.grid(row=r, column=c)
    button.bind("<1>", button_click)
    c += 1
    if c%3 == 0:
        r += 1
        c = 0

# 練習５
operators = ["+", "-", "*", "/", "="] #四則演算対応
for ope in operators:
    button = tk.Button(root, text=f"{ope}", width=4, height=2, font=("", 30))
    button.grid(row=r, column=c)
    button.bind("<1>", button_click)
    c += 1
    if c%3 == 0:
        r += 1
        c = 0

#追加機能
deleters = ["del", "aldel"]
for delbut in deleters:
    button = tk.Button(root, text=f"{delbut}", width=4, height=2, font=("", 30))
    button.grid(row=r, column=c)
    button.bind("<1>", button_click)
    c += 1
    if c%3 == 0:
        r += 1
        c = 0



root.mainloop()