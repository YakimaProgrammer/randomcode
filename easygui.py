def button_box(msg,choices,choice_name,h1_text='',title="PSG",destination_page=''):
    msg = msg.replace("\n","</p><p>")
    if choices == []:
        choices = ["[Back]"]
    buttons = []
    for i in choices:
        buttons.append(f"<button name = '{choice_name}' value = '{i}' type = 'submit'>{i}</button>")
    table = "<table><tr>"
    for i in buttons:
        table += f"<td>{i}</td>"
    table += "</tr></table>"
    return f"<html><header><title>{title}</title></header><body><h1>{h1_text}</h1><p>{msg}</p><form action = '{destination_page}' method = 'post'>{table}</form></body></html>"

#Will need to be updated ##def choice_box(msg,choices,choice_name,h1_text='',title="PSG",destination_page=''):
##    msg = msg.replace("\n","</p><p>")
##    buttons = []
##    for i in choices:
##        buttons.append(f"<button name = '{choice_name}' value = '{i}' type = 'submit'>{i}</button>")
##    table = "<table>"
##    for i in buttons:
##        table += f"<tr><td>{i}</td></tr>"
##    table += "</table>"
##    return f"<html><header><title>{title}</title></header><body><h1>{h1_text}</h1><p>{msg}</p><form action = '{destination_page}' method = 'post'>{table}</form></body></html>"

def msg_box(msg,h1_text="",title="PSG",button_label="OK",destination_page=''):
    msg = msg.replace("\n","</p><p>")
    return f"<html><header><title>{title}</title></header><body><h1>{h1_text}</h1><p>{msg}</p><form action = '{destination_page}' method = 'post'><input type = 'submit' value = \"{button_label}\"></form></body></html>"

def enter_box(msg,choice_name,h1_text="",title="PSG",button_label="OK",destination_page=''):
    msg = msg.replace("\n","</p><p>")
    return f"<html><header><title>{title}</title></header><body><h1>{h1_text}</h1><p>{msg}</p><form action = '{destination_page}' method = 'post'><input type = 'text' name = '{choice_name}'><br><input type = 'submit' value = \"{button_label}\"></form></body></html>"
