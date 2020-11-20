bl_info = {
    "name": "Create Dataset",
    "blender": (2, 90, 1),
    "category": "All",
}

if "bpy" in locals():
    import importlib
    importlib.reload(dataset_creator)

else:
    from . import dataset_creator

import bpy
from bpy.app.handlers import persistent
from .drag_panel_op import DP_OT_draw_operator

addon_keymaps = []

@persistent
def load_handler(scene):
    bpy.ops.object.dp_ot_draw_operator('INVOKE_DEFAULT')

def register():
    bpy.utils.register_class(dataset_creator.CreateDataset)
    bpy.app.handlers.load_post.append(load_handler)

    bpy.utils.register_class(DP_OT_draw_operator)
    kcfg = bpy.context.window_manager.keyconfigs.addon
    if kcfg:
        km = kcfg.keymaps.new(name='3D View', space_type='VIEW_3D')

        kmi = km.keymap_items.new("object.dp_ot_draw_operator", 'F', 'PRESS', shift=True, ctrl=True)

        addon_keymaps.append((km, kmi))


def unregister():
        for km, kmi in addon_keymaps:
        km.keymap_items.remove(kmi)
    addon_keymaps.clear()

    bpy.utils.unregister_class(DP_OT_draw_operator)
    bpy.app.handlers.load_post.remove(load_handler)
    bpy.utils.unregister_class(dataset_creator.CreateDataset)


# This allows you to run the script directly from Blender's Text editor
# to test the add-on without having to install it.
if __name__ == "__main__":
    register()
