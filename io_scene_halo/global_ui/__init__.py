# ##### BEGIN MIT LICENSE BLOCK #####
#
# MIT License
#
# Copyright (c) 2020 Steven Garcia
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

import bpy
import sys
import argparse

from bpy.types import (
        Panel,
        PropertyGroup
        )

from bpy.props import (
        IntProperty,
        BoolProperty,
        EnumProperty,
        FloatProperty,
        StringProperty,
        PointerProperty,
        FloatVectorProperty
        )

from ..global_functions import global_functions

class ASS_JMS_MaterialProps(Panel):
    bl_label = "Halo Material Properties"
    bl_idname = "ASS_JMS_PT_MaterialPanel"
    bl_space_type = 'PROPERTIES'
    bl_region_type = 'WINDOW'
    bl_context = "material"
    bl_options = {'DEFAULT_CLOSED'}

    @classmethod
    def poll(self, context):
        mat = context.material

        return mat

    def draw_header(self, context):
        current_material = context.object.active_material
        if current_material is not None:
            material_ass_jms = current_material.ass_jms
            self.layout.prop(material_ass_jms, "is_bm", text='')

    def draw(self, context):
        layout = self.layout
        scene = context.scene
        scene_halo = scene.halo
        current_material = context.object.active_material
        if current_material is not None:
            material_ass_jms = current_material.ass_jms
            layout.enabled = material_ass_jms.is_bm
            if scene_halo.game_version == 'halo2' or scene_halo.game_version == 'halo3':
                row = layout.row()
                row.label(text="Material Effect:")
                row.prop(material_ass_jms, "material_effect", text='')

