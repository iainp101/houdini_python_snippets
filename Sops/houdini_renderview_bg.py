import hou,os,OpenImageIO

if hou.hipFile != None:
    start_dir = "/".join(hou.hipFile.path().split("/")[:7])
else:
    start_dir = None

file_select = hou.ui.selectFile(
                start_directory=start_dir,
                title="Render View Background Image",
                collapse_sequences=True,
                file_type=hou.fileType.Image,
                multiple_select=True,
                chooser_mode=hou.fileChooserMode.Read,
                width=0,
                height=0)
                
print(file_select)
if file_select != "":
    hou.hscript("imgdispopt -f %s" % str(file_select))
    
    # Get and set resolution
    dir = "/".join(file_select.split("/")[:-1])
    for f in os.listdir(dir):
        if f.endswith(".exr"):
            exr = dir + "/" + f
            continue
    
    try:
        img = OpenImageIO.ImageInput.open(exr)
        resx = str(img.spec().width)#int(res[0]))
        resy = str(img.spec().height)#int(res[1]))
        hou.hscript("imgdispopt -s on -r %s" % str(resx+' '+resy))
    except:
        pass
