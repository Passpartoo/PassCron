import tkinter as tk
from tkinter import ttk
from TimeZoneConverter import TimeZoneConverter
from AutomationScript import AutomationScript
from EniCrypt import EniCrypt

root = tk.Tk()
root.geometry("450x300")

tab_control = ttk.Notebook(root)
tab1 = TimeZoneConverter(tab_control)
tab2 = AutomationScript(tab_control)
tab3 = EniCrypt(tab_control)

tab_control.add(tab1, text='TimeZoneConverter')
tab_control.add(tab2, text='AutomationScript')
tab_control.add(tab3, text='EniCrypt')

tab_control.pack(expand=1, fill='both')

root.mainloop()

"""
Ce code ne fournit aucun moyen de communiquer entre les classes.
Si besoin que les classes interagissent entre elles (ex: TimeZoneConverter puisse modifier des variables dans AutomationScript)
Passer des références aux autres classes lors de la création des instances
ou Utiliser un modèle de conception comme l'observateur ou le médiateur.
"""
