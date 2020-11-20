import bpy

class Spawner:

    @staticmethod
    def add_table():
        bpy.ops.mesh.primitive_cube_add()
        scene = bpy.context.scene
        for obj in scene.objects:
            # TODO: change hardcoded shpae name to something descriptive, otherwise affects all 'Cube's
            if obj.name == 'Cube':
                bpy.ops.object.select_all(action='DESELECT')
                obj.select_set(True)
                bpy.context.view_layer.objects.active = obj
                obj.dimensions = [12, 12, 0.2]
                obj.location = [0, 0, -0.5]
                obj.scale = [1.5, 1.5, 0.1]
                bpy.ops.rigidbody.object_add(type='PASSIVE')

    @staticmethod
    def delete_all_objects_in_scene(only_fruit=True):
        # if bpy.context.object.mode == 'EDIT':
        #     bpy.ops.object.mode_set(mode='OBJECT')
        # deselect all objects
        bpy.ops.object.select_all(action='DESELECT')

        candidate_list = [item.name for item in bpy.data.objects]

        for obj in candidate_list:
            # select the object
            bpy.data.objects[obj].select_set(True)
            # delete all selected objects
            # bpy.data.objects.remove(bpy.data.objects[obj], do_unlink=True)
            bpy.ops.object.delete(use_global=True)
