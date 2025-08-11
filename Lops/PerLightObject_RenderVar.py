import os
from pxr import Sdf,Usd,Gf

node = hou.pwd()
stage = node.editableStage()
input_node = node.input(0)

sources = ["/lights"]

# Render Var properties
input_name = "specular"
source_name = "C[S].*"
filter_type = "gaussian_filter"
filter_width = 2.0
data_type = "color3f"
format_type = "color3h"
source_type = "lpe"

light_grps = []

# Find arnold light groups
for s in sources:
    start_prim = stage.GetPrimAtPath(s)
    iterator = iter(Usd.PrimRange(start_prim))
    for prim in iterator:
        if prim.GetAttribute("primvars:arnold:aov"):
            light_grps.append(prim.GetAttribute("primvars:arnold:aov").Get(0))

# Remove duplicates
light_grps = list(set(light_grps))

vars_root = "/Render/Products/Vars/"
products_root = "/Render/Products/"

# Create Render Var for each group
for grp in light_grps:
    v = stage.DefinePrim(vars_root+input_name+"_"+grp, "RenderVar")
    filter = v.CreateAttribute("arnold:filter",Sdf.ValueTypeNames.String)
    filter.Set(str(filter_type))
    v.GetAttribute("dataType").Set(str(data_type))
    format = v.CreateAttribute("driver:parameters:aov:format",Sdf.ValueTypeNames.String)
    format.Set(str(format_type))
    name = v.CreateAttribute("driver:parameters:aov:name",Sdf.ValueTypeNames.String)
    name.Set(input_name+"_"+grp)
    v.GetAttribute("sourceName").Set(source_name.replace(".*","<L."+grp+">.*"))
    v.GetAttribute("sourceType").Set(str(source_type))