class ASS_JMS_MaterialFlagsProps(Panel):
    bl_label = "Flags"
    bl_idname = "ASS_JMS_PT_MaterialFlagsPanel"
    bl_space_type = 'PROPERTIES'
    bl_region_type = 'WINDOW'
    bl_context = "material"
    bl_options = {'DEFAULT_CLOSED'}
    bl_parent_id = "ASS_JMS_PT_MaterialPanel"

    def draw(self, context):
        layout = self.layout
        scene = context.scene
        scene_halo = scene.halo
        current_material = context.object.active_material
        if current_material is not None:
            material_ass_jms = current_material.ass_jms
            layout.enabled = material_ass_jms.is_bm
            box = layout.split()
            col = box.column(align=True)
            row = col.row()

            if scene_halo.game_version == 'haloce':
                row = col.row()
                row.label(text='Two-sided:')
                row.prop(material_ass_jms, "two_sided", text='')
                row = col.row()
                row.label(text='Transparent:')
                row.prop(material_ass_jms, "transparent_1_sided", text='')
                row = col.row()
                row.label(text='Render Only:')
                row.prop(material_ass_jms, "render_only", text='')
                row = col.row()
                row.label(text='Large Collideable:')
                row.prop(material_ass_jms, "sphere_collision_only", text='')
                row = col.row()
                row.label(text='Fog Plane:')
                row.prop(material_ass_jms, "fog_plane", text='')
                row = col.row()
                row.label(text='Ladder:')
                row.prop(material_ass_jms, "ladder", text='')
                row = col.row()
                row.label(text='Breakable:')
                row.prop(material_ass_jms, "breakable", text='')
                row = col.row()
                row.label(text='AI Deafening:')
                row.prop(material_ass_jms, "ai_deafening", text='')
                row = col.row()
                row.label(text='Collision Only:')
                row.prop(material_ass_jms, "collision_only", text='')
                row = col.row()
                row.label(text='Exact Portal:')
                row.prop(material_ass_jms, "portal_exact", text='')

            if scene_halo.game_version == 'halo2':
                row = col.row()
                row.label(text='Two-sided:')
                row.prop(material_ass_jms, "two_sided", text='')
                row = col.row()
                row.label(text='One-sided Transparent:')
                row.prop(material_ass_jms, "transparent_1_sided", text='')
                row = col.row()
                row.label(text='Two-sided Transparent:')
                row.prop(material_ass_jms, "transparent_2_sided", text='')
                row = col.row()
                row.label(text='Render Only:')
                row.prop(material_ass_jms, "render_only", text='')
                row = col.row()
                row.label(text='Collision Only:')
                row.prop(material_ass_jms, "collision_only", text='')
                row = col.row()
                row.label(text='Sphere Collision Only:')
                row.prop(material_ass_jms, "sphere_collision_only", text='')
                row = col.row()
                row.label(text='Fog Plane:')
                row.prop(material_ass_jms, "fog_plane", text='')
                row = col.row()
                row.label(text='Ladder:')
                row.prop(material_ass_jms, "ladder", text='')
                row = col.row()
                row.label(text='Breakable:')
                row.prop(material_ass_jms, "breakable", text='')
                row = col.row()
                row.label(text='AI Deafening:')
                row.prop(material_ass_jms, "ai_deafening", text='')
                row = col.row()
                row.label(text='No Shadow:')
                row.prop(material_ass_jms, "no_shadow", text='')
                row = col.row()
                row.label(text='Shadow Only:')
                row.prop(material_ass_jms, "shadow_only", text='')
                col = box.column()
                row = col.row()
                row.label(text='Lightmap Only:')
                row.prop(material_ass_jms, "lightmap_only", text='')
                row = col.row()
                row.label(text='Precise:')
                row.prop(material_ass_jms, "precise", text='')
                row = col.row()
                row.label(text='Conveyor:')
                row.prop(material_ass_jms, "conveyor", text='')
                row = col.row()
                row.label(text='Portal (One-Way):')
                row.prop(material_ass_jms, "portal_1_way", text='')
                row = col.row()
                row.label(text='Portal (Door):')
                row.prop(material_ass_jms, "portal_door", text='')
                row = col.row()
                row.label(text='Portal (Vis Blocker):')
                row.prop(material_ass_jms, "portal_vis_blocker", text='')
                row = col.row()
                row.label(text='Dislikes Photons:')
                row.prop(material_ass_jms, "dislike_photons", text='')
                row = col.row()
                row.label(text='Ignored by Lightmapper:')
                row.prop(material_ass_jms, "ignored_by_lightmaps", text='')
                row = col.row()
                row.label(text='Portal (Sound Blocker):')
                row.prop(material_ass_jms, "blocks_sound", text='')
                row = col.row()
                row.label(text='Decal Offset:')
                row.prop(material_ass_jms, "decal_offset", text='')

            if scene_halo.game_version == 'halo3':
                row = col.row()
                row.label(text='Two-sided:')
                row.prop(material_ass_jms, "two_sided", text='')
                row = col.row()
                row.label(text='One-sided Transparent:')
                row.prop(material_ass_jms, "transparent_1_sided", text='')
                row = col.row()
                row.label(text='Two-sided Transparent:')
                row.prop(material_ass_jms, "transparent_2_sided", text='')
                row = col.row()
                row.label(text='Render Only:')
                row.prop(material_ass_jms, "render_only", text='')
                row = col.row()
                row.label(text='Collision Only:')
                row.prop(material_ass_jms, "collision_only", text='')
                row = col.row()
                row.label(text='Sphere Collision Only:')
                row.prop(material_ass_jms, "sphere_collision_only", text='')
                row = col.row()
                row.label(text='Fog Plane:')
                row.prop(material_ass_jms, "fog_plane", text='')
                row = col.row()
                row.label(text='Ladder:')
                row.prop(material_ass_jms, "ladder", text='')
                row = col.row()
                row.label(text='Breakable:')
                row.prop(material_ass_jms, "breakable", text='')
                row = col.row()
                row.label(text='AI Deafening:')
                row.prop(material_ass_jms, "ai_deafening", text='')
                row = col.row()
                row.label(text='No Shadow:')
                row.prop(material_ass_jms, "no_shadow", text='')
                row = col.row()
                row.label(text='Shadow Only:')
                row.prop(material_ass_jms, "shadow_only", text='')
                col = box.column()
                row = col.row()
                row.label(text='Lightmap Only:')
                row.prop(material_ass_jms, "lightmap_only", text='')
                row = col.row()
                row.label(text='Precise:')
                row.prop(material_ass_jms, "precise", text='')
                row = col.row()
                row.label(text='Conveyor:')
                row.prop(material_ass_jms, "conveyor", text='')
                row = col.row()
                row.label(text='Portal (One-Way):')
                row.prop(material_ass_jms, "portal_1_way", text='')
                row = col.row()
                row.label(text='Portal (Door):')
                row.prop(material_ass_jms, "portal_door", text='')
                row = col.row()
                row.label(text='Portal (Vis Blocker):')
                row.prop(material_ass_jms, "portal_vis_blocker", text='')
                row = col.row()
                row.label(text='Ignored by Lightmapper:')
                row.prop(material_ass_jms, "ignored_by_lightmaps", text='')
                row = col.row()
                row.label(text='Portal (Sound Blocker):')
                row.prop(material_ass_jms, "blocks_sound", text='')
                row = col.row()
                row.label(text='Decal Offset:')
                row.prop(material_ass_jms, "decal_offset", text='')
                row = col.row()
                row.label(text='Slip Surface:')
                row.prop(material_ass_jms, "slip_surface", text='')

