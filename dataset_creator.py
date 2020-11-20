import bpy

class CreateDataset(bpy.types.Operator):
    """My Object Moving Script"""  # Use this as a tooltip for menu items and buttons.
    bl_idname = "object.createdataset"  # Unique identifier for buttons and menu items to reference.
    bl_label = "Create a dataset"  # Display name in the interface.
    bl_options = {'REGISTER', 'UNDO'}  # Enable undo for the operator.

    @staticmethod
    def delete_all_objects_in_scene():

        bpy.ops.object.select_all(action='DESELECT')
        candidate_list = [item.name for item in bpy.data.objects]

        for obj in candidate_list:
            # select the object
            bpy.data.objects[obj].select_set(True)
            # delete all selected objects
            bpy.ops.object.delete(use_global=True)

    def execute(self, context):  # execute() is called when running the operator.

        def pre_frame(scene):
            if scene.frame_current == 90:
                print("frame 90")

        bpy.app.handlers.frame_change_pre.append(pre_frame)
        if not bpy.context.screen.is_animation_playing:
            bpy.ops.screen.animation_play()
        return {'FINISHED'}  # Lets Blender know the operator finished successfully.