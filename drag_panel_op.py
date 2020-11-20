from .bl_ui_label import *
from .bl_ui_button import *
from .bl_ui_drag_panel import *
from .bl_ui_draw_op import *
from . import spawner

class DP_OT_draw_operator(BL_UI_OT_draw_operator):
    bl_idname = "object.dp_ot_draw_operator"
    bl_label = "bl ui widgets custom operator"
    bl_description = "Demo operator for bl ui widgets"
    bl_options = {'REGISTER'}

    def __init__(self):

        super().__init__()

        self.spn = spawner.Spawner()

        self.panel = BL_UI_Drag_Panel(100, 300, 300, 290)
        self.panel.bg_color = (0.2, 0.2, 0.2, 0.9)

        self.label = BL_UI_Label(20, 10, 100, 15)
        self.label.text = "Size:"
        self.label.text_size = 14
        self.label.text_color = (0.2, 0.9, 0.9, 1.0)

        self.button1 = BL_UI_Button(20, 100, 120, 30)
        self.button1.bg_color = (0.2, 0.8, 0.8, 0.8)
        self.button1.hover_bg_color = (0.2, 0.9, 0.9, 1.0)
        self.button1.text = "Start dataset generation"
        # self.button1.set_image("//img/scale.png")
        self.button1.set_image_size((24, 24))
        self.button1.set_image_position((4, 2))
        self.button1.set_mouse_down(self.button1_press)

        self.button2 = BL_UI_Button(160, 100, 120, 30)
        self.button2.bg_color = (0.2, 0.8, 0.8, 0.8)
        self.button2.hover_bg_color = (0.2, 0.9, 0.9, 1.0)
        self.button2.text = "Stop and clear scene"
        # self.button2.set_image("//img/rotate.png")
        self.button2.set_image_size((24, 24))
        self.button2.set_image_position((4, 2))
        self.button2.set_mouse_down(self.button2_press)


    def on_invoke(self, context, event):

        # Add new widgets here (TODO: perhaps a better, more automated solution?)
        # widgets_panel = [self.label, self.label_size, self.button1, self.button2, self.slider, self.up_down,
        #                  self.chb_visibility, self.chb_1, self.chb_2]
        widgets_panel = [self.label, self.button1, self.button2]
        widgets = [self.panel]

        widgets += widgets_panel
        print("DRAG PANEL OP: ", context)
        self.init_widgets(context, widgets)

        self.panel.add_widgets(widgets_panel)

        # Open the panel at the mouse location
        self.panel.set_location(event.mouse_x,
                                context.area.height - event.mouse_y + 20)

    def on_chb_visibility_state_change(self, checkbox, state):
        active_obj = bpy.context.view_layer.objects.active
        if active_obj is not None:
            active_obj.hide_viewport = not state

    def on_up_down_value_change(self, up_down, value):
        active_obj = bpy.context.view_layer.objects.active
        if active_obj is not None:
            active_obj.scale = (1, 1, value)

    def on_slider_value_change(self, slider, value):
        active_obj = bpy.context.view_layer.objects.active
        if active_obj is not None:
            active_obj.scale = (1, 1, value)

    # Button press handlers
    def button1_press(self, widget):
        spawner.Spawner.add_table()
        print("Button '{0}' is pressed".format(widget.text))

    def button2_press(self, widget):
        print("Button '{0}' is pressed".format(widget.text))
        bpy.ops.screen.animation_cancel(restore_frame=False)
        bpy.context.scene.frame_set(0)
        spawner.Spawner.delete_all_objects_in_scene(False)
        bpy.ops.wm.save_as_mainfile(filepath=bpy.data.filepath)
        bpy.ops.wm.open_mainfile(filepath=bpy.data.filepath)


