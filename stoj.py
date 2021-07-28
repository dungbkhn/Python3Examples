import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, Gdk
from gi.repository import GdkPixbuf

UI_INFO = """
<ui>
  <menubar name='MenuBar'>
    <menu action='FileMenu'>
      <menu action='Connection'>
        <menuitem action='NewStandard' />
        <menuitem action='Close' />
      </menu>
      <separator />
      <menuitem action='QuitApp' />
    </menu>
    <menu action='Option'>
      <menuitem action='Save Connection' />
    </menu>
    <menu action='Help'>
      <menuitem action='Information'/>
      <separator />
      <menuitem action='About'/>
    </menu>
  </menubar>
  <toolbar name='ToolBar'>
    <toolitem action='NewStandard' />
    <toolitem action='CloseCon' />
  </toolbar>
</ui>
"""


class MenuExampleWindow(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="Stoj App")

        self.set_default_size(800, 600)

        action_group = Gtk.ActionGroup(name="my_actions")

        self.add_file_menu_actions(action_group)
        self.add_edit_menu_actions(action_group)
        self.add_choices_menu_actions(action_group)

        uimanager = self.create_ui_manager()
        uimanager.insert_action_group(action_group)

        menubar = uimanager.get_widget("/MenuBar")

        box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        box.pack_start(menubar, False, False, 0)

        toolbar = uimanager.get_widget("/ToolBar")
        box.pack_start(toolbar, False, False, 0)
        
        
        
        self.entry = Gtk.Entry()
        self.entry.set_text("2405:4802:2321:a4e0:872b:27d2:7ce9:ecd7")
        self.entry.set_halign(Gtk.Align.START)
        self.entry.set_valign(Gtk.Align.START)
        self.entry.set_width_chars(36)
        self.label = Gtk.Label(label="  IPAddress")
        self.label.set_halign(Gtk.Align.CENTER)
        self.label.set_valign(Gtk.Align.CENTER)
        
        self.entry2 = Gtk.Entry()
        self.entry2.set_text("xxxx")
        self.entry2.set_halign(Gtk.Align.START)
        self.entry2.set_valign(Gtk.Align.START)
        self.label2 = Gtk.Label(label="  Username")
        self.label2.set_halign(Gtk.Align.CENTER)
        self.label2.set_valign(Gtk.Align.CENTER)
        
        self.pBox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=6)
        self.pBox.pack_start(self.label, False, False, 2)
        self.pBox.pack_start(self.entry, False, False, 2)
        self.pBox.pack_start(self.label2, False, False, 2)
        self.pBox.pack_start(self.entry2, False, False, 2)
        
        self.entry3 = Gtk.Entry()
        self.entry3.set_text("xxxx")
        self.entry3.set_halign(Gtk.Align.START)
        self.entry3.set_valign(Gtk.Align.START)
        self.entry3.set_visibility(False)
        self.label3 = Gtk.Label(label="  Password")
        self.label3.set_halign(Gtk.Align.CENTER)
        self.label3.set_valign(Gtk.Align.CENTER)
        
        self.entry4 = Gtk.Entry()
        self.entry4.set_text("xxxx")
        self.entry4.set_halign(Gtk.Align.START)
        self.entry4.set_valign(Gtk.Align.START)
        self.entry4.set_width_chars(6)
        self.label4 = Gtk.Label(label="  Port")
        self.label4.set_halign(Gtk.Align.CENTER)
        self.label4.set_valign(Gtk.Align.CENTER)
        self.con_button = Gtk.Button(label="Connect")
        
        self.pBox2 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=6)
        self.pBox2.pack_start(self.label3, False, False, 2)
        self.pBox2.pack_start(self.entry3, False, False, 2)
        self.pBox2.pack_start(self.label4, False, False, 2)
        self.pBox2.pack_start(self.entry4, False, False, 2)
        self.pBox2.pack_start(self.con_button, False, False, 2)
        
        self.separator1 = Gtk.Separator()
        box.pack_start(self.separator1, False, False, 4)
        box.pack_start(self.pBox, False, False, 2)
        box.pack_start(self.pBox2, False, False, 2)
        self.separator2 = Gtk.Separator()
        box.pack_start(self.separator2, False, False, 4)

        self.add(box)
        
        
        liststore = Gtk.ListStore(str, GdkPixbuf.Pixbuf)

        icon = GdkPixbuf.Pixbuf.new_from_file_at_size("./a.svg", 16, 16)
        liststore.append(["Fedora", icon])
        icon = GdkPixbuf.Pixbuf.new_from_file_at_size("./a.svg", 16, 16)
        liststore.append(["OpenSuSE", icon])
        icon = GdkPixbuf.Pixbuf.new_from_file_at_size("./a.svg", 16, 16)
        liststore.append(["Gentoo", icon])

        self.treeview = Gtk.TreeView()
        self.treeview.set_model(liststore)
        box.pack_start(self.treeview, False, False, 4)

        cellrenderertext = Gtk.CellRendererText()

        treeviewcolumn = Gtk.TreeViewColumn("Distribution")
        self.treeview.append_column(treeviewcolumn)
        treeviewcolumn.pack_start(cellrenderertext, True)
        treeviewcolumn.add_attribute(cellrenderertext, "text", 0)

		
        cellrendererpixbuf = Gtk.CellRendererPixbuf()

        treeviewcolumn = Gtk.TreeViewColumn("Logo")
        self.treeview.append_column(treeviewcolumn)
        treeviewcolumn.pack_start(cellrendererpixbuf, False)
        treeviewcolumn.add_attribute(cellrendererpixbuf, "pixbuf", 1)
        
        
        self.download_button = Gtk.Button(label="Download")
        self.separator3 = Gtk.Separator()
        
        box.pack_end(self.download_button, False, False, 4)
        box.pack_end(self.separator3, False, False, 4)

    def add_file_menu_actions(self, action_group):
        action_filemenu = Gtk.Action(name="FileMenu", label="Program")
        action_group.add_action(action_filemenu)

        action_filenewmenu = Gtk.Action(name="Connection", label="Connection")
        action_group.add_action(action_filenewmenu)

        action_new = Gtk.Action(
            name="NewStandard",
            label="_New Connection",
            tooltip="Create a new connection",
            stock_id=Gtk.STOCK_NEW,
        )
        action_new.connect("activate", self.on_menu_con_new_generic)
        action_group.add_action_with_accel(action_new, None)

        action_group.add_actions(
            [
                (
                    "Close",
                    None,
                    "Close Connection",
                    None,
                    "Close connection",
                    self.on_menu_con_close_generic,
                ),
            ]
        )

        action_pquit = Gtk.Action(name="CloseCon", stock_id=Gtk.STOCK_QUIT)
        action_pquit.connect("activate", self.on_menu_con_close_generic)
        action_group.add_action(action_pquit)
        
        action_fileqamenu = Gtk.Action(name="QuitApp", label="Quit")
        action_fileqamenu.connect("activate", self.on_menu_file_quit)
        action_group.add_action(action_fileqamenu)

    def add_edit_menu_actions(self, action_group):
        action_group.add_actions(
            [
                ("Option", None, "Options"),
                ("Save Connection", None, "Save Connection", None, None, self.on_menu_others),
                
            ]
        )

    def add_choices_menu_actions(self, action_group):
        action_group.add_action(Gtk.Action(name="Help", label="Help"))
        action_fileinfomenu = Gtk.Action(name="Information", label="Information")
        action_fileinfomenu.connect("activate", self.on_menu_others)
        action_group.add_action(action_fileinfomenu)

        action_fileaboutmenu = Gtk.Action(name="About", label="About")
        action_fileaboutmenu.connect("activate", self.on_menu_others)
        action_group.add_action(action_fileaboutmenu)
        
        

    def create_ui_manager(self):
        uimanager = Gtk.UIManager()

        # Throws exception if something went wrong
        uimanager.add_ui_from_string(UI_INFO)

        # Add the accelerator group to the toplevel window
        accelgroup = uimanager.get_accel_group()
        self.add_accel_group(accelgroup)
        return uimanager

    def on_menu_con_new_generic(self, widget):
        print("A File|New menu item was selected.")
        
    def on_menu_con_close_generic(self, widget):
        print("Close menu item was selected.")

    def on_menu_file_quit(self, widget):
        Gtk.main_quit()

    def on_menu_others(self, widget):
        print("Menu item " + widget.get_name() + " was selected")

    
window = MenuExampleWindow()
window.connect("destroy", Gtk.main_quit)
window.show_all()
Gtk.main()
