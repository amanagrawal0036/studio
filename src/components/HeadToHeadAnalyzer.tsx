"use client";

import { useState } from "react";
import { Button } from "@/components/ui/button";
import { Select, SelectContent, SelectItem, SelectTrigger, SelectValue } from "@/components/ui/select";
import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card";
import { IplStats } from "@/services/ipl";
import { useToast } from "@/hooks/use-toast";
import { useDashboardContext } from "@/contexts/dashboard-context";

const mockStats1: IplStats = {
  matchesPlayed: 150,
  runsScored: 5000,
  wicketsTaken: 80,
  battingAverage: 33.33,
};

const mockStats2: IplStats = {
  matchesPlayed: 120,
  runsScored: 4500,
  wicketsTaken: 70,
  battingAverage: 37.50,
};

export const HeadToHeadAnalyzer = () => {
  const [compareBy, setCompareBy] = useState("Player vs Player");
  const [entity1, setEntity1] = useState("");
  const [entity2, setEntity2] = useState("");
  const [stats1, setStats1] = useState<IplStats | null>(null);
  const [stats2, setStats2] = useState<IplStats | null>(null);
  const { toast } = useToast();
  const { addInsight } = useDashboardContext();

  const handleCompareEntities = async () => {
    // Placeholder: Replace with actual backend calls to fetch stats
    setStats1(mockStats1);
    setStats2(mockStats2);
  };

  const handleSaveComparison = () => {
    if (stats1 && stats2) {
      addInsight({
        type: "comparison",
        query: `Comparison between ${entity1} and ${entity2} by ${compareBy}`,
        result: `Stats for ${entity1}: ${JSON.stringify(stats1)}, Stats for ${entity2}: ${JSON.stringify(stats2)}`,
      });
      toast({
        title: "Comparison Saved",
        description: "Comparison saved to your history.",
      });
    } else {
      toast({
        variant: "destructive",
        title: "Error",
        description: "No comparison to save.",
      });
    }
  };

  return (
    <Card className="space-y-4">
      <CardHeader>
        <CardTitle>⚔️ Head-to-Head Analyzer</CardTitle>
      </CardHeader>
      <CardContent className="space-y-4">
        <Select onValueChange={setCompareBy} defaultValue={compareBy}>
          <SelectTrigger>
            <SelectValue placeholder="Compare by:" />
          </SelectTrigger>
          <SelectContent>
            <SelectItem value="Player vs Player">Player vs Player</SelectItem>
            <SelectItem value="Team vs Team">Team vs Team</SelectItem>
          </SelectContent>
        </Select>

        <div className="grid grid-cols-2 gap-4">
          <div>
            <label className="block text-sm font-medium leading-none mb-2">Entity 1</label>
            <input
              type="text"
              placeholder="Enter Entity 1"
              value={entity1}
              onChange={(e) => setEntity1(e.target.value)}
              className="w-full rounded-md border border-input bg-background px-3 py-2 text-sm ring-offset-background file:border-0 file:bg-transparent file:text-sm file:font-medium placeholder:text-muted-foreground focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-ring focus-visible:ring-offset-2 disabled:cursor-not-allowed disabled:opacity-50"
            />
          </div>
          <div>
            <label className="block text-sm font-medium leading-none mb-2">Entity 2</label>
            <input
              type="text"
              placeholder="Enter Entity 2"
              value={entity2}
              onChange={(e) => setEntity2(e.target.value)}
              className="w-full rounded-md border border-input bg-background px-3 py-2 text-sm ring-offset-background file:border-0 file:bg-transparent file:text-sm file:font-medium placeholder:text-muted-foreground focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-ring focus-visible:ring-offset-2 disabled:cursor-not-allowed disabled:opacity-50"
            />
          </div>
        </div>

        <Button onClick={handleCompareEntities}>Compare Entities</Button>

        {stats1 && stats2 && (
          <div className="grid grid-cols-2 gap-4 mt-4">
            <StatCard title="Entity 1 Stats" stats={stats1} />
            <StatCard title="Entity 2 Stats" stats={stats2} />
             <Button variant="secondary" onClick={handleSaveComparison}>Save Comparison</Button>
          </div>
        )}
      </CardContent>
    </Card>
  );
};

const StatCard = ({ title, stats }: { title: string; stats: IplStats }) => {
  const betterStyle = "font-semibold text-accent"; // Style for highlighting better stats

  return (
    <Card>
      <CardHeader>
        <CardTitle>{title}</CardTitle>
      </CardHeader>
      <CardContent className="space-y-2">
        <p>Matches Played: <span className={stats.matchesPlayed > mockStats2.matchesPlayed ? betterStyle : ""}>{stats.matchesPlayed}</span></p>
        <p>Runs Scored: <span className={stats.runsScored > mockStats2.runsScored ? betterStyle : ""}>{stats.runsScored}</span></p>
        <p>Wickets Taken: <span className={stats.wicketsTaken > mockStats2.wicketsTaken ? betterStyle : ""}>{stats.wicketsTaken}</span></p>
        <p>Batting Average: <span className={stats.battingAverage > mockStats2.battingAverage ? betterStyle : ""}>{stats.battingAverage}</span></p>

      </CardContent>
    </Card>
  );
};
