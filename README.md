# houdini_python_snippets
Various python snippets that I have found useful for use in Houdini Solaris.

### Copy .hip path to clipboard
I usually put this into a shelf button for easy access.
```
path = hou.hipFile.path()
hou.ui.copyTextToClipboard(path)
```

### Set Network Graph Display flag
```
hou.node("/stage/NodeName").setDisplayFlag(True)
```

### isUIAvailable
I put this on the `input` parameter on a Switch node as a python expression. When the Houdini UI is active the switch value is `1` and so anything in that input will be active. Handy for when you want certain nodes to be active locally, and inactive when on the farm.
```
hou.isUIAvailable()
```

### Callback Scripts
```
kwargs["parm_name"]
kwargs["script_multiparm_index"]
```

## Sops

### houdini_renderview_bg.py
Easily find and set the background image for the Mantra RenderView tab in SOPs.

### houdini_pintabs.py
Quickly find and pin several node parameter tabs to specific tab panes

## Lops

### RenderVarEdit
Disable RenderVar objects in the SceneGraph and also within OrderedVars on the RenderProduct. Accepts the usual Houdini Lops primitive matching patterns.

### PerLightObject_RenderVar
Searches prims at the defined source(s) for Arnold light group names and creates a RenderVar per light group.
