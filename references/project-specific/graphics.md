See [reference.md](../../reference.md#graphics)
 
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
- monocular synthetic video
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
            "transform_matrix": [
                [
                    -0.9998774528503418,
                    0.0020596340764313936,
                    -0.015522046014666557,
                    -0.06257136911153793
                ],
                [
                    -0.015658097341656685,
                    -0.1315218210220337,
                    0.9911895990371704,
                    3.9956130981445312
                ],
                [
                    2.3283064365386963e-10,
                    0.9913111329078674,
                    0.13153794407844543,
                    0.5302464365959167
                ],
                [
                    0.0,
                    0.0,
                    0.0,
                    1.0
                ]
            ]
        }
    ]
```

### Dynerf (meta)
- multiview (18) real video, 10s.


# Papers
## Defocus
### D2DF

[{'lr': 3.406460345289806e-05, 'betas': (0.9, 0.999), 'eps': 1e-08, 'weight_decay': 0, 'amsgrad': False, 'maximize': False, 'foreach': None, 'capturable': False, 'differentiable': False, 'fused': None, 'params': [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69]}]
## Dynamic
### 4DGS
- training
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



# Project
## 4DGS-deblur
### Env
- python 3.9
- mamba
- 4dgs, d2rf pkgs, torch with cuda11.8
- FAILED: colmap with conda cmake
- mamba install conda-forge::colmap

### Code
scene->dataset_reader
- readColmapSceneInfo: needs "images" and "sparse/0"

## D2RF
### Code
config
- start_frame end_frame are not used


load_llff
- only images_bokeh is used as image data (sorted)
- the downloaded dataset used factor 2 which is default llff factor and images_2 contains downsampled bokeh image
- llff_holdout is  2 which means it's using every second image (left for train, right for test)
- the internal dimensions and return dim is a little different, the final shape for poses is (N_imgs, 3, 5) and for imgs (N_imgs, 360, 940, 3)