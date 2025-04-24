/**
 * Represents a player in the IPL.
 */
export interface Player {
  /**
   * The name of the player.
   */
  name: string;
  /**
   * The team the player plays for.
   */
  team: string;
}

/**
 * Represents a team in the IPL.
 */
export interface Team {
  /**
   * The name of the team.
   */
  name: string;
  /**
   * The city the team represents.
   */
  city: string;
}

/**
 * Represents IPL statistics for a player or team.
 */
export interface IplStats {
  /**
   * The number of matches played.
   */
  matchesPlayed: number;
  /**
   * The number of runs scored.
   */
  runsScored: number;
  /**
   * The number of wickets taken.
   */
  wicketsTaken: number;
  /**
   * The batting average.
   */
  battingAverage: number;
}

/**
 * Asynchronously retrieves IPL statistics for a given player.
 *
 * @param player The player for which to retrieve statistics.
 * @returns A promise that resolves to an IplStats object containing the player's statistics.
 */
export async function getPlayerStats(player: Player): Promise<IplStats> {
  // TODO: Implement this by calling an API.

  return {
    matchesPlayed: 100,
    runsScored: 3000,
    wicketsTaken: 50,
    battingAverage: 30.00,
  };
}

/**
 * Asynchronously retrieves IPL statistics for a given team.
 *
 * @param team The team for which to retrieve statistics.
 * @returns A promise that resolves to an IplStats object containing the team's statistics.
 */
export async function getTeamStats(team: Team): Promise<IplStats> {
  // TODO: Implement this by calling an API.

  return {
    matchesPlayed: 100,
    runsScored: 15000,
    wicketsTaken: 500,
    battingAverage: 30.00,
  };
}
