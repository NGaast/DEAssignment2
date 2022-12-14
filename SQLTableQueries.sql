CREATE TABLE IF NOT EXISTS worldcup.statistics (
  fixture_id INT64,
  shots_on_goal INT64,
  shots_off_goal INT64,
  total_shots INT64,
  blocked_shots INT64,
  shots_outside_box INT64,
  shots_inside_box INT64,
  fouls INT64,
  corner_kicks INT64,
  offside INT64,
  ball_possesion STRING,
  yellow_cards INT64,
  red_cards INT64,
  goalkeeper_saves INT64,
  total_passes INT64,
  passes_accurate INT64,
  passes_perc STRING
);

CREATE TABLE IF NOT EXISTS worldcup.fixture (
  id INT64,
  league_id INT64,
  date DATE,
  time TIMESTAMP,
  away_id INT64,
  home_id INT64,
  round_id INT64,
  referee_id INT64,
  season_id INT64,
  halftime_home INT64,
  halftime_away INT64,
  fulltime_home INT64,
  fulltime_away INT64,
  extratime_home INT64,
  extratime_away INT64,
  penalty_home INT64,
  penalty_away INT64
);

CREATE TABLE IF NOT EXISTS worldcup.rounds (
  id INT64,
  round INT64
);

CREATE TABLE IF NOT EXISTS worldcup.teams (
  id INT64,
  name STRING
);

CREATE TABLE IF NOT EXISTS worldcup.season (
  id INT64,
  season INT64
);

CREATE TABLE IF NOT EXISTS worldcup.referee (
  id INT64,
  referee STRING
);