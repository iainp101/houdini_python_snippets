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

### houdini_renderview_bg.py
Easily find and set the background image for the Mantra RenderView tab in SOPs.

Frustratingly, an image sequence isn't initially accepted and just the current frame is set, even if an image sequence is used. Workaround at the moment is to press 'D' when the cursor is over the pane, and re-select the image sequence.
