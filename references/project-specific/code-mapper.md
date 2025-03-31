# Project structure
## Processing
### Repo Control
summary
- the url is hashed as a key to repos
- repos are stored directly in the project folder 

plan
- database?

3.30
- the url is hashed as a key to repos
- repos are stored directly in the project folder 

### Code Analyzer
summary
- llm analyzes readme and find the entry file
- entry functions: entry file is parsed with ast and all of its function names and codes are returned
- function snapshot: each function is analzed by llm to create a short summary text and detailed description
- function workflow: 

workflow
- only look at function calls first
- 

plan
- under the repo the output at each analyzer step should also be stored
- the ast should also give all variables and function calls inside functions 

3.30
- llm analyzes readme and find the entry file
- entry file is parsed with ast and all of its function names and codes are stored
- each function is analzed by llm to create a short summary text and detailed description

## Presentation





# 
## Sample Questions
- how does rgb convert to sh
- what is the structure and vars of cam_transforms sh_utils->RGB2SH
- how is time incorporated to model 
    - render->viewpoint_camera.time->pc._deformation(...,time), FourDGSdataset uses
```py
Camera(colmap_id=index,R=R,T=T,FoVx=FovX,FoVy=FovY,image=image,gt_alpha_mask=None,
       image_name=f"{index}",uid=index,data_device=torch.device("cuda"),time=time,
       mask=mask) 
CameraInfo(uid=uid, R=R, T=T, FovY=FovY, FovX=FovX, image=image,
    image_path=image_path, image_name=image_name, width=width,height=height,
    time = float(idx/len(cam_extrinsics)), mask=None)
```