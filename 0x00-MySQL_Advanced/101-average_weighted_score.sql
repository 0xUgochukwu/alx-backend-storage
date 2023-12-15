-- creates a stored procedure ComputeAverageWeightedScoreForUsers that computes and store the average weighted score for all students

DROP PROCEDURE IF EXISTS ComputeAverageWeightedScoreForUsers;

DELIMITER %%
CREATE PROCEDURE ComputeAverageWeightedScoreForUsers()
BEGIN
  -- Create a temporary table to store the computed averages
  CREATE TEMPORARY TABLE tmp_averages AS
    SELECT U.id, SUM(C.score * P.weight) / SUM(P.weight) AS avg_score
    FROM users AS U
    JOIN corrections AS C ON U.id = C.user_id
    JOIN projects AS P ON C.project_id = P.id
    GROUP BY U.id;

  -- Update the users table with the computed averages
  UPDATE users AS U
  JOIN tmp_averages AS T ON U.id = T.user_id
  SET U.average_score = T.avg_score;

  -- Drop the temporary table
  DROP TEMPORARY TABLE IF EXISTS tmp_averages;
END
%% DELIMITER;
