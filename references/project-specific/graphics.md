See [reference.md](../../reference.md#graphics)
 

# Summary
always run this first
```
module load cuda/11.8; module load gcc/9.1.0; export CUDA_ROOT=/nas/longleaf/rhel8/apps/cuda/11.8; export CUDA_PATH=/nas/longleaf/rhel8/apps/cuda/11.8; export CPATH="/nas/longleaf/rhel8/apps/cuda/11.8/include"; export TORCH_CUDA_ARCH_LIST="8.9"; export CC=$(which gcc); export CXX=$(which g++); export CUDAHOSTCXX=$(which g++); 
```

# Basics/Review
## SfM
- SIFT
- flann
- RANSAC
- Bundle Adjustment
- multiview stereo (MVS)
    - patch match


## Rendering
### Coordinate transform
1. world (x,y,z,1) to camera through extrinsic matrix [R|t]. ${\mathbf{X}_c = \begin{bmatrix} X_c \\ Y_c \\ Z_c \\ 1 \end{bmatrix}
=
\begin{bmatrix} R ; t \\ 0 ; 1 \end{bmatrix}
\begin{bmatrix} X_w \\ Y_w \\ Z_w \\ 1 \end{bmatrix}}$

2. camera to image through intrinsic matrix K. ${\mathbf{x}_{\text{image}} =
K \cdot
\begin{bmatrix} X_c \\ Y_c \\ Z_c \end{bmatrix}
=
\begin{bmatrix}
f_x  ; 0  ; c_x \\
0  ; f_y  ; c_y \\
0  ; 0  ; 1
\end{bmatrix}
\begin{bmatrix} X_c \\ Y_c \\ Z_c \end{bmatrix}}$

3. image to pixel: $\\{u = \frac{u'}{w'} = \frac{f_x X_c}{Z_c} + c_x}\\{v = \frac{v'}{w'} = \frac{f_y Y_c}{Z_c} + c_y}$

# Dataset
## Colmap
https://colmap.github.io/format.html
### Cameras.bin
```c
# Camera list with one line of data per camera:
#   CAMERA_ID, MODEL, WIDTH, HEIGHT, PARAMS[]
# Number of cameras: 3
(1)CAMERA_ID SIMPLE_PINHOLE (3072 2304)dimension (2559.81)focal length (1536 1152)principal point
2 PINHOLE 3072 2304 2560.56 2560.56 1536 1152
3 SIMPLE_RADIAL 3072 2304 2559.69 1536 1152 -0.0218531
```

### Images.bin
```c
# Image list with two lines of data per image (world to camera):
#   IMAGE_ID, (QW, QX, QY, QZ) quaternion, (TX, TY, TZ) position, CAMERA_ID, NAME
#   POINTS2D[] as (X, Y, POINT3D_ID)
# Number of images: 2, mean observations per image: 2
1 (0.851773 0.0165051 0.503764 -0.142941)quaternion (-0.737434 1.02973 3.74354 1)xyz (1)CAMERA_ID (P1180141.JPG)NAME
(2362.39 248.498 58396) (1784.7 268.254 59027) (1784.7 268.254 -1)
2 0.851773 0.0165051 0.503764 -0.142941 -0.737434 1.02973 3.74354 1 P1180142.JPG
1190.83 663.957 23056 1258.77 640.354 59070
```

### points3D.bin
```c
# 3D point list with one line of data per point:
#   POINT3D_ID, X, Y, Z, R, G, B, ERROR, TRACK[] as (IMAGE_ID, POINT2D_IDX)
# Number of points: 3, mean track length: 3.3334
63390 (1.67241 0.292931 0.609726)XYZ (115 121 122)RGB (1.33927)ERROR [(16 6542) (15 7345) (6 6714) (14 7227)]
63376 2.01848 0.108877 -0.0260841 102 209 250 1.73449 16 6519 15 7322 14 7212 8 3991
63371 1.71102 0.28566 0.53475 245 251 249 0.612829 118 4140 117 4473
```

## Popular
### LLFF
poses_bounds.npy
- camera-to-world, 3 by 5 matrix plus 2 float
- extrinsic: first 3 columns are rotation with axis [down, right, backwards]
- extrinsic: 4th is translation 
- intrinsic: 5th is [height, width, focal]
- this matrix is flattened to concat the close and far depths. [n_imgs 17]

```py
images, depths, masks, poses, bds, render_poses, ref_c2w, motion_coords, bg_masks = load_llff_data(args.datadir,  args.start_frame, args.end_frame, args.factor, target_idx=target_idx, recenter=True, bd_factor=.9, spherify=args.spherify,  final_height=args.final_height)
```

## Dynamics
### D2RF
- scene (~30 images with name {image_id:6}_{left/right})
    - background_mask: jpg black-white 1880x720
    - dpt: npy files of float 360x940
    - flow_i1: npz, fwd and bwd
    - images: jpg 1880x720
    - images_2: jpg 940x360
    - images_bokeh: jpg 1880x720 (focus on a certain depth)
    - motion_masks: jpg black-white 940x360

    - sparse/0 (one camera)
        - cameras.bin: 1: {'model': 2, 'width': 1880, 'height': 720, 'params': (544.2031891338942, 940.0, 360.0)}
        - images.bin: 
        - points3D.bin: 27k points
    - database.db
    - poses_bounds.npy: 62x17 (62 images, 3x5 matrix concat 2 bounds)

### DNeRF
- monocular synthetic (Blender) video
- scene
    - test
    - train (100-150 vector images): r_{id:3}.png
    - val
    - transforms_test.json
    - transforms_train.json
    - transforms_val.json

```c
"camera_angle_x": 0.6911112070083618, // field of view this appears to be the same across datasets and splits
// focal = .5 * W / np.tan(.5 * camera_angle_x)
    "frames": [
        {
            "file_path": "./val/r_006",
            "rotation": 0.3141592653589793, # PI. this does not seem to be used
            "time": 0.31,
            "transform_matrix": [ # 4 by 4 matrix
                ]
            ]
        }
    ]
```

### Dynerf (meta)
- multiview (18 cameras) real video, 10s.

### ENeRF (Zhengjiang)
- multiview (18 cameras) complex motion video.

### Dynamic Scene 
- monocular phone video, very short

### HyperNeRF
- phone video 

### [Dycheck](https://github.com/KAIR-BAIR/dycheck)
- 

### [Nvidia](https://github.com/gaochen315/DynamicNeRF?tab=readme-ov-file)
![](/images/nvidia-dataset.png)

### Iphone
| ![Alt 1](/images/iphone-dataset-1.png) | ![Alt 2](/images/iphone-dataset-2.png) | ![Alt 3](/images/iphone-dataset-3.png) | ![Alt 4](/images/iphone-dataset-4.png) |
|:------------------:|:------------------:|:------------------:|:------------------:|


# Papers
## Summary
### Trajectory Representation
- (per frame) deformation field: MoDGS
- hexplane + MLP: 4DGS
- SE(3) motion bases: SOM
- spline: SplineGS, MoBGS
- polynomial: Gaussian Flow
- fourier/cosine transform: Gaussian Flow, DeBlurf
- per frame per Gaussian translation: Gaussian Marble
- embedded deformation graph: MoSca

### Blur Formulation and Solutions
- object and camera motion induced blur
    - learned blur kernel
    - even exposure time discretization, SE(3) linear interpolation for camera poses during exposure: BAD-NeRF, Dyblurf
- defocus/depth of field blur

## Deblur
### DeblurNeRF
- static, handles image blurriness caused by defocus or motion (note exposure time is not considered)
- ![](/images/deblur-nerf.png)

### D2RF
- dynamic monocular, handles defocus blur caused by depth variation 
![](/images/d2rf.png)


### [Dyblurf (Korean)](https://kaist-viclab.github.io/dyblurf-site/)

### [Dyblurf (China)](https://huiqiang-sun.github.io/dyblurf/)
- even exposure time discretization, SE(3) linear interpolation for camera poses during exposure
- NSFF, dynamic MLP outputs not deformation but discrete cosine transform coefficients

### [Deblur-4dGS](https://deblur4dgs.github.io/)
- Shape of motion core with **continuous camera poses estimation** to predict the exposure time as a learnable parameter
- multiple canonical gaussians at sharpest times
- static camera: interpolation btw estimated exposure start and end with a tiny MLP
- dynamic camera: within the estimated exposure intervals, learn time interval w btw the times for the gaussians
- various reg
- ![](/images/deblur4DGS.png)

### [Bundle Adjusted Deblur (BAD) 4dgs](https://lingzhezhao.github.io/BAD-Gaussians/)

## Dynamic
### !4DGS

### [4D Gaussian Primitive](https://github.com/fudan-zvg/4d-gaussian-splatting)


### [ST-4dGS](https://github.com/wanglids/ST-4DGS)
![](/images/st-4dgs.png)

### [!Gaussian Flow](https://nju-3dv.github.io/projects/Gaussian-Flow/)
- deformation as sum of polynomial and fourier fit, learned time dilation for abrupt changes. ![](/images/gaussian-flow-why-dual-domain.png)
- temporal smoothness and simple rigidity constraint (nearby points have similar flow)


### [!!Shape of Motion]
factorized long range rigid transform
- per frame rigid transformation (SE(3)) for each canonical Gaussian at each time (instead of implicit deformation field)
- use a small set (20) of basis transformations for each time
- jointly learn the set of global motion bases and motion coefficients of each 3D Gaussian.

loss
- depth, color, motion mask
- 2d and lifted 3d motion track
- rigidity loss (distance to nearby gaussians preserved from time to time)



### [!!Gaussian Marbles](https://geometry.stanford.edu/projects/dynamic-gaussian-marbles.github.io/)
- isotropic Gaussian
> ![](/images/gm-why-iso.png)
- per Gaussian per frame translation (3xTx|G|, T is frame number, G is set of Gaussian)
- divide long video to segments and iteratively learn and merge and adjust
- motion mask, 2D tracking, depth prior
- nearby and instance rigidity, and Chamfer priors

### [!MODGS](https://modgs.github.io/)
- per frame, invertible, deformation field (MLP) initialized by depth lifted 2d flow
- noval ordinal depth loss

### [MAGS](https://github.com/jasongzy/MAGS)
- noval flow supervision

### [MoBGS (Korean)]
- handles blur caused by both camera motion and object motion by having latent cameras and calculating per frame exposure time
- spline based dynamics (based on their [SplineGS](https://kaist-viclab.github.io/splinegs-site/))
- ![](/images/MoBGS.png)

### [MoSca]
#### Background on embeded deformation
https://people.inf.ethz.ch/sumnerb/research/embdef/Sumner2007EDF.pdf

#### method
> Although the real-world geometry and appearance are complex and include high-frequency details, the underlying deformation that drives these geometries is usually compact (low-rank) and smooth.
- extend classic Embedded Graphs to connect priors from 2D foundation models to dynamic Gaussian splatting.
- From each track, initialize a MoSca node v(𝑖) using the lifted positions h𝑡 as the translation part and the identity as the rotation, i.e., $Q_t(𝑖) = [I, h_t(𝑖)]$. Then all Qs parametrizes a radial basis function
- as rigid as possible geometry loss

## Feedforward Generative
### [Splatter Iamge](https://github.com/szymanowiczs/splatter-image)
- For each pixel, create a GS purely withthe UNet. xyz means offset from depth at the projected ray so unseen parts can be accounted for by some background GS (See second figure). ![](/images/splatter-img.png)
- ![](/images/splatter-imge-2.png)

### [Pixel Splatt](https://davidcharatan.com/pixelsplat/)

### [Latent Spaltt](https://geometric-rl.mpi-inf.mpg.de/latentsplat/)

### [MVSplat](https://donydchen.github.io/mvsplat/)

### [Dynamic Neural Point Cloud (D-NPC)]
- octree based geometry and multi-res hash based appearance encoding, COLMAP, depth and segmentation prior

## Diffusion Generative
https://zero123.cs.columbia.edu/

## Generative 4D
### [GCD](https://gcd.cs.columbia.edu/)

# Env
## GS
- python 3.9
- mamba
- 4dgs, d2rf pkgs, torch with cuda11.8
- FAILED: colmap with conda cmake
- mamba install conda-forge::colmap
- above are removed

core
- python 3.10
- 4dgs (knn, gs raster)
- torch 2.2.0-cuda11.8

trivial
- nerfstudio  0.3.4
- imageio 2.37.0; imageio-ffmpeg 0.6.0
- gsplat  1.5.0



# Project
## 4DGS

### Code
scene->dataset_reader
- readColmapSceneInfo: needs "images" and "sparse/0"

arguments->init
- all arguments models can be found here grouped to several classes.
- save_iterations 
- checkpoint_iterations

    - Scene
        - scene_info = sceneLoadTypeCallbacks (**world to camera (as colmap)**)
            - readColmapSceneInfo
                - `scene_info = SceneInfo(point_cloud=pcd,
                            train_cameras=train_cam_infos,
                            test_cameras=test_cam_infos,
                            video_cameras=train_cam_infos,
                            maxtime=0, # this might not be used
                            nerf_normalization=getNerfppNorm,
                            ply_path=ply_path)`
                    - ply is conditionally built from storePly() and contains only vertex
                    - pcd:`BasicPointCloud(points=positions, colors=colors, normals=normals)` is from fetchPly (sparse/0/points3D.txt or bin or ply)
                    - note maxtime=0
                    - cam_infos are list of `CameraInfo(uid=idx, R, T, FovY, FovX, image, image_path, image_name, width, height, time, mask)`
            - readNerfSyntheticInfo (also see D-NeRF/load_blender.py)
                - `scene_info = SceneInfo(point_cloud=pcd,
                            train_cameras=train_cam_infos,
                            test_cameras=test_cam_infos,
                            video_cameras=video_cam_infos,
                            nerf_normalization=getNerfppNorm,
                            ply_path=ply_path,
                            maxtime=max_time  # this might not be used
                            )`
                    - if no fused.ply, use 2000 random points
            > time is coded into cam_infos which is list of CameraInfo object and all cam_infos are eventually converted to Camera object through FourDGSdataset
            ```py
            class CameraInfo(NamedTuple):
                uid: int
                R: np.array
                T: np.array
                FovY: np.array
                FovX: np.array
                image: np.array
                image_path: str
                image_name: str
                width: int
                height: int
                time : float
                mask: np.array
            ```
        - the output of scene_info are stored as class variables
        - 
    - scene_reconstruction coarse and fine

### Run
- python train.py -s data/colmap/Camp --port 6017 --expname "colmap/Camp" --configs arguments/d2rf/default.py
- train and save checkpoint: python train.py -s data/colmap/Camp_4dgs_colmap --port 6017 --expname "colmap/Camp" --configs arguments/d2rf/default.py --checkpoint_iterations 10000 
- start with checkpoint: python train.py -s data/dnerf/bouncingballs --port 6017 --expname "dnerf/bouncingballs" --configs arguments/dnerf/bouncingballs.py --start_checkpoint "output/dnerf/bouncingballs/chkpnt_coarse_200.pth" 
    - or end with this for fine stage checkpoint: --start_checkpoint "output/dnerf/bouncingballs/chkpnt_fine_200.pth"
- python render.py --model_path "output/colmap/Camp_4dgs_colmap"  --skip_train --configs arguments/d2rf/default.py 

python train.py -s data/colmap/Camp --port 6017 --expname "colmap/Camp" --configs arguments/d2rf/default.py; python render.py --model_path "output/colmap/Camp"  --skip_train --configs arguments/d2rf/default.py; python train.py -s data/colmap/Mountain --port 6017 --expname "colmap/Mountain" --configs arguments/d2rf/default.py; python render.py --model_path "output/colmap/Mountain"  --skip_train --configs arguments/d2rf/default.py 

### Problem
- ! it seems current training uses both views


## D2RF
### Code
config
- start_frame end_frame are not used


load_llff
- only images_bokeh is used as image data (sorted)
- the downloaded dataset used factor 2 which is default llff factor and images_2 contains downsampled bokeh image
- llff_holdout is  2 which means it's using every second image (left for train, right for test)
- the internal dimensions and return dim is a little different, the final shape for poses is (N_imgs, 3, 5) and for imgs (N_imgs, 360, 940, 3)


## SOM
### Dataset Conversion
SOM requires only a video. 

D2RF
- for high res, first convert to png and resize: `/nas/longleaf/home/zhw/personal/gs/jpgs_to_pngs.sh /nas/longleaf/home/zhw/personal/gs/data/D2RF/Camp/images /nas/longleaf/home/zhw/personal/gs/data/D2RF/Camp/images_small 940 360`
- `/nas/longleaf/home/zhw/personal/gs/create_stereo_videos.sh     /nas/longleaf/home/zhw/personal/gs/data/D2RF/Camp/images_small     /nas/longleaf/home/zhw/personal/gs/data/D2RF_som/high_res/Camp/videos/seq     24` 

### Setup
- git clone --recurse-submodules https://github.com/vye16/shape-of-motion
> note the --recurse-submodules
- since this project requires building custom libraries, you need to set the correct cuda and gcc module. See [gaussian splatt example](../../howto.md#build-gaussian-splatt-cuda-libraries)
- pip install git+https://github.com/nerfstudio-project/gsplat.git
> gsplat requires correct `TORCH_CUDA_ARCH_LIST` variable. See https://en.wikipedia.org/wiki/CUDA#GPUs_supported and find your current GPU architecture. eg, on L40, `export TORCH_CUDA_ARCH_LIST="8.9"`

#### Changes
- made this change https://github.com/vye16/shape-of-motion/issues/69
- and this https://github.com/vye16/shape-of-motion/pull/75/files
- In extract_frames.py     `command = f"ffmpeg -i {video_path} -vf \"select='not(mod(n,{skip_time}))',scale=-1:{height}\" -vsync vfr -ss {start_time} {to_str} {output_dir}/%05d.{ext}"` is replaced by `command = f"ffmpeg -i {video_path} -vf \"fps=24,scale=-1:{height}\" -vsync vfr -ss {start_time} {to_str} {output_dir}/%05d.{ext}"` to avoid FPS sampling that duplicated frames 
- The rendering/eval script (eval_custom.py) is given by Claude in project [som->Loading cameras for custom dataset](https://claude.ai/chat/4c6f401c-6709-4b01-8e5c-e6e29db39f63)
- modified end of preproc/mask_app.py to 
```py
demo.launch(
        server_name="127.0.0.1",
        server_port=8890,
        share=True, # public URL
        allowed_paths=["/nas/longleaf/home/zhw/personal/gs/data/D2RF_som/high_res/Camp", "/nas/longleaf/home/zhw/personal/gs/data/D2RF_som/high_res/Camp/videos"] # all data paths
    )
```

### Dataset
**mask**
![](/images/som-mask.png)
- https://github.com/vye16/shape-of-motion/blob/main/preproc/README.md
- python mask_app.py --root_dir [data_root]
- note that the FPS is fixed, see changes section 
- there might be a Xmem not found error, just move the checkpoint file under checkpoints
- first select a video, end frame set to arbitary high, extract frames
- image directory doesn't matter, change frame index to 1 and click get SAM features
- click the image below to select dynamic objects
- submit mask for tracking
- run `python process_custom.py --img-dirs /nas/longleaf/home/zhw/personal/gs/data/D2RF_som/high_res/Camp/images/** --gpus 0` NO QUOTE on path

**dataset**
```
/nas/longleaf/home/zhw/personal/gs/data/D2RF_som/Camp1
├── aligned_depth_anything
├── bootstapir
├── depth_anything
├── droid_recon.npy
├── flow3d_preprocessed
├── images
├── masks
├── unidepth_disp
├── unidepth_intrins
└── videos
```
- Each folder should have no further sub folder. Note the droid_recon.npy which was from droid_recon folder. 

### Running
**train**
- one sequence/video in data: `python run_training.py --work-dir /nas/longleaf/home/zhw/personal/gs/shape-of-motion/log/Camp/high/left data:custom --data.data-dir /nas/longleaf/home/zhw/personal/gs/data/D2RF_som/high_res/Camp_left --data.camera-type "droid_recon"`
- isotropic gaussian marble: `python run_training.py --work-dir /nas/longleaf/home/zhw/personal/gs/shape-of-motion/log/Camp/high_iso/left --use-isotropic-gaussians data:custom --data.data-dir /nas/longleaf/home/zhw/personal/gs/data/D2RF_som/high_res/Camp_left --data.camera-type "droid_recon"`
- (doesn't work) multiple seq:
```
python run_training.py \
    --work-dir /nas/longleaf/home/zhw/personal/gs/shape-of-motion/log/Camp/high/both \
    --port 6006 \
    data:custom \
    --data.data-dir /nas/longleaf/home/zhw/personal/gs/data/D2RF_som/high_res/Camp/** \
    --data.camera-type "droid_recon"
```

**rendering** 
- https://github.com/vye16/shape-of-motion/issues/22
- Below is to create nerf studio web view
```
python run_rendering.py \
    --work-dir /nas/longleaf/home/zhw/personal/gs/shape-of-motion/log/Camp/high_iso/left \
    --port 6006
```
- The rendering script is given by Claude in project [som->Loading cameras for custom dataset](https://claude.ai/chat/4c6f401c-6709-4b01-8e5c-e6e29db39f63)
    - test: python scripts/eval_custom.py --data_dir /nas/longleaf/home/zhw/personal/gs/data/D2RF_som/high_res/Camp_right --output_dir /nas/longleaf/home/zhw/personal/gs/shape-of-motion/log/Camp/high/right/ --ckpt_path /nas/longleaf/home/zhw/personal/gs/shape-of-motion/log/Camp/high/left/checkpoints/last.ckpt
    - train: python scripts/eval_custom.py --data_dir /nas/longleaf/home/zhw/personal/gs/data/D2RF_som/bokeh/Camp1 --output_dir /nas/longleaf/home/zhw/personal/gs/shape-of-motion/log/Camp1/renders/train --ckpt_path /nas/longleaf/home/zhw/personal/gs/shape-of-motion/log/Camp1/checkpoints/last.ckpt


### Potential Problems
```
torchtyping 0.1.5 requires typeguard<3,>=2.11.1, but you have typeguard 4.4.2 which is incompatible.
nerfstudio 0.3.4 requires viser==0.1.3, but you have viser 0.2.23 which is incompatible.
```

## GM
### Setup
#### Changes
- removed the 10 fps sampling from `ffmpeg -i 10 $video_path "${directory}/rgb/1x/%04d.png` in 00_initialize_directory.sh

### Potential problems
```
ERROR: pip's dependency resolver does not currently take into account all the packages that are installed. This behaviour is the source of the following dependency conflicts.
- geopandas 1.0.1 requires shapely>=2.0.0, but you have shapely 1.8.5.post1 which is incompatible.
- nerfview 0.0.3 requires viser>=0.2.1, but you have viser 0.1.3 which is incompatible.
- unidepth 0.1 requires protobuf==4.25.3, but you have protobuf 3.20.3 which is incompatible.
- nuscenes-devkit 1.1.11 requires Shapely<2.0.0, but you have shapely 2.1.0 which is incompatible.
- tyro 0.9.18 requires typeguard>=4.0.0, but you have typeguard 2.13.3 which is incompatible.
```


### dataset
- https://github.com/coltonstearns/dynamic-gaussian-marbles/blob/main/preprocess/README.md
```
scene_datadir
├── camera
│   └── C_XXXXX.json
│   └── ...
├── rgb
│   └── 1x
│       ├── C_XXXXX.png
│       └── ...
├── depth
│   └── 1x
│       ├── C_XXXXX.npy
│       └── ...
├── segmentation
│   └── 1x
│       ├── C_XXXXX.npy
│       └── ...
├── tracks
│   └── 1x
│       ├── track_XXXXX.npy
│       └── ...
└── splits
│   ├── train.json
│   └── val.json
│── scene.json
└── dataset.json 
```

### running
- python train.py --data_dir ./data/nvidia/Balloon1 --config configs.dgmarbles_nvidia --outdir ./out
- python train.py --data_dir ./data/real-world/coyote --config configs.dgmarbles_realworld

## MoSca
### Setup
- used check_missing.py to download requirements
- download some model weights: 
    - `gdown --id 15tveiv7ZkvBBAN3qkkB7Zfky9d7vSqLD -O weights.zip`
    - `unzip weights.zip -d ./weights`
- downloaded 4 pip custom built pkgs
- cupy version has to be cupy-cuda11x==12.2.0
- diffusers-0.33.1; huggingface-hub==0.30.1; xformers-0.0.24+cu118

### Run


### Potential problems
ERROR: pip's dependency resolver does not currently take into account all the packages that are installed. This behaviour is the source of the following dependency conflicts.
nerfstudio 0.3.4 requires viser==0.1.3, but you have viser 0.2.23 which is incompatible.
nuscenes-devkit 1.1.11 requires matplotlib<3.6.0, but you have matplotlib 3.10.1 which is incompatible.
nuscenes-devkit 1.1.11 requires Shapely<2.0.0, but you have shapely 2.1.0 which is incompatible.
unidepth 0.1 requires protobuf==4.25.3, but you have protobuf 3.20.3 which is incompatible.
