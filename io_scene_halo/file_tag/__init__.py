# ##### BEGIN MIT LICENSE BLOCK #####
#
# MIT License
#
# Copyright (c) 2023 Steven Garcia
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
#
# ##### END MIT LICENSE BLOCK #####

import os
import bpy

from bpy_extras.io_utils import (
    ImportHelper,
    ExportHelper
    )

from bpy.types import Operator

from bpy.props import (
    BoolProperty,
    EnumProperty,
    StringProperty,
    CollectionProperty
    )

from ..global_functions import global_functions

class ExportSCNR(Operator, ExportHelper):
    """Write a scenario tag file"""
    bl_idname = "export_scene.scnr"
    bl_label = "Export Scenario"
    filename_ext = '.scenario'

    filter_glob: StringProperty(
        default="*.scenario",
        options={'HIDDEN'},
        )

    def execute(self, context):
        from . import export_tag

        return global_functions.run_code("export_tag.write_file(context, self.filepath, self.report)")

try:
    from bpy.types import (
        FileHandler,
        OperatorFileListElement
        )

    class ImportTag(Operator, ImportHelper):
        """Import a tag for various Halo titles"""
        bl_idname = "import_scene.tag"
        bl_label = "Import Tag"

        game_title: EnumProperty(
            name="Game:",
            description="What game does the tag group belong to",
            items=[ ('auto', "Auto", "Attempt to get the game title automatically. Defaults to Halo 1 if it fails."),
                    ('halo1', "Halo 1", "Use tag data from Halo 1"),
                    ('halo2', "Halo 2", "Use tag data from Halo 2"),
                    ('halo3', "Halo 3", "Use tag data from Halo 3"),
                ]
            )

        fix_rotations: BoolProperty(
            name ="Fix Rotations",
            description = "Set rotations to match what you would visually see in 3DS Max. Rotates bones by 90 degrees on a local Z axis to match how Blender handles rotations",
            default = False,
            )

        empty_markers: BoolProperty(
            name ="Generate Empty Markers",
            description = "Generate empty markers instead of UV spheres",
            default = True,
            )

        directory: StringProperty(
            subtype='FILE_PATH', 
            options={'SKIP_SAVE'}
            )
        
        files: CollectionProperty(
            type=OperatorFileListElement, 
            options={'SKIP_SAVE'}
            )

        def execute(self, context):
            from ..file_tag import import_tag

            if not self.directory:
                return {'CANCELLED'}
            
            for file in self.files:
                filepath = os.path.join(self.directory, file.name)
                print(filepath)
                global_functions.run_code("import_tag.load_file(context, filepath, self.game_title, self.fix_rotations, self.empty_markers, self.report)")

            return {'FINISHED'}

        def invoke(self, context, event):
            if self.directory:
                return self.execute(context)
            context.window_manager.fileselect_add(self)
            return {'RUNNING_MODAL'}

        def draw(self, context):
            layout = self.layout

            box = layout.box()
            box.label(text="Game Title:")
            col = box.column(align=True)
            row = col.row()
            row.prop(self, "game_title", text='')
            col = box.column(align=True)

            box = layout.box()
            box.label(text="Import Options:")
            col = box.column(align=True)

            row = col.row()
            row.label(text='Fix Rotations:')
            row.prop(self, "fix_rotations", text='')
            row = col.row()
            row.label(text='Use Empties For Markers:')
            row.prop(self, "empty_markers", text='')

    class ImportTag_FileHandler(FileHandler):
        bl_idname = "TAG_FH_import"
        bl_label = "File handler for tag import"
        bl_import_operator = "import_scene.tag"
        bl_file_extensions = ".model;.gbxmodel;.model_collision_geometry;.model_animations;.physics;.scenario_structure_bsp;.scenario;.camera_track;.render_model;.shader_environment;.shader_model;.shader_transparent_meter;.shader_transparent_glass"

        @classmethod
        def poll_drop(cls, context):
            return (context.area and context.area.type == 'VIEW_3D')

except ImportError:
    print("Blender is out of date. Drag and drop will not function")
    FileHandler = None
    class ImportTag(Operator, ImportHelper):
        """Import a tag for various Halo titles"""
        bl_idname = "import_scene.tag"
        bl_label = "Import Tag"

        game_title: EnumProperty(
            name="Game:",
            description="What game does the tag group belong to",
            items=[ ('auto', "Auto", "Attempt to get the game title automatically. Defaults to Halo 1 if it fails."),
                    ('halo1', "Halo 1", "Use tag data from Halo 1"),
                    ('halo2', "Halo 2", "Use tag data from Halo 2"),
                    ('halo3', "Halo 3", "Use tag data from Halo 3"),
                ]
            )

        fix_rotations: BoolProperty(
            name ="Fix Rotations",
            description = "Set rotations to match what you would visually see in 3DS Max. Rotates bones by 90 degrees on a local Z axis to match how Blender handles rotations",
            default = False,
            )

        empty_markers: BoolProperty(
            name ="Generate Empty Markers",
            description = "Generate empty markers instead of UV spheres",
            default = True,
            )

        def execute(self, context):
            from ..file_tag import import_tag

            global_functions.run_code("import_tag.load_file(context, self.filepath, self.game_title, self.fix_rotations, self.empty_markers, self.report)")

            return {'FINISHED'}

        def draw(self, context):
            layout = self.layout

            box = layout.box()
            box.label(text="Game Title:")
            col = box.column(align=True)
            row = col.row()
            row.prop(self, "game_title", text='')
            col = box.column(align=True)

            box = layout.box()
            box.label(text="Import Options:")
            col = box.column(align=True)

            row = col.row()
            row.label(text='Fix Rotations:')
            row.prop(self, "fix_rotations", text='')
            row = col.row()
            row.label(text='Use Empties For Markers:')
            row.prop(self, "empty_markers", text='')

classeshalo = [
    ImportTag,
    ExportSCNR
]

if not FileHandler == None:
    classeshalo.append(ImportTag_FileHandler)

def menu_func_export(self, context):
    self.layout.operator(ExportSCNR.bl_idname, text="Halo Scenario (.scenario)")

def menu_func_import(self, context):
    self.layout.operator(ImportTag.bl_idname, text="Halo Tag (mode/mod2/coll/phys/antr/sbsp)")

def register():
    for clshalo in classeshalo:
        bpy.utils.register_class(clshalo)

    bpy.types.TOPBAR_MT_file_export.append(menu_func_export)
    bpy.types.TOPBAR_MT_file_import.append(menu_func_import)

def unregister():
    bpy.types.TOPBAR_MT_file_export.remove(menu_func_export)
    bpy.types.TOPBAR_MT_file_import.remove(menu_func_import)
    for clshalo in classeshalo:
        bpy.utils.unregister_class(clshalo)

if __name__ == '__main__':
    register()