class ASS_JMS_MaterialLightmapProps(Panel):
    bl_label = "Lightmap Resolution Properties"
    bl_idname = "ASS_JMS_PT_MaterialLightmapPanel"
    bl_space_type = 'PROPERTIES'
    bl_region_type = 'WINDOW'
    bl_context = "material"
    bl_options = {'DEFAULT_CLOSED'}
    bl_parent_id = "ASS_JMS_PT_MaterialPanel"

    @classmethod
    def poll(self, context):
        scene = context.scene
        scene_halo = scene.halo
        if scene_halo.game_version == 'halo2' or scene_halo.game_version == 'halo3':
            return True

    def draw(self, context):
        layout = self.layout
        current_material = context.object.active_material
        scene = context.scene
        scene_halo = scene.halo
        if current_material is not None:
            material_ass_jms = current_material.ass_jms
            layout.enabled = material_ass_jms.is_bm
            if scene_halo.game_version == 'halo2':
                col = layout.column(align=True)
                row = col.row()
                row.label(text='Lightmap Resolution Scale:')
                row.prop(material_ass_jms, "lightmap_resolution_scale", text='')
                row = col.row()
                row.label(text='Lightmap Power Scale:')
                row.prop(material_ass_jms, "lightmap_power_scale", text='')
                row = col.row()
                row.label(text='Lightmap Half-Life Scale:')
                row.prop(material_ass_jms, "lightmap_half_life", text='')
                row = col.row()
                row.label(text='Lightmap Diffuse Scale:')
                row.prop(material_ass_jms, "lightmap_diffuse_scale", text='')

            else:
                col_split = layout.column(align=True).split()
                col = layout.column(align=True)
                col_split_b = layout.column(align=True).split()
                col_b = layout.column(align=True)
                row = col_split.row()
                row.label(text='Override Lightmap Transparency:')
                row.prop(material_ass_jms, "override_lightmap_transparency", text='')
                row = col_split.row()
                row.label(text='Ignore Default Resolution Scale:')
                row.prop(material_ass_jms, "ignore_default_res_scale", text='')
                row = col.row()
                row.label(text='Two-sided Transparent Tint:')
                row.prop(material_ass_jms, "two_sided_transparent_tint", text='')
                row = col.row()
                row.label(text='Additive Transparency:')
                row.prop(material_ass_jms, "additive_transparency", text='')
                row = col_split_b.row()
                row.label(text='Lightmap Resolution:')
                row.prop(material_ass_jms, "lightmap_res", text='')
                row = col_split_b.row()
                row.label(text='Photon Fidelity:')
                row.prop(material_ass_jms, "photon_fidelity", text='')
                row = col_b.row()
                row.label(text='Use Shader Gel:')
                row.prop(material_ass_jms, "use_shader_gel", text='')

