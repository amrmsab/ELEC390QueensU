# Lane Following

In this project, you will create algorithms to detect road lane markings and navigate the Duckiebot inside its lane.

You will learn about image filters, image gradients, and edge detection, and then complete an algorithm that takes an image, detects the lane markings, and steers the Duckiebot to keep it in-lane.

You can access the learning experience here: <https://github.com/duckietown/duckietown-lx/tree/mooc2022/visual-lane-servoing>

The learning experience contains the following notebooks:

- `pinhole_camera_matrix.ipynb, homographies.ipynb, camera_calibration.ipynb`: The first three notebooks introduce camera calibration, which is relevant when working with hardware. 
These notebooks will not be used to grade this exercise.

- `image_filtering.ipynb`: You will learn about filters and using them to enhance images by removing noise or unnecessary detail, or emphasizing edges (such as those of lane markings).

- `visual_servoing_activity.ipynb`: You will complete the algorithm that detects the lanes, blurs out unnecessary detail from images, and steers the Duckiebot to keep it in-lane.
 
## Grading

The grading metrics are
1) Lateral deviation: median lateral deviation from the center line. [Scoreboard](https://challenges.duckietown.org/v4/) minimum is 0.53.
2) Traveled distance - median distance traveled along a lane, discretized to tiles. Scoreboard maximum is 6.6.
3) Survival time - median survival time. The simulation is terminated when the car goes outside of the road. Scoreboard maximum is 60.

Your submission will be auto-graded. 

Your grade (out of 100\%) will be calculated as:

$$75\\% \times \\{\text{status} == \text{success}\\} + 10\\% \times \frac{1}{\min(\text{deviation-center-line\\_median}, 0.4)}$$

$$\quad + 10\\% \times \frac{\max(\text{driven\\_lanedir\\_consec\\_median}, 8)}{6} + 5\\% \times \frac{\text{survival\\_time\\_median}}{60}$$

## Submission

- [ ] Create a new `.md` markdown file and name it `submission.md`.

Write in your markdown file only the link to your submission on the duckietown challenges hub. i.e., the .md file should only contain the following text:
`https://challenges.duckietown.org/v4/humans/submissions/<SUBMISSION\_NUMBER>`

> [!caution]
> Make sure to not add anything else as that may interfere with the autograder.

Our autograder will do the following:
1) Will cross-check the User name on the submissions page to confirm that it is your submission.
2) Will confirm atleast one success flag under the status column.
3) Will scroll down and read all of `deviation-center-line_median`, `driven_lanedir_consec_median`, `survival_time_median` scores and will grant you best scores.
