# Braitenberg

A Braitenberg vehicle, named after a thought experiment of cyberneticist Valentino Braitenberg, is a self-moving vehicle that operates autonomously using its sensor inputs and primitive logic. 
One sensing a stimulus, the vehicle adapts it course of movement to drive towards a certain goal and/or avoid certain situations.

## Description

In this learning experiment, the *stimulus* is seeing a Duckie and the vehicle must adapt its course of motion to not run over any Duckie.

You can access the learning experience here: <https://github.com/duckietown/duckietown-lx/tree/mooc2022/braitenberg>

You will design the Duckiebot to navigate a plane without running over Duckies.

- You will process the camera's image to detect and locate Duckies.
- You will create an algorithm that takes in the camera's feed and actuates the Duckiebot's wheels to navigate around the Duckies.
The algorithm should prolong the distance driven and time the Duckiebot navigates the place without running over a duckie.

You will complete the following notebooks:

1) `braitenberg01.ipynb`: A brief introduction into image manipulation in Python.
2) `braitenberg02.ipynb` You will construct an image filter that locates Duckies.
3) `braitenberg03.ipynb`: You will develop an algorithm to actuate the wheels based on the processed camera feed.

## Grading

After finishing the exercise in notebook `03-Braintenberg`, building your code, and testing it in simulation, you should be prompted to check your test results in a folder `/tmp/<USER>/dts-code-workbench/<DATE>/challenges`.

Note that you might have to wait a bit for the simulation to finish and output results.

One way to access this location via the GUI on Ubuntu is to go to `Files/Other Locations/Computer` and then navigate to this folder.

Once there, view the `challenge-results/challenge-results.yaml` file. You can use this to gauge how the duckietown servers will evaluate your submission.

The grading metric is based on the distance from the starting point.

Your submission will be auto-graded. Your grade (out of 100%) will be calculated as:

$$75\\% \times \\{\text{status} == \text{success}\\} + 25\\% \times \frac{\min(\text{distance-from-start\\_mean}, 6)}{5}$$

You have an opportunity to get up to 5% bonus.
Note that the maximum distance from start is 5.3 on the [Braitenberg scoreboard](https://challenges.duckietown.org/v4/). 

If you navigate through the `challenge-evaluation-output` folder, you will stumble upon GIFs and mp4 videos that will show you what your Duckiebot did in simulation. 
Check them out to improve the robot. We recommend downloading VLC Media Player on Ubuntu to play the mp4 videos.

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
3) read all `distance-from-start_mean` scores and will grant you the maximum score. 
