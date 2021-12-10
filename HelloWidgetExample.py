# Created with Pyto
import widgets as wd

def hello_world():
    title = "Hello World"
    subtitle = "More Text!"
    return title, subtitle
    
posts = hello_world()
widget = wd.Widget()

#No frills text
title = wd.Text(posts[0])
subtitle = wd.Text(posts[1])

#Other ways to do build sizes but this is easy.
layouts = [widget.small_layout, widget.medium_layout, widget.large_layout]
for l in layouts:
    l.add_row([title])
    l.add_row([subtitle])
    
# reload in 5 hours
wd.schedule_next_reload(60*60*5)
wd.show_widget(widget)
