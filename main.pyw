import dearpygui.dearpygui as dpg
from time import time, sleep
from datetime import timedelta

t1 = time()
dt = time() - t1
pt = time()
running = False

def start(btn, adata, udata):
    global running, t1, pt, ptx
    running = True if dpg.get_item_label(btn) == 'Start' else False

    if running:  # sets True when pressed first time
        t1 += time() - pt
        dpg.set_item_label(btn, 'Pause')
    else:
        pt = time()
        dpg.set_item_label(btn, 'Start')


def reset(btn, adata, udata):
    x = True if dpg.get_item_label(btn) == 'Reset' else False
    if x:
        dpg.set_item_label(btn, 'You sure?')
    else:
        dpg.set_item_label(btn, 'Reset')

        global running, t1, pt, dt
        running = False
        dpg.set_item_label('start', 'Start')
        dt = 0
        t1 = time()
        pt = time()

def quit(btn, adata, udata):
    x = True if dpg.get_item_label(btn) == 'Quit' else False
    if x:
        dpg.set_item_label(btn, 'You sure?')
    else:
        dpg.set_item_label(btn, 'Quit')
        dpg.stop_dearpygui()
        dpg.destroy_context()
        quit()

while True:
    dpg.create_context()

    with dpg.window(tag="Primary Window"):
        dpg.add_text('Stopwatch', tag='time')
        dpg.add_button(width=100, label='Start', callback=start, tag='start')
        dpg.add_same_line()
        dpg.add_button(width=100, label='Reset', callback=reset)
        dpg.add_text() # TODO: разобраться с разметкой и сделать нормально...
        dpg.add_text()
        dpg.add_text()
        dpg.add_separator()
        dpg.add_button(width=100, label='Quit', callback=quit)

    dpg.create_context()
    dpg.create_viewport(title='Coding Stopwatch',
                        width=300, height=200, max_width=300, max_height=200, min_width=300, min_height=200)
    dpg.setup_dearpygui()
    dpg.show_viewport()
    dpg.set_primary_window("Primary Window", True)
    while dpg.is_dearpygui_running():
        # you can manually stop by using stop_dearpygui()
        if running:
            dt = time() - t1
        try:
            dpg.set_value('time', f'{str(timedelta(seconds=dt))[:7]} ({dt:.2f})')

            dpg.render_dearpygui_frame()
        except Exception as e:
            print(e)
            break

    dpg.destroy_context()