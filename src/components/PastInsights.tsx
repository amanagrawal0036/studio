"use client";

import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card";
import { useDashboardContext } from "@/contexts/dashboard-context";

export const PastInsights = () => {
  const { insights } = useDashboardContext();

  return (
    <Card>
      <CardHeader>
        <CardTitle>📁 Past Insights</CardTitle>
      </CardHeader>
      <CardContent>
        {insights.length === 0 ? (
          <p>No saved insights yet.</p>
        ) : (
          <ul>
            {insights.map((insight, index) => (
              <li key={index} className="mb-4">
                <p className="font-semibold">{insight.query}</p>
                <p>{insight.result}</p>
              </li>
            ))}
          </ul>
        )}
      </CardContent>
    </Card>
  );
};
