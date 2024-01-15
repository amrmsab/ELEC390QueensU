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
$$\left( 75\\% \times \\{\text{status} == \text{success}\\} \right) + \left( 20\\% \times \frac{\min(\text{driven\\_lanedir\\_consec\\_median}, 5)}{4.5} \right) + \left( 5\\% \times \frac{\text{survival\\_time\\_median}}{60} \right)$$

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
3) read the `driven_lanedir_consec_median` `survival_time_median` scores and will grant you best scores.
