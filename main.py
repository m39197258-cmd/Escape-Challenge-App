import tkinter as tk
import random
from tkinter import messagebox

def handle_exit():
    # هذا الكود سينفذ "حققاً حقاً" إذا تم الضغط على الزر
    messagebox.showinfo("مذهل!", "لقد فعلتها! أنت أسرع من البرق ومن كل الكواكب المارقة! ⚡")
    root.destroy()

def move_button(event):
    # الهروب السريع عند اقتراب الماوس
    new_x = random.randint(50, root.winfo_width() - 70)
    new_y = random.randint(50, root.winfo_height() - 70)
    exit_button.place(x=new_x, y=new_y)

# إنشاء النافذة
root = tk.Tk()
root.title("لن تستطيع إغلاقي هاهاها! 😂")
root.geometry("700x700")
root.configure(bg="white")

# قفل زر الإغلاق الأصلي العلوي
root.protocol("WM_DELETE_WINDOW", lambda: None)

# جملة التحدي
label = tk.Label(root, text="اتحداك ان تغلقني !😂", fg="black", bg="white", font=("Arial", 18, "bold"))
label.pack(pady=30)

# إنشاء الزر (مربع بنفس استايل المستطيل السابق)
# العرض 4 والارتفاع 2 يجعله مربعاً متناسقاً على الشاشة
exit_button = tk.Button(root, text="X", bg="red", fg="white",
                       font=("Arial", 14, "bold"), width=4, height=2,
                       command=handle_exit, relief="raised", bd=4)

# وضعه في مكان عشوائي عند البداية
exit_button.place(x=320, y=320)

# ربط الهروب بملامسة الماوس (Enter)
exit_button.bind("<Enter>", move_button)

root.mainloop()
