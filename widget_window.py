import tkinter
subscriber_count = 0

def reset_subscribers():
    global subscriber_count
    subscriber_count = 0
    subscriber_label.config(text=f"{subscriber_count} subscribers")
    feedback_label.config(text="")
    subscriber_entry.delete(0, tkinter.END)


def read_subscriber_input():
    global subscriber_count
    try:
        new_count = int(subscriber_entry.get())
        if new_count < 0:
            feedback_label.config(text="Subscriber count cannot be negative.")
            return
        subscriber_count = new_count
        subscriber_label.config(text=f"{new_count} subscribers")
        feedback_label.config(text="")
        subscriber_entry.delete(0, tkinter.END)
    except ValueError:
        feedback_label.config(text="Please enter a valid number.")


window = tkinter.Tk()
window.title("Subscriber Tracker")
window.geometry("400x250")
window.configure(bg="#F7F3E8")
title_label = tkinter.Label(window, text="Subscriber Tracker", bg="#F7F3E8", font=("Arial", 14, "bold"))
title_label.pack(pady=10)

subscriber_label = tkinter.Label(
    window,
    text=f"{subscriber_count} subscribers",
    font=("Arial", 24),
    fg="#36594A", 
    bg="#F7F3E8")
subscriber_label.pack()

reset_button = tkinter.Button(window, text="Reset Count", command=reset_subscribers, bg="#B8D4C2", fg="#263B30")
reset_button.pack(pady=5)
subscriber_entry = tkinter.Entry(window)
subscriber_entry.pack()
submit_button = tkinter.Button(window, text="Submit Count", command=read_subscriber_input, bg="#729D8F", fg="white")
submit_button.pack()
feedback_label = tkinter.Label(window, text="", bg="#F7F3E8", fg="#A13E43")
feedback_label.pack()
window.mainloop()