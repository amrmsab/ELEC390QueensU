# Collision Avoidance

In this learning experience, your Duckiebot will navigate a straight road until it sees a Duckie crossing on the road. 
The Duckiebot needs to drive as close to the Duckie as possible and then stop before hitting it.

You will develop and train a convolutional neural network (CNN) to detect the Duckie and then complete the algorithm to stop the Duckiebot.

You can access the learning experience here: <https://github.com/duckietown/duckietown-lx/tree/mooc2022/object-detection/notebooks>

You will complete the following notebooks:
- `cnn.ipynb`: Directs you to Google Colab notebook where you can get familiar with CNNs.

- `setup.ipynb`: You will learn how simulations can be used to collect synthetic data to be used to train neural networks.

- `training.ipynb`: You will train your CNN using the real-world and synthetic images to detect Duckies.

- `training.ipynb`: You will complete an algorithm that detects the Duckiebots and actuates the Duckiebot until it is as close as possible to the Duckie and then stops the Duckiebot before colliding with the Duckie.

## Grading

The grading metrics are:
- Traveled distance - median distance traveled along a lane, discretized to tiles. [Scoreboard](https://challenges.duckietown.org/v4/) maximum is 4.8.
- Survival time - median survival time. The simulation terminates when the car crashes with a duckie. Scoreboard maximum is 60.

Your submission will be auto-graded. 

Your grade (out of 100\%) will be calculated as:
$$\left( 75\\% \times \\{\text{status} == \text{success}\\} \right) + \left( 20\\% \times \frac{\min(\text{driven\\_lanedir\\_consec\\_median}, 5)}{4} \right) + \left( 5\\% \times \frac{\text{survival\\_time\\_median}}{60} \right)$$

## Submission

- [ ] Create a new `.md` markdown file and name it `submission.md`.

Write in your markdown file only the link to your submission on the duckietown challenges hub. i.e., the .md file should only contain the following text:
`https://challenges.duckietown.org/v4/humans/submissions/<SUBMISSION\_NUMBER>`

> [!caution]
> Make sure to not add anything else as that may interfere with the autograder.

Our autograder will do the following:
1) Will cross-check the User name on the submissions page to confirm that it is your submission.
2) Will confirm atleast one success flag under the status column.
3) Will scroll down and read the `driven_lanedir_consec_median` `survival_time_median` scores and will grant you best scores.
