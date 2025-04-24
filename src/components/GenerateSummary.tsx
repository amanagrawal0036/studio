"use client";

import { useState } from "react";
import { Button } from "@/components/ui/button";
import { Textarea } from "@/components/ui/textarea";
import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card";
import { useToast } from "@/hooks/use-toast";
import { generateSummary } from "@/ai/flows/generate-summary";

export const GenerateSummary = () => {
  const [prompt, setPrompt] = useState("");
  const [summary, setSummary] = useState("");
  const [isLoading, setIsLoading] = useState(false);
    const { toast } = useToast();

  const handleGenerateSummary = async () => {
    setIsLoading(true);
    try {
      const result = await generateSummary({ entityName: prompt });
      setSummary(result.summary);
            toast({
                title: "Summary Generated",
                description: "Summary generated successfully.",
            });
    } catch (error: any) {
            toast({
                variant: "destructive",
                title: "Error",
                description: error.message || "Failed to generate summary.",
            });
      console.error("Error generating summary:", error);
      setSummary("Error generating summary. Please try again.");
    } finally {
      setIsLoading(false);
    }
  };

  const handleSaveSummary = () => {
        toast({
            title: "Summary Saved",
            description: "Summary saved to your history.",
        });
    // TODO: Implement save functionality
  };

  return (
    <Card className="space-y-4">
      <CardHeader>
        <CardTitle>📊 Generate Summary</CardTitle>
      </CardHeader>
      <CardContent className="space-y-4">
        <Textarea
          placeholder="Enter player or team name"
          value={prompt}
          onChange={(e) => setPrompt(e.target.value)}
        />
        <Button onClick={handleGenerateSummary} disabled={isLoading}>
          {isLoading ? "Generating..." : "Generate Summary"}
        </Button>
        {summary && (
          <div className="mt-4">
            <h3>Summary:</h3>
            <p>{summary}</p>
            <Button variant="secondary" onClick={handleSaveSummary}>
              Save Summary
            </Button>
          </div>
        )}
      </CardContent>
    </Card>
  );
};
