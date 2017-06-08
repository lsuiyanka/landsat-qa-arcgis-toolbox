import os
import sys

# add 'Scripts' dir to tool path
sys.path.append(os.path.join(os.path.dirname(__file__), "Scripts"))

import qa_decode_tool
reload(qa_decode_tool)
from qa_decode_tool import DecodeQA

class Toolbox(object):
    def __init__(self):
        """Define the toolbox (the name of the toolbox is the name of the
        .pyt file)."""
        self.label = "Landsat QA ArcGIS Toolbox"
        self.alias = "Landsat QA ArcGIS Toolbox"

        # List of tool classes associated with this toolbox
        self.tools = [DecodeQA]