class ASS_JMS_MaterialBasicProps(Panel):
    bl_label = "Lightmap Properties"
    bl_idname = "ASS_JMS_PT_MaterialBasicPanel"
    bl_space_type = 'PROPERTIES'
    bl_region_type = 'WINDOW'
    bl_context = "material"
    bl_options = {'DEFAULT_CLOSED'}
    bl_parent_id = "ASS_JMS_PT_MaterialPanel"

    @classmethod
    def poll(self, context):
        scene = context.scene
        scene_halo = scene.halo

        if scene_halo.game_version == 'halo3':
            return True

    def draw(self, context):
        layout = self.layout
        current_material = context.object.active_material
        if current_material is not None:
            material_ass_jms = current_material.ass_jms
            layout.enabled = material_ass_jms.is_bm
            is_enabled = True
            if material_ass_jms.power <= 0.0:
                is_enabled = False
            col = layout.column(align=True)
            row = col.row()
            row.label(text='Power:')
            row.prop(material_ass_jms, "power", text='')
            row = col.row()
            row.enabled = is_enabled
            row.label(text='Color:')
            row.prop(material_ass_jms, "color", text='')
            row = col.row()
            row.enabled = is_enabled
            row.label(text='Quality:')
            row.prop(material_ass_jms, "quality", text='')
            row = col.row()
            row.enabled = is_enabled
            row.label(text='Power Per Unit Area:')
            row.prop(material_ass_jms, "power_per_unit_area", text='')
            row = col.row()
            row.enabled = is_enabled
            row.label(text='Emissive Focus:')
            row.prop(material_ass_jms, "emissive_focus", text='')

class ASS_JMS_MaterialAttenuationProps(Panel):
    bl_label = "Attenuation"
    bl_idname = "ASS_JMS_PT_MaterialAttenuationPanel"
    bl_space_type = 'PROPERTIES'
    bl_region_type = 'WINDOW'
    bl_context = "material"
    bl_options = {'DEFAULT_CLOSED'}
    bl_parent_id = "ASS_JMS_PT_MaterialBasicPanel"

    def draw_header(self, context):
        current_material = context.object.active_material
        if current_material is not None:
            material_ass_jms = current_material.ass_jms
            if material_ass_jms.power <= 0.0 or not material_ass_jms.is_bm:
                self.layout.enabled = False

            self.layout.prop(material_ass_jms, "attenuation_enabled", text='')

    def draw(self, context):
        layout = self.layout
        current_material = context.object.active_material
        if current_material is not None:
            material_ass_jms = current_material.ass_jms
            if material_ass_jms.power <= 0.0 or not material_ass_jms.is_bm or not material_ass_jms.attenuation_enabled:
                layout.enabled = False

            col = layout.column(align=True)
            row = col.row()
            row.label(text='Falloff Distance:')
            row.prop(material_ass_jms, "falloff_distance", text='')
            row = col.row()
            row.label(text='Cutoff Distance:')
            row.prop(material_ass_jms, "cutoff_distance", text='')

class ASS_JMS_MaterialFrustumProps(Panel):
    bl_label = "Frustum"
    bl_idname = "ASS_JMS_PT_MaterialFrustumPanel"
    bl_space_type = 'PROPERTIES'
    bl_region_type = 'WINDOW'
    bl_context = "material"
    bl_options = {'DEFAULT_CLOSED'}
    bl_parent_id = "ASS_JMS_PT_MaterialBasicPanel"

    def draw(self, context):
        layout = self.layout
        current_material = context.object.active_material
        if current_material is not None:
            material_ass_jms = current_material.ass_jms
            layout.enabled = material_ass_jms.is_bm
            if material_ass_jms.power <= 0.0:
                layout.enabled = False

            col = layout.column(align=True)
            row = col.row()
            row.label(text='Blend:')
            row.prop(material_ass_jms, "frustum_blend", text='')
            row = col.row()
            row.label(text='Falloff:')
            row.prop(material_ass_jms, "frustum_falloff", text='')
            row = col.row()
            row.label(text='Cutoff:')
            row.prop(material_ass_jms, "frustum_cutoff", text='')

