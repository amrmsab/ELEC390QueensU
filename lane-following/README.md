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

$$75\\% \times \\{\text{status} == \text{success}\\} + \left( 10\\% \times \frac{0.6}{\max(\text{deviation-center-line\\_median}, 0.45)} \right)$$

$$\quad + \left( 10\\% \times \frac{\min(\text{driven\\_lanedir\\_consec\\_median}, 8)}{6} \right) + \left( 5\\% \times \frac{\text{survival\\_time\\_median}}{60} \right)$$

## Submission

What you need to submit:

- [ ] Find the `.md` markdown file in your assignment repository that has the name `submission.md`.
- [ ] In the markdown file, on the first line, write the number of your submission to the duckietown challenges hub. This is the 5 digit number that identifies your submission. This must be the same number that ends the url to your submission page (https://challenges.duckietown.org/v4/humans/submissions/#####) i.e., Only write #####
- [ ] In the markdown file, on the second line, write your username, i.e., user####

> [!caution]
> Make sure to not add anything else as that may interfere with the autograder.
> Do not modify `submission_test.md` so that GitHub Actions verifies that you have correctly included your submission number.
> Make sure to submit your own work.

Our autograder will do the following:

1) access your submission on the cross-check the user name on the submissions page to confirm that it is your submission.
2) scroll down and confirm at least one success flag under the status column.
3) read all of `deviation-center-line_median`, `driven_lanedir_consec_median`, `survival_time_median` scores and will grant you best scores.
