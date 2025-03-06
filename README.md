# solaris_python_snippets
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