class ASS_JMS_MaterialPropertiesGroup(PropertyGroup):
    material_effect: StringProperty(
        name = "Material Effect",
        description = "Set material effect name",
        default = "",
        )

    two_sided: BoolProperty(
        name ="Two-sided",
        description = "This flag or shader symbol when applied to a material that is applied to a face or surface renders both sides of the surface instead of just the side that the normal is facing",
        default = False,
        )

    transparent_1_sided: BoolProperty(
        name ="One-sided Transparent",
        description = "One-sided but non-manifold collidable geometry",
        default = False,
        )

    transparent_2_sided: BoolProperty(
        name ="Two-sided Transparent",
        description = "Two-sided collidable geometry that is not connected to or touching one-sided geometry",
        default = False,
        )

    render_only: BoolProperty(
        name ="Render Only",
        description = "Non-collidable, Non-solid geometry",
        default = False,
        )

    collision_only: BoolProperty(
        name ="Collision Only",
        description = "Non-rendered geometry",
        default = False,
        )

    sphere_collision_only: BoolProperty(
        name ="Sphere Collision Only",
        description = "Non-rendered geometry that ray tests pass through but spheres (bipeds and vehicles) will not",
        default = False,
        )

    fog_plane: BoolProperty(
        name ="Fog Plane",
        description = "Non-collidable fog plane. This shader symbol when applied to a material that is applied to a face or surface makes the surface not be rendered. The faces acts as a fog plane that can be used to define a volumetric fog region",
        default = False,
        )

    ladder: BoolProperty(
        name ="Ladder",
        description = "Climbable geometry. This flag or shader symbol when applied to a material that is applied to a face or surface sets the surface up to act as a ladder for the player",
        default = False,
        )

    breakable: BoolProperty(
        name ="Breakable",
        description = "Two-sided breakable geometry",
        default = False,
        )

    ai_deafening: BoolProperty(
        name ="AI Deafening",
        description = "A portal that does not propagate sound. This property does not apply to multiplayer levels",
        default = False,
        )

    no_shadow: BoolProperty(
        name ="No Shadow",
        description = "Does not cast real time shadows",
        default = False,
        )

    shadow_only: BoolProperty(
        name ="Shadow Only",
        description = "Casts real time shadows but is not visible",
        default = False,
        )

    lightmap_only: BoolProperty(
        name ="Lightmap Only",
        description = "Emits light in the light mapper but is otherwise non-existent (non-collidable and non-rendered)",
        default = False,
        )

    precise: BoolProperty(
        name ="Precise",
        description = "Points and triangles are precise and will not be fiddled with in the BSP pass",
        default = False,
        )

    conveyor: BoolProperty(
        name ="Conveyor",
        description = "Geometry which will have a surface coordinate system and velocity",
        default = False,
        )

    portal_1_way: BoolProperty(
        name ="Portal (One-Way)",
        description = "Portal can only be seen through in a single direction",
        default = False,
        )

    portal_door: BoolProperty(
        name ="Portal (Door)",
        description = "Portal visibility is attached to a device machine state",
        default = False,
        )

    portal_vis_blocker: BoolProperty(
        name ="Portal (Vis Blocker)",
        description = "Portal visibility is completely blocked by this portal",
        default = False,
        )

    portal_exact: BoolProperty(
        name ="Portal (Exact Portal)",
        description = "Exact Portal property. This flag or shader symbol when applied to a material that is applied to a face or surface makes the surface able to be used to define an exact portal",
        default = False,
        )

    dislike_photons: BoolProperty(
        name ="Dislikes Photons",
        description = "Photons from sky/sun quads will ignore these materials",
        default = False,
        )

    ignored_by_lightmaps: BoolProperty(
        name ="Dislikes Photons",
        description = "Lightmapper will not add this geometry to it's raytracing scene representation",
        default = False,
        )

    blocks_sound: BoolProperty(
        name ="Portal (Sound Blocker)",
        description = "Portal that does not propagate any sound",
        default = False,
        )

    decal_offset: BoolProperty(
        name ="Decal Offset",
        description = "Offsets the faces that this material is applied to as it would normally for a decal",
        default = False,
        )

    slip_surface: BoolProperty(
        name ="Blocks Sound",
        description = "Offsets the faces that this material is applied to as it would normally for a decal",
        default = False,
        )

    water_surface: BoolProperty(
        name ="Water Surface",
        description = "This flag or shader symbol when applied to a material that is applied to a face or surface marks that surface as a water surface",
        default = False,
        )

    group_transparents_by_plane: BoolProperty(
        name ="Group Transparents by Plane",
        description = "Group the transparent geometry by fitted planes",
        default = False,
        )

    override_lightmap_transparency: BoolProperty(
        name ="Override Lightmap Transparency",
        description = "This flag or shader symbol when applied to a material that is applied to a face or surface overrides the lightmap transparency for that surface",
        default = False,
        )

    ignore_default_res_scale: BoolProperty(
        name ="Ignore Default Resolution Scale",
        description = "This flag or shader symbol when applied to a material that is applied to a face or surface overrides the default lightmap resolution for that surface",
        default = False,
        )

    use_shader_gel: BoolProperty(
        name ="Use Shader Gel",
        description = "I have no idea what this is",
        default = False,
        )

    lightmap_res: FloatProperty(
        name = "Lightmap Resolution",
        description = "Lightmap resolution scale for the material",
        default = 1.0,
        max = 50000.0,
        min = 0.001,
        )

    photon_fidelity: IntProperty(
        name = "Photon Fidelity",
        description = "I have no idea what this is",
        default = 1,
        max = 3,
        min = 0,
        )

    two_sided_transparent_tint: FloatVectorProperty(
        name = "Two-sided Transparent Tint",
        description = "Tint for two-sided transparent meshes",
        subtype = 'COLOR',
        default = (0.0, 0.0, 0.0),
        max = 1.0,
        min = 0.0,
        )

    additive_transparency: FloatVectorProperty(
        name = "Additive Transparency",
        description = "I have no idea what this is",
        subtype = 'COLOR',
        default = (0.0, 0.0, 0.0),
        max = 1.0,
        min = 0.0,
        )

    power: FloatProperty(
        name = "Power",
        description = "Lightmap power for the material",
        default = 0.0,
        max = 1000.0,
        min = 0,
        )

    color: FloatVectorProperty(
        name = "Color",
        description = "Color of the light emitted by the material",
        subtype = 'COLOR',
        default = (1.0, 1.0, 1.0),
        max = 1.0,
        min = 0.0,
        )

    quality: FloatProperty(
        name = "Quality",
        description = "Lightmap quality for the material",
        default = 1.0,
        max = 1000.0,
        min = 0.1,
        )

    power_per_unit_area: BoolProperty(
        name ="Power Per Unit Area",
        description = "I have no idea what this is",
        default = False,
        )

    emissive_focus: FloatProperty(
        name = "Emissive Focus",
        description = "I have no idea what this is",
        default = 0.0,
        max = 1.0,
        min = 0.0,
        )

    attenuation_enabled: BoolProperty(
        name ="Attenuation Enabled",
        description = "I have no idea what this is",
        default = False,
        )

    falloff_distance: FloatProperty(
        name = "Falloff Distance",
        description = "I have no idea what this is",
        default = 1000.0,
        max = 100000.0,
        min = 0.0,
        )

    cutoff_distance: FloatProperty(
        name = "Cutoff Distance",
        description = "I have no idea what this is",
        default = 2000.0,
        max = 100000.0,
        min = 0.0,
        )

    frustum_blend: FloatProperty(
        name = "Frustum Blend",
        description = "I have no idea what this is",
        default = 0.0,
        max = 1.0,
        min = 0.0,
        )

    frustum_falloff: FloatProperty(
        name = "Frustum Falloff",
        description = "I have no idea what this is",
        default = 25.0,
        max = 170.0,
        min = 2.0,
        )

    frustum_cutoff: FloatProperty(
        name = "Frustum Cutoff",
        description = "I have no idea what this is",
        default = 45.0,
        max = 170.0,
        min = 2.0,
        )

    is_bm: BoolProperty(
        name = "Halo Material Enabled",
        description = "Enable material flags and settings",
        default = False,
        )

    lightmap_resolution_scale: FloatProperty(
        name = "Lightmap Resolution Scale",
        description = "Lightmap resolution scale for the material",
        default = 0.0,
        min = 0.0,
        )

    lightmap_power_scale: FloatProperty(
        name = "Lightmap Power Scale",
        description = "Lightmap power scale for the material",
        default = 0.0,
        min = 0.0,
        )

    lightmap_half_life: FloatProperty(
        name = "Lightmap Half-Life",
        description = "Lightmap half-Life for the material",
        default = 0.0,
        min = 0.0,
        )

    lightmap_diffuse_scale: FloatProperty(
        name = "Lightmap Diffuse Scale",
        description = "Lightmap diffuse scale for the material",
        default = 0.0,
        min = 0.0,
        )

