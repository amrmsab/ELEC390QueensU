# Braitenberg

A Braitenberg vehicle, named after a thought experiment of cyberneticist Valentino Braitenberg, is a self-moving vehicle that operates autonomously using its sensor inputs and primitive logic. 
One sensing a stimulus, the vehicle adapts it course of movement to drive towards a certain goal and/or avoid certain situations.

## Description

In this learning experiment, the stimulus is seeing a duckie and the vehicle must adapt its course of motion to not run over the duckie.

You will design the Duckiebot to navigate a plane without running over duckies.

- You will process the camera's image searching for yellow color indicating the presence of a duckie in front of the Duckiebot.
- You will conceive an algorithm (calculation over the pixels of the image) that takes in the camera's image and outputs instructions (actuation) to the Duckiebot's wheels.
The actuation should prolong the distance driven and time the Duckiebot navigates the place without running over a duckie.
- The actuation to the right and left wheel motors are calculated as below:

    left\_motor  = const + gain *  np.sum( LEFT * preprocess(image) )
    right\_motor = const + gain *  np.sum( RIGHT * preprocess(image) )

`const` and `gain` are in the `agent.py` file.
`LEFT` and `RIGHT` are masks that you will design in the `connections.py` file.

You will design the `preprocess()` function to detect the Duckiebots based on their color.


1) `braitenberg01.ipynb`: A brief intro image manipulation on Python.
2) `braitenberg02.ipynb` You will construct a color filter that detects yellow duckies in an image.
3) `braitenberg03.ipynb`: You will complete an algorithm that takes in a image from the duckie's camera feed, detects the yellow duckies in the image based on the previous exercise,
   and then performs a calculation over the image's pixels that actuates the wheels to avoid running over the duckies.

## Grading

After finishing the exercise in notebook `03-Braintenberg`, building your code, and testing it in simulation, you should be prompted to check your test results in a folder `/tmp/<USER>/dts-code-workbench/<DATE>/challenges`.

Note that you might have to wait a bit for the simulation to finish and output results.

One way to access this location via the GUI on Ubuntu is to go to `Files/Other Locations/Computer` and then navigate to this folder.

Once there, view the `challenge-results/challenge-results.yaml` file. You can use this to gauge how the duckietown servers will evaluate your submission.

The grading metric is based on the distance from the starting point.

Your submission will be auto-graded. Your grade (out of 100%) will be calculated as:

$$75\\% \times \\{\text{status} == \text{success}\\} + 25\\% \times \frac{\max(\text{distance-from-start\\_mean}, 6)}{5}$$

You have an opportunity to get up to 5% bonus.
Note that the maximum distance from start is 5.3 on the [Braitenberg scoreboard](https://challenges.duckietown.org/v4/). 

If you navigate through the `challenge-evaluation-output` folder, you will stumble upon GIFs and mp4 videos that will show you what your Duckiebot did in simulation. 
Check them out to improve the robot. We recommend downloading VLC Media Player on Ubuntu (on WLS) to play the mp4 videos.

What you need to submit:

- [ ] Create a new `.md` markdown file in your assignment repository and name it `submission.md`.
- [ ] Write in your markdown file only the link to your submission on the duckietown challenges hub. i.e., the .md file should only contain the following text: `https://challenges.duckietown.org/v4/humans/submissions/<SUBMISSION\_NUMBER>`

> [!caution]
> Make sure to not add anything else as that may interfere with the autograder.

Our autograder will do the following:

1) Will cross-check the user name on the submissions page to confirm that it is your submission.
2) Will confirm at least one success flag under the status column.
3) Will scroll down and read all of `distance-from-start_mean` scores and will grant you the maximum score. 