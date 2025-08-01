node = hou.pwd()
stage = node.editableStage()

# Get prims from parms
remove_selection = hou.LopSelectionRule(pattern=node.evalParm("remove"))
remove_prims = remove_selection.expandedPaths(stage=stage)
keep_selection = hou.LopSelectionRule(pattern=node.evalParm("keep"))
keep_prims = keep_selection.expandedPaths(stage=stage)

# Get vars
rendersettings = stage.GetPrimAtPath("/Render/rendersettings")
vars = rendersettings.GetRelationship("products").GetTargets()
product = stage.GetPrimAtPath(vars[0])
orderedVars = product.GetRelationship("orderedVars").GetTargets()

# Remove and keep defined vars
for var in orderedVars:
    if var in remove_prims and var not in keep_prims:
        product.GetRelationship("orderedVars").RemoveTarget(var)
        stage.GetPrimAtPath(var).SetActive(False)
        
# Add in any missing vars to orderedVars on render product
renderVars = hou.LopSelectionRule(pattern="/Render/Products/Vars/** & %type:RenderVar & {usd_isactive(0, @primpath)}")
renderVars = renderVars.expandedPaths(stage=stage)
missingVars = [x for x in renderVars if x not in keep_prims]

if len(missingVars) > 0:
    for var in missingVars:
        product.GetRelationship("orderedVars").AddTarget(var)