class Halo_MeshProps(Panel):
    bl_label = "Halo Mesh Properties"
    bl_idname = "HALO_PT_MeshDetailsPanel"
    bl_space_type = "PROPERTIES"
    bl_region_type = "WINDOW"
    bl_context = "data"
    bl_options = {"DEFAULT_CLOSED"}

    @classmethod
    def poll(cls, context):
        scene = context.scene
        scene_halo = scene.halo

        obj = context.object
        mesh = obj.data

        show_panel = None
        if hasattr(obj, 'marker') and obj.name[0:1].lower() == '#' or hasattr(mesh, 'ass_jms') and not scene_halo.game_version == 'haloce' or hasattr(obj, 'jmi') and obj.name[0:1].lower() == '!' and scene_halo.game_version == 'haloce':
            show_panel = True

        return show_panel

    def draw(self, context):
        layout = self.layout

class ASS_JMS_MeshProps(Panel):
    bl_label = "ASS/JMS Properties"
    bl_idname = "ASS_JMS_PT_DetailsPanel"
    bl_space_type = "PROPERTIES"
    bl_region_type = "WINDOW"
    bl_context = "data"
    bl_options = {"DEFAULT_CLOSED"}
    bl_parent_id = "HALO_PT_MeshDetailsPanel"

    @classmethod
    def poll(self, context):
        scene = context.scene
        scene_halo = scene.halo

        mesh = context.object.data

        ass_jms = None
        if hasattr(mesh, 'ass_jms') and not scene_halo.game_version == 'haloce':
            ass_jms = mesh.ass_jms

        return ass_jms

    def draw(self, context):
        layout = self.layout

        mesh = context.object.data
        mesh_ass_jms = mesh.ass_jms

        col = layout.column(align=True)
        row = col.row()
        row.label(text='Bounding Radius:')
        row.prop(mesh_ass_jms, "bounding_radius", text='')
        row = col.row()
        row.label(text='LOD:')
        row.prop(mesh_ass_jms, "level_of_detail", text='')
        row = col.row()
        row.label(text='Object Type:')
        row.prop(mesh_ass_jms, "Object_Type", text='')
        row = col.row()
        row.label(text='XREF Path:')
        row.prop(mesh_ass_jms, "XREF_path", text='')

