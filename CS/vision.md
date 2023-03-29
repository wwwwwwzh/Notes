# Ransac
## 
1. Randomly choose s samples. Typically s = minimum sample size that lets you fit a model
2. Fit a model (e.g., line) to those samples
3. Count the number of inliers that approximately fit the model
4. Repeat N times
5. Choose the model that has the largest set of inliers

3d rotation

# Camera Calibration
Solution x is the column of V corresponding to smallest singular value of SVD

Equivalently, solution x is the Eigenvector corresponding to smallest Eigenvalue of ATA

![](/images/P_M.png)
![](/images/esti-P2.png)
![](/images/esti-P.png)
![](/images/P-to-RT.png)

# Epipolar 
## E and F
![](/images/skew-sym.png)
![](/images/E_M3.png)
![](/images/E_M2.png)
![](/images/E_M.png)
![](/images/E_F.png)
![](/images/F_M.png)

## Estimate
![](/images/8-point.png)
