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

from xml.dom import minidom
from .format import CameraTrackAsset
from ....global_functions import tag_format

XML_OUTPUT = False

def initilize_camera_track(CAMERATRACK):
    CAMERATRACK.control_points = []

def read_camera_track_body_v0(CAMERATRACK, TAG, input_stream, tag_node, XML_OUTPUT):
    CAMERATRACK.body_header = TAG.TagBlockHeader().read(input_stream, TAG)
    input_stream.read(4) # Padding?
    CAMERATRACK.control_points_tag_block = TAG.TagBlock().read(input_stream, TAG, tag_format.XMLData(tag_node, "control points"))
    input_stream.read(32) # Padding?

def read_control_points_v0(CAMERATRACK, TAG, input_stream, tag_node, XML_OUTPUT):
    if CAMERATRACK.control_points_tag_block.count > 0:
        control_point_node = tag_format.get_xml_node(XML_OUTPUT, CAMERATRACK.control_points_tag_block.count, tag_node, "name", "control points")
        CAMERATRACK.control_points_header = TAG.TagBlockHeader().read(input_stream, TAG)
        for control_point_idx in range(CAMERATRACK.control_points_tag_block.count):
            control_point_element_node = None
            if XML_OUTPUT:
                control_point_element_node = TAG.xml_doc.createElement('element')
                control_point_element_node.setAttribute('index', str(control_point_idx))
                control_point_node.appendChild(control_point_element_node)

            control_point = CAMERATRACK.ControlPoint()
            control_point.position = TAG.read_point_3d(input_stream, TAG,  tag_format.XMLData(control_point_element_node, "position")) * 560
            control_point.orientation = TAG.read_quaternion(input_stream, TAG,  tag_format.XMLData(control_point_element_node, "orientation"), True)
            input_stream.read(32) # Padding?

            CAMERATRACK.control_points.append(control_point)

def read_camera_track_body_retail(CAMERATRACK, TAG, input_stream, tag_node, XML_OUTPUT):
    CAMERATRACK.body_header = TAG.TagBlockHeader().read(input_stream, TAG)
    input_stream.read(4) # Padding?
    CAMERATRACK.control_points_tag_block = TAG.TagBlock().read(input_stream, TAG, tag_format.XMLData(tag_node, "control points"))

def read_control_points_retail(CAMERATRACK, TAG, input_stream, tag_node, XML_OUTPUT):
    if CAMERATRACK.control_points_tag_block.count > 0:
        control_point_node = tag_format.get_xml_node(XML_OUTPUT, CAMERATRACK.control_points_tag_block.count, tag_node, "name", "control points")
        CAMERATRACK.control_points_header = TAG.TagBlockHeader().read(input_stream, TAG)
        for control_point_idx in range(CAMERATRACK.control_points_tag_block.count):
            control_point_element_node = None
            if XML_OUTPUT:
                control_point_element_node = TAG.xml_doc.createElement('element')
                control_point_element_node.setAttribute('index', str(control_point_idx))
                control_point_node.appendChild(control_point_element_node)

            control_point = CAMERATRACK.ControlPoint()
            control_point.position = TAG.read_point_3d(input_stream, TAG,  tag_format.XMLData(control_point_element_node, "position")) * 560
            control_point.orientation = TAG.read_quaternion(input_stream, TAG,  tag_format.XMLData(control_point_element_node, "orientation"), True)

            CAMERATRACK.control_points.append(control_point)

def process_file(input_stream, report):
    TAG = tag_format.TagAsset()
    CAMERATRACK = CameraTrackAsset()
    TAG.is_legacy = False
    TAG.big_endian = False

    if XML_OUTPUT:
        TAG.xml_doc = minidom.Document()

    CAMERATRACK.header = TAG.Header().read(input_stream, TAG)

    tag_node = None
    if XML_OUTPUT:
        tag_node = TAG.xml_doc.childNodes[0]

    initilize_camera_track(CAMERATRACK)
    if CAMERATRACK.header.engine_tag == "LAMB":
        read_camera_track_body_v0(CAMERATRACK, TAG, input_stream, tag_node, XML_OUTPUT)
        read_control_points_v0(CAMERATRACK, TAG, input_stream, tag_node, XML_OUTPUT)

    elif CAMERATRACK.header.engine_tag == "MLAB":
        read_camera_track_body_v0(CAMERATRACK, TAG, input_stream, tag_node, XML_OUTPUT)
        read_control_points_v0(CAMERATRACK, TAG, input_stream, tag_node, XML_OUTPUT)

    elif CAMERATRACK.header.engine_tag == "BLM!":
        read_camera_track_body_retail(CAMERATRACK, TAG, input_stream, tag_node, XML_OUTPUT)
        read_control_points_retail(CAMERATRACK, TAG, input_stream, tag_node, XML_OUTPUT)

    current_position = input_stream.tell()
    EOF = input_stream.seek(0, 2)
    if not EOF - current_position == 0: # is something wrong with the parser?
        report({'WARNING'}, "%s elements left after parse end" % (EOF - current_position))

    if XML_OUTPUT:
        xml_str = TAG.xml_doc.toprettyxml(indent ="\t")

        save_path_file = tag_format.get_xml_path(input_stream.name, CAMERATRACK.header.tag_group, TAG.is_legacy)

        with open(save_path_file, "w") as f:
            f.write(xml_str)

    return CAMERATRACK