class ASS_JMS_MeshPropertiesGroup(PropertyGroup):
    bounding_radius: BoolProperty(
        name ="Bounding Radius",
        description = "Sets object as a bounding radius",
        default = False,
        )

    level_of_detail: EnumProperty(
        name="LOD:",
        description="What LOD to use for the object",
        items=[ ('0', "NONE", "No level of detail set"),
                ('1', "L1", "Super Low"),
                ('2', "L2", "Low"),
                ('3', "L3", "Medium"),
                ('4', "L4", "High"),
                ('5', "L5", "Super High"),
                ('6', "L6", "Hollywood"),
               ]
        )

    Object_Type : EnumProperty(
        name="Object Type",
        description="Select object type to write mesh as",
        default = "CONVEX SHAPES",
        items=[ ('SPHERE', "Sphere", "Sphere"),
                ('BOX', "Box", "Box"),
                ('CAPSULES', "Pill", "Pill/Capsule"),
                ('CONVEX SHAPES', "Convex Shape", "Convex Shape/Mesh"),
               ]
        )

    XREF_path: StringProperty(
        name="XREF Object",
        description="Select a path to a model file",
        subtype="FILE_PATH"
    )

class Halo_SceneProps(Panel):
    bl_label = "Halo Scene Properties"
    bl_idname = "HALO_PT_GameVersionPanel"
    bl_space_type = 'PROPERTIES'
    bl_region_type = 'WINDOW'
    bl_context = "scene"
    bl_options = {'DEFAULT_CLOSED'}
    def draw(self, context):
        scene = context.scene
        scene_halo = scene.halo

        layout = self.layout

        box = layout.box()
        box.label(text="Game Version:")
        col = box.column(align=True)
        row = col.row()
        row.prop(scene_halo, "game_version", text='')
        box = layout.box()
        box.label(text="Export Settings:")
        col = box.column(align=True)
        row = col.row()
        row.label(text='Expert Mode:')
        row.prop(scene_halo, "expert_mode", text='')

