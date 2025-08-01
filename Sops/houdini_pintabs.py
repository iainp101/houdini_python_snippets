panes = hou.ui.panes()
current_selection = hou.selectedNodes()
nodes_to_tabs = ["RenderPanel", "RenderManager", "PassManager", "RenderPreview", "MultiShot"]
tab_names = []
tab_anchor = "SceneView"
stage = "/obj/"

# Check if in Sops or Lops
for p in panes:
    tabs = p.tabs()
    for t in tabs:
        if "NetworkEditor" in t.type().name():
            network_context = t.pwd().childTypeCategory().name()
            if network_context == "Lop":
                tab_anchor = "RenderGallery"
                stage = "/stage/"
            elif network_context == "Sop":
                tab_anchor = "SceneView"
                stage = "/obj/"

# Get existing tabs
for p in panes:
    tabs = p.tabs()
    for t in tabs:
        if tab_anchor in t.type().name():
            for t in tabs:
                tab_names.append(t.name())
        else:
            break

# Add and pin any missing tabs
for p in panes:
    tabs = p.tabs()
    for t in tabs:
        if tab_anchor in t.type().name():
            for n in nodes_to_tabs:
                if n not in tab_names:
                    if hou.node(stage+n):
                        hou.node(stage+n).setCurrent(True, clear_all_selected=True)
                        pt = p.createTab(hou.paneTabType.Parm)
                        pt.setName(n)
                        pt.setPin(True)
        else:
            break
