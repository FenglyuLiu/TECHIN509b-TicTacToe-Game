# Week 9 - Lab Submission (Visualizing TicTacToe Game Data) 

In the first text cell of the notebook, add the link to your Github repository that includes the logs and related code in the following format: "https://github.com/xxxxxxx/repository_name.git"

Implement the additional features to your TicTacToe game:

The game should record all the winners in a 'database' file, which can just be a CSV or text file in the logs directory
The log file should contain any relevant data needed to perform statistics about the game and players
Using the Google Colab notebook environment, upload the log file and import and read the logs in the Colab notebook
Report on at least 3 interesting statistics about the games and players using tables (e.g. global ranks, wins/losses/draws, etc).
Create at least 3 plots of the game and player data using Matplotlib 
The code used to record data during the game needs to be added to your repository
Note: when you create log data for this assignment, you need to Add and commit that data also to your repository, so that it can be later uploaded to the Google Colab site. This will allow the grader to log your log data and re-run the cells in your notebook


# Week 10 - Lab Submission (TicTacToe Game Data Science) 

In this assignment, we will build upon our previous work to analyze the game log data:

Update your game logs to include data that allows you to know which square was played first and whether the game resulting in a win, loss or draw by that first player
Generate at least 30 games played in your logs
Provide some descriptive statistics about the game logs, including the new data, using Pandas
Build a simple linear regression model to understand which position is best to start the game with using scikit-learn
Report the model fit parameters and the likelihood of winning from each game position (which can be simplified to corner, center, or middle)
You do not need to worry about training vs testing data