class Halo_ScenePropertiesGroup(PropertyGroup):
    game_version: EnumProperty(
        name="Game:",
        description="What game will you be exporting for",
        items=[ ('haloce', "Halo CE", "Show properties for Halo Custom Edition Or Halo CE MCC"),
                ('halo2', "Halo 2", "Show properties for Halo 2 Vista or Halo 2 MCC"),
                ('halo3', "Halo 3", "Show properties for Halo 3 MCC"),
               ]
        )

    expert_mode: BoolProperty(
        name ="Expert Mode",
        description = "Reveal hidden options. If you're not a developer or know what you're doing then you probably shouldn't be messing with this.",
        default = False,
        )

classeshalo = (
    ASS_JMS_MeshPropertiesGroup,
    ASS_JMS_MaterialPropertiesGroup,
    Halo_MeshProps,
    ASS_JMS_MeshProps,
    ASS_JMS_MaterialProps,
    ASS_JMS_MaterialFlagsProps,
    ASS_JMS_MaterialLightmapProps,
    ASS_JMS_MaterialBasicProps,
    ASS_JMS_MaterialAttenuationProps,
    ASS_JMS_MaterialFrustumProps,
    Halo_ScenePropertiesGroup,
    Halo_SceneProps,
)

def register():
    for clshalo in classeshalo:
        bpy.utils.register_class(clshalo)

    bpy.types.Mesh.ass_jms = PointerProperty(type=ASS_JMS_MeshPropertiesGroup, name="ASS/JMS Properties", description="Set properties for your mesh")
    bpy.types.Material.ass_jms = PointerProperty(type=ASS_JMS_MaterialPropertiesGroup, name="ASS/JMS Properties", description="Set properties for your materials")
    bpy.types.Scene.halo = PointerProperty(type=Halo_ScenePropertiesGroup, name="Halo Scene Properties", description="Set properties for your scene")

def unregister():
    del bpy.types.Mesh.ass_jms
    del bpy.types.Material.ass_jms
    del bpy.types.Scene.halo
    for clshalo in classeshalo:
        bpy.utils.unregister_class(clshalo)

if __name__ == '__main__':
    register()