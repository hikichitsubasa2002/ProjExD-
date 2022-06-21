
import tkinter as tk
import tkinter.messagebox as tkm

def button_click(event):
    btn = event.widget
    num = btn["text"]
    if num == "=":
        epn = entry.get()
        res = eval(epn)
        print(res)
        entry.delete(0,tk.END)
        entry.insert(tk.END,res)
    else:
        entry.insert(tk.END, num)
    if num == "C":
        entry.delete(0,tk.END)
        entry.insert(tk.END)
    
    if num == "AC":
        cl = entry.get()
        ac = cl[::-1]
        entry.delete(0,tk.END)
        entry.insert(tk.END,str(ac))
    else:
        entry.insert(tk.END, num)
        
def button_C(event):
    entry.delete(0,tk.END)
    entry.insert(tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    root.title("電卓")
    #root.geometry("300x500")
      
    entry = tk.Entry(root, justify="right",width=10,font=("Times New Roman",40))
    entry.grid(row=0,column=0,columnspan=3) 
    
    r,c = 1, 0
    for i, num in enumerate([i for i in range(9, -1, -1)]+["+","-","=","AC","C"]):
        btn = tk.Button(root,
                        text=num,
                        width=5,
                        height=3,
                        font=("Helvetica",30),
                        bg ="#434445",
                        fg = "#ff0000",
                    )

        btn.bind("<1>",button_click)
        btn.grid(row=r,column=c)
        c += 1
        if (i+1)%5 == 0:
            r += 1
            c = 0

    root.mainloop()