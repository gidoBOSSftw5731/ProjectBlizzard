import signal
import os
from gi.repository import Gtk as gtk
from gi.repository import AppIndicator3 as appindicator

APPINDICATOR_ID = 'myappindicator'
filepath = "/tmp/doIlock"

def main():
    indicator = appindicator.Indicator.new(APPINDICATOR_ID, gtk.STOCK_INFO, appindicator.IndicatorCategory.SYSTEM_SERVICES)
    indicator.set_status(appindicator.IndicatorStatus.ACTIVE)
    indicator.set_menu(build_menu())
    gtk.main()

def build_menu():
    menu = gtk.Menu()
    item_quit = gtk.MenuItem('Quit')
    item_quit.connect('activate', quit)
    menu.append(item_quit)
    
    item_toggle = gtk.CheckMenuItem('Toggle Lock')
    item_toggle.set_active("active")
    item_toggle.connect('activate', toggle_func)
    menu.append(item_toggle)
    
    menu.show_all()
    return menu

def toggle_func(is_toggled):
    f = open(os.open(filepath, os.O_CREAT | os.O_WRONLY, 0o644), 'w+')
    
    if item_toggle.get_active:
        f.write("false") # we do not want to act on this
    else:
        f.write("true")

def quit(source):
    gtk.main_quit()

if __name__ == "__main__":
    signal.signal(signal.SIGINT, signal.SIG_DFL)
    main()