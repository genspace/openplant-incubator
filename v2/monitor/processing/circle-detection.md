## Circle Detection

### Basic Edge Detection

#### Sobel Operator

The Sobel Operator convolves two kernels, $K_x$ and $K_y$, indepdendently over an image.

$$
\begin{align*}
K_x=\begin{bmatrix}
-1 & 0 & 1\\
-2 & 0 & 2\\
-1 & 0 & 1
\end{bmatrix}\\\\
K_y=\begin{bmatrix}
-1 & -2 & -1\\
0 & 0 & 0\\
1 & 2 & 1
\end{bmatrix}
\end{align*}
$$

The resulting values are then combined using the follwing formula:

$$
mag=\sqrt{mag_x^2+mag_y^2}
$$

This computes an image gradient that can be used to identify the sharpest edges in an image.

#### Canny Edge Detector

Gradient image is often too noisy to be used directly. The Canny edge detector is a multi-stage algorithm that will clean the image and only keep the strongest edges.

The Canny edge detector successively applies the following operations:

- **Gaussian filter:** aims to smooth the image to remove some noise, convolving a filter that blends the discrete values together using a guassian normal distribution
- **Compute image gradient:** compute a gradient using something like the sobel operator that helps to identify edge features
- **Non-maximum suppression**: compute the direction of the gradient using the formula $atan2(mag_y, mag_x)$. only keep the pixels that are the maximum among their neighbors in the direction of the gradient.
- **Edge tracking:** link together the stronger edges and remove unlinked elements. done by passing two thresholds over the image, `low` and `high`. edges lower than `low` are removed. edges higher than `high` are marked as strong. edges between `low` and `high` are marked as weak unless they are next to a strong edge, in which case they are marked as strong.

### Circle Hough Transform

The parametric equation of a circle of radius $r$ and center $(a, b)$ is:
$$
x = a + r * cos(t)\\
y = a + r * sin(t)\\
\text{with}\quad t \in [0, 2\pi)
$$
The set of all possible circles is defined by all the possible values for $a$, $b$, and $r$. For each circle, the pixels that belong to the circle can be found by iterating over some possible values of $t$. To reduce the amount of circles to take into consideration, we only consider the values for $r$ between $r_{min}$ and $r_{max}$. 

To do the detection, we iterate over the coordinates of each strong edge (x, y) and compute the coordinates of the center of all circles that intersect with the edge. For each of these cirlces defined as (a, b, r), we increment a counter.

In order to select which circles are good enough, we use a threshold (at least 40% of the pixels of a circle must be detected) and we exlude cirlces that are too close to eachother.



