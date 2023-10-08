# Board-Game-Recommendator

## Data

- id.txt

  This file contains IDs of the top 2000 board games obtained from BoardGameGeek.com.

- board-game.csv

  This dataset contains multiple variants obtained through the API provided by BoardGameGeek.com. The rows are ordered according to the IDs listed in id.txt. Here is an explanation of each column.

  | Column       | Description                                                  |
  | ------------ | ------------------------------------------------------------ |
  | Name         | The name of the board game.                                  |
  | Year         | Year of publication.                                         |
  | min_players  | Minimum number of players required.                          |
  | max_players  | Maximum number of players allowed.                           |
  | min_playtime | Minimum playing time per game (in minutes).                  |
  | max_playtime | Maximum playing time per game (in minutes).                  |
  | min_age      | Minimum age requirement for players.                         |
  | category     | Categories to which the board game belongs.                  |
  | mechanic     | Game mechanics employed in the game.                         |
  | userrated    | Total number of users who have rated the game.               |
  | avg_rate     | Average rating score (out of 10) given by users.             |
  | rank         | Ranking in the overall Board Game Rank.                      |
  | owned        | Number of users who own the board game.                      |
  | trading      | Number of users who are selling the board game.              |
  | wanting      | Number of users who are willing to trade for the board game. |
  | wishing      | Number of users who have added the board game to their wishlists. |
  | num_comments | Total number of user comments and reviews for the game.      |
  | num_weights  | Total number of user votes on the game's weight or complexity. |
  | avg_weight   | Average weight (difficulty/complexity) score of the board game. The score ranges from 1 (Light) to 5 (Heavy). |

- prices.csv

  The columns represent online stores selling the corresponding board games, such as Amazon and Noble Knight Games. The rows are arranged in the same order as the IDs in id.txt. Please note that approximately 228 rows do not have any price values.

## Todo

- Find the changes in popular categories and mechanics over the years.
- Apply NLP methods to descriptions/categories/mechanisms to find their relations with rating/score.
- Find the relation between categories/mechanics and weight.